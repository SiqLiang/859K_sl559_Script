library(raster)
library(rgdal)
library(rgbif)
library(dplyr)
library(beepr)
library(auk)
library(leaflet)
library(lubridate)
library(spdplyr)
library(alphahull)
library(rgeos)
library(maptools)
library(mapview)
library(gstat)
library(leaflet)
library(RColorBrewer)
library(htmltools)
library(rgbif)
library(stringr)
library(sf)
library(pushoverr)
library(rgeos)

setwd("D:/Bird Range Mapping/MapLayers")
set_pushover_user(user="uy3q1pxmhksvw3haeqrwbduqwf5zg8")
set_pushover_app(token="ag4d2takwrzkapbse55bz47w582f2x")

rgdal_show_exportToProj4_warnings="none"
auk_set_ebd_path("D:/Bird Range Mapping/MapLayers/eBird_data", overwrite = FALSE)

##################SET VARIABLES################
validate = FALSE
keep.hi = TRUE
keep.gbif = TRUE
buffer = 1000 #set in m
non.detect.size = 5 #set in Km
non.detect.thresh = 25
targets <- read.csv("./target_list_final.csv", header = TRUE)
targets <- targets[,2]
################################################

#Load Functions
arc2line <- dget("Functions/arc2line.R")
ahull2lines <- dget("Functions/ahull2lines_v3.R")
spLines2poly <- dget("Functions/spLines2poly_v2.R")
alphahull <- dget("Functions/alphahull_v4.R")
refineHabitat <- dget("Functions/refineHabitat_v2.R")
presAbs <- dget("Functions/presAbs.R")
nnInterpolate <- dget("Functions/nnInterpolate.R")

#Load Data
SAmer.proj <- CRS("+proj=aea +lat_1=-5 +lat_2=-42 +lat_0=-32 +lon_0=-60 +x_0=0 +y_0=0 +ellps=aust_SA +datum=WGS84 +units=m +no_defs")
WGS84.proj <- CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
land <- readOGR(dsn = '.', layer = "Amer_land")
forest <- raster("Hansen3.tif")
DEM <- raster("DEM_1km.tif")
all_spp <- readOGR(dsn = '.', layer = "Amer_spp2")
bl.elev <- read.csv("D:/Bird Range Mapping/MapLayers/BL_elevations2.csv", stringsAsFactors=FALSE)

#colors
hab.refine.col <- "#808080"
hab.final.col <- "#0d4201"
hull.col <- "#000000"
icon.col <- colorFactor(c("#414141", "#a9eb75"), domain = c(0,1))
stroke.col <- colorFactor(c("#000000", "#4d7e29"), domain = c(0,1))
iucn.col <- "#d6872d"
alpha.col <- "#6CD4FF"
###FULL LEGEND
# values = c("Presence Points", "Area of Habitat", "Possible Area of Habitat", "BirdLife Range", "Alpha Hull", "Historical/Incidental", "GBIF Points", 
#            "Training Points", "Testing Points")
# leg.col = c("#a9eb75", "#0d4201", "#808080", '#d6872d', "#6CD4FF", "#414141", "#FF00FF", "#C60404", "#0066cc")

##PARTIAL LEGEND
values = c("Presence Points", "Area of Habitat", "Possible Area of Habitat", "BirdLife Range", "Alpha Hull","Historical/Incidental", "GBIF Points")
leg.col = c("#a9eb75", "#0d4201", "#808080", '#d6872d', "#6CD4FF","#414141", "#FF00FF")

#Create blank table for final results
# report.table <- read.csv("D:/Bird Range Mapping/MapLayers/Report Table_10_5.csv", stringsAsFactors=FALSE)
# report.table <- report.table[,-1]
report.table <- data.frame(SciName = character(),
                           TotalPresences = double(),
                           ForestThresh = double(),
                           LowerElev = double(),
                           UpperElev = double(),
                           AOH = double(),
                           PAOH = double(),
                           TotalAOH = double(),
                           IUCNArea = double(),
                           IUCN.AOH = double(),
                           IUCN.AOH.Per = double(),
                           IUCN.PAOH = double(),
                           IUCN.PAOH.Per = double(),
                           IUCN.TAOH = double(),
                           IUCN.TAOH.Per = double(),
                           Errors = character(),
                           Time = double(),
                           stringsAsFactors = FALSE)
valid.table <- data.frame(SciName = character(),
                          Train.Total = double(),
                          ForestThresh = double(),
                          LowerElev = double(),
                          UpperElev = double(),
                          AOH = double(),
                          AOH.Change = double(),
                          PAOH = double(),
                          PAOH.Change = double(),
                          TotalAOH = double(),
                          TotalAOH.Change= double(),
                          IUCN.AOH = double(),
                          IUCN.AOH.Change = double(),
                          IUCN.PAOH = double(),
                          IUCN.PAOH.Change = double(),
                          IUCN.TAOH = double(),
                          IUCN.TAOH.Change = double(),
                          Valid.Total = double(),
                          Valid.AOH.Num = double(),
                          Valid.AOH.Per = double(),
                          Valid.PAOH.Num = double(),
                          Valid.PAOH.Per = double(),
                          Valid.Hull.Num = double(),
                          Valid.Hull.Per = double(),
                          Valid.Miss.Num = double(),
                          Valid.Miss.Per = double(),
                          stringsAsFactors = FALSE)

##########################EFFORT#################################

#OG eBird records
f_ebd <- "eBird_data/ebd_relAug-2020.txt"
f_sed <- "eBird_data/ebd_sampling_relAug-2020.txt"
ebd <- auk_ebd(f_ebd)
sed<-auk_sampling(f_sed)

extent <- extent(forest)
bbox <- c(extent@xmin, extent@ymin, extent@xmax, extent@ymax)
protocols <- valid_protocols[-c(21,23,38)]

checklists <- sed %>%
  auk_bbox(bbox) %>%
  auk_protocol(protocols) %>%
  auk_complete() %>% 
  auk_filter("eBird_filters/checklists.txt", overwrite = TRUE) %>%
  read_sampling()

checklists <- subset(checklists, !(protocol_type == "Traveling" & (duration_minutes > 180 | effort_distance_km > 7)))
coordinates(checklists) <- c("longitude", "latitude")
proj4string(checklists) <- WGS84.proj

#####################################################################

for (i in 180:length(targets)){
  has.error <- tryCatch({
    
    start.time <- Sys.time()
    
    sci.name <- as.character(targets[i])
    print(sci.name)
    sci.name.abbrv <- paste0(substring(sci.name,1,3),"_",unlist(strsplit(sci.name, " "))[2])
    report.table[i,"SciName"] <- sci.name

    spp.bl <- all_spp %>%
      filter(SCINAME == sci.name)
    spp.elev  <- bl.elev %>%
      filter(Scientific.name == sci.name) %>%
      select(Min, Max)
    
    dir.create (file.path("./Scratch/",sci.name.abbrv), showWarnings = FALSE)
    rasterOptions(tmpdir = file.path("./Scratch/",sci.name.abbrv))
    
    ####################################LOAD EBIRD DATA############################################
    
    if(file.exists(paste0("./eBird_text/",sci.name,"_ebird.txt"))){
      ebd_sp <- read.delim(paste0("./eBird_text/",sci.name,"_ebird.txt"), stringsAsFactors=FALSE)
      ebd_sp <- ebd_sp %>%
        filter(APPROVED == 1) %>%
        rename(
          decimalLatitude = LATITUDE,
          decimalLongitude = LONGITUDE,
          locality = LOCALITY,
          protocol_type = PROTOCOL.TYPE,
          duration_minutes = DURATION.MINUTES,
          effort_distance_km = EFFORT.DISTANCE.KM,
          checklist_id = SAMPLING.EVENT.IDENTIFIER,
          observation_date = OBSERVATION.DATE)
    }else{
      ebd_sp <- ebd %>%
        auk_species(sci.name) %>%
        auk_complete() %>%
        #auk_protocol(protocols) %>%
        auk_filter(paste0("eBird_text/",sci.name,"_ebird.txt"), overwrite = TRUE) %>%
        read_ebd()
      
      ebd_sp <- ebd_sp %>%
        filter(approved == "TRUE") %>%
        rename(
          decimalLatitude = latitude,
          decimalLongitude = longitude
        )
    }
    
    ebd_sp <- subset(ebd_sp, !(protocol_type == "Traveling" & (duration_minutes > 180 | effort_distance_km > 7)))
    ebd_sp <- ebd_sp[,colSums(is.na(ebd_sp))==0]
    
    ebd_sp <- ebd_sp %>%
      mutate(year = year(observation_date)) %>%
      mutate(url = paste0("https://ebird.org/checklist/", checklist_id)) %>%
      mutate(keep = ifelse((protocol_type == "Historical" |protocol_type == "Incidental"),"N","Y"))
    
    if(keep.hi){
      ebd_hi <- subset(ebd_sp, keep=="N")
      if(nrow(ebd_hi)>0){
        coordinates(ebd_hi) <- c("decimalLongitude", "decimalLatitude")
        proj4string(ebd_hi) <- WGS84.proj
      }
    }
    
    species <- subset(ebd_sp, keep=="Y")
    
    if(validate){
      species.test <- species[species$observation_date >= quantile(species$observation_date, 0.8, type = 1),]
      coordinates(species.test) <- c("decimalLongitude", "decimalLatitude")
      proj4string(species.test) <- WGS84.proj
      
      species.train <- species[species$observation_date < quantile(species$observation_date, 0.8, type =1),]
      species.train <- species.train[!duplicated(species.train[c("decimalLongitude", "decimalLatitude")]),]
      coordinates(species.train) <- c("decimalLongitude", "decimalLatitude")
      proj4string(species.train) <- WGS84.proj
      valid.table[i,"Train.Total"] <- length(species.train)
    }

    species <- species[!duplicated(species[c("decimalLongitude", "decimalLatitude")]),] 
    coordinates(species) <- c("decimalLongitude", "decimalLatitude")
    proj4string(species) <- WGS84.proj
    species <- species[!is.na(over(as(species, "SpatialPoints"),as(land, "SpatialPolygons"))),]
    
    report.table[i,"TotalPresences"] <- length(species)
    
    suppressWarnings(writeOGR(obj = species, dsn = './Spp_records', layer = paste0(sci.name.abbrv,"_ebd"), driver = "ESRI Shapefile", overwrite_layer = TRUE))
    
    #############################################################################
    ##################################GBIF POINTS################################
    #############################################################################

    if(keep.gbif){
      gbif<-occ_search(scientificName = sci.name,
                       hasCoordinate = TRUE,
                       limit = 5000,
                       fields = c('gbifID', 'scientificName','decimalLatitude', 'decimalLongitude','issues',
                                  'basisOfRecord', 'year', 'month', 'day', 'verbatimEventDate', 'collectionCode',
                                  'georeferenceVerificationStatus', 'identifier'))
      gbif <- gbif$data %>%
        dplyr::filter((is.na(year)== FALSE ) & (issues == ""|issues == "cdround"))
      if("georeferenceVerificationStatus" %in% colnames(gbif)){
        gbif <- gbif %>%
          dplyr::filter(is.na(georeferenceVerificationStatus)|(georeferenceVerificationStatus!="unverified"&
                                                                 georeferenceVerificationStatus!="verification required" &
                                                                 georeferenceVerificationStatus!="requires verification"))
      }
      gbif <- gbif %>%
        filter(!str_detect(identifier, "^OBS"))
      
      gbif <- gbif[!duplicated(gbif[c("decimalLongitude", "decimalLatitude")]),]
      gbif$date <- ymd(paste(gbif$year, gbif$month, gbif$day))
      
      if(nrow(gbif)>0){
        coordinates(gbif) <- c("decimalLongitude", "decimalLatitude")
        proj4string(gbif) <- WGS84.proj
      }
    }
    
    
    ############################HULL GENERATION#################################
    
    alpha.hull <- alphahull(points = species, 
                            polygon = spp.bl, 
                            #alpha = alpha, 
                            buffer = buffer)
    alpha <- alpha.hull[[2]]
    alpha.hull <- alpha.hull[[1]]
    st_write(obj = st_as_sf(alpha.hull), dsn = './AlphaHull', layer = paste0(sci.name.abbrv,"_hull_",round(alpha/1000)), driver = "ESRI Shapefile", overwrite_layer = TRUE, append=FALSE)
    
    ##########################HABITAT REFINEMENT#################################
    
    habitat <- refineHabitat(forest, DEM, presences = species, hull = alpha.hull, bl.min = spp.elev$Min, bl.max = spp.elev$Max)
    species <- habitat$Presences
    report.table[i,"ForestThresh"] <- habitat$ForestLimit
    report.table[i,"LowerElev"] <- habitat$DEMLimit.Min
    report.table[i,"UpperElev"] <- habitat$DEMLimit.Max
    habitat.refine <- habitat$HabitatRast
    cell.size <- area(habitat.refine, na.rm = TRUE)
    report.table[i,"TotalAOH"] <- sum(cell.size[!is.na(cell.size)])
    
    raster::writeRaster(habitat.refine, filename = paste0("RefinedHabitats/",sci.name.abbrv,"_habitat.tif"), format = "GTiff", overwrite = TRUE)
    
    ##########################PRESENCE/ABSENCE##################################
    
    effort <- presAbs(checklists = checklists,
                         presences = species,
                         hull = alpha.hull,
                         habitat = habitat.refine,
                         distance = non.detect.size,
                         threshold = non.detect.thresh)
    nn.points <- effort$Points
    non.detection <- effort$NonDetection
    
    ####################DISPLAY NON DETECT OUTSIDE OF HULL??###################
    # non.detect.coord <- xyFromCell(non.detection, cell = raster::Which(non.detection, cells = T), spatial = T)
    # non.hull.cells <- gDifference(non.detect.coord, alpha.hull)
    # ii <- extract(non.detection, non.hull.cells, cellnumbers=TRUE)[,"cells"]
    # non.detection[ii] <- NA
    ###########################################################################
    
    writeOGR(obj = nn.points, dsn = './PresenceAbsences', layer = paste0(sci.name.abbrv,"_points"), driver = "ESRI Shapefile", overwrite_layer = TRUE)
    
    suppressWarnings(nn <- nnInterpolate(nn.points, habitat.refine)) #PROJ6 issue
    
    writeRaster(nn, filename = paste0("NN/",sci.name.abbrv,"_NN.tif"), format = "GTiff", overwrite = TRUE)
    
    final.range<- mask(habitat.refine, nn)
    cell.size <- area(final.range, na.rm = TRUE)
    report.table[i,"AOH"] <- sum(cell.size[!is.na(cell.size)])
    report.table[i,"PAOH"] <- report.table[i,"TotalAOH"] - report.table[i,"AOH"]
    writeRaster(final.range, filename = paste0("FinalRange/",sci.name.abbrv,".tif"), format = "GTiff", overwrite = TRUE)
    
    if(length(spp.bl)>0){
      report.table[i,"IUCNArea"] <- area(spp.bl)/1000000
      IUCN.TAOH <- mask(habitat.refine, spp.bl)
      cell.size <- area(IUCN.TAOH, na.rm = TRUE)
      report.table[i,"IUCN.TAOH"] <- sum(cell.size[!is.na(cell.size)])
      report.table[i,"IUCN.TAOH.Per"] <- report.table[i,"IUCN.TAOH"]/report.table[i,"TotalAOH"]*100
      IUCN.AOH <- mask(final.range, spp.bl)
      cell.size <- area(IUCN.AOH, na.rm = TRUE)
      report.table[i,"IUCN.AOH"] <- sum(cell.size[!is.na(cell.size)])
      report.table[i,"IUCN.AOH.Per"] <- report.table[i,"IUCN.AOH"]/report.table[i,"AOH"]*100
      report.table[i,"IUCN.PAOH"] <- report.table[i,"IUCN.TAOH"] - report.table[i,"IUCN.AOH"]
      report.table[i,"IUCN.PAOH.Per"] <- report.table[i,"IUCN.PAOH"]/report.table[i,"PAOH"]*100
    }
    
    ###################################################VALIDATION########################################################
    
    if(validate){
      print("Running Validation...")
      valid.table[i,"SciName"] <- sci.name
      train.hull <- alphahull(points = species.train, 
                              polygon = spp.bl, 
                              #alpha = alpha, 
                              buffer = buffer)
      train.hull <- train.hull[[1]]
      train.habitat <- refineHabitat(forest, DEM, 
                                     presences = species.train, 
                                     hull = train.hull, bl.min = spp.elev$Min, bl.max = spp.elev$Max)
      valid.table[i,"ForestThresh"] <- train.habitat$ForestLimit
      valid.table[i,"LowerElev"] <- train.habitat$DEMLimit.Min
      valid.table[i,"UpperElev"] <- train.habitat$DEMLimit.Max
      train.habitat.refine <- train.habitat$HabitatRast
      cell.size <- area(train.habitat.refine, na.rm = TRUE)
      valid.table[i,"TotalAOH"] <- sum(cell.size[!is.na(cell.size)])
      valid.table[i,"TotalAOH.Change"] <- valid.table[i,"TotalAOH"] - report.table[i,"TotalAOH"]
      train.effort <- presAbs(checklists = checklists,
                          presences = species.train,
                          hull = train.hull,
                          habitat = train.habitat.refine,
                          distance = non.detect.size,
                          threshold = non.detect.thresh)
      train.nn.points <- train.effort$Points
      train.nondetect <- train.effort$NonDetection
      train.nn <- nnInterpolate(train.nn.points, train.habitat.refine)
      train.final<- mask(train.habitat.refine, train.nn)
      cell.size <- area(train.final, na.rm = TRUE)
      valid.table[i,"AOH"] <- sum(cell.size[!is.na(cell.size)])
      valid.table[i,"AOH.Change"] <-  valid.table[i,"AOH"] - report.table[i,"AOH"]
      valid.table[i,"PAOH"] <- valid.table[i,"TotalAOH"] - valid.table[i,"AOH"]
      valid.table[i,"PAOH.Change"] <- valid.table[i,"PAOH"] - report.table[i,"PAOH"]
      
      if(length(spp.bl)>0){
        valid.IUCN.TAOH <- mask(train.habitat.refine, spp.bl)
        cell.size <- area(valid.IUCN.TAOH, na.rm = TRUE)
        valid.table[i,"IUCN.TAOH"] <- sum(cell.size[!is.na(cell.size)])
        valid.table[i,"IUCN.TAOH.Change"] <- valid.table[i,"IUCN.TAOH"] - report.table[i,"IUCN.TAOH"]
        IUCN.AOH <- mask(final.range, spp.bl)
        cell.size <- area(IUCN.AOH, na.rm = TRUE)
        valid.table[i,"IUCN.AOH"] <- sum(cell.size[!is.na(cell.size)])
        valid.table[i,"IUCN.AOH.Change"] <- valid.table[i,"IUCN.AOH"] - report.table[i,"IUCN.AOH"]
        valid.table[i,"IUCN.PAOH"] <- valid.table[i,"IUCN.TAOH"] - valid.table[i,"IUCN.AOH"]
        valid.table[i,"IUCN.PAOH.Change"] <- valid.table[i,"IUCN.PAOH"] - report.table[i,"IUCN.PAOH"]
      }
      
      
      test.length <- length(species.test)
      valid.table[i,"Valid.Total"] <- test.length
      test.hull <- species.test[alpha.hull,]
      valid.table[i,"Valid.Miss.Num"] <- test.length - length(test.hull)
      valid.table[i,"Valid.Miss.Per"] <- valid.table[i,"Valid.Miss.Num"]/test.length*100
      test.hull@data$AOH <- raster::extract(train.final, test.hull)
      test.AOH <- test.hull %>%
        filter(test.hull@data$AOH>0)
      valid.table[i,"Valid.AOH.Num"] <- length(test.AOH)
      valid.table[i,"Valid.AOH.Per"] <- valid.table[i,"Valid.AOH.Num"]/test.length*100
      test.no.AOH <- test.hull %>%
        filter(is.na(test.hull@data$AOH))
      test.no.AOH@data$PAOH <- raster::extract(habitat.refine,test.no.AOH)
      test.PAOH <- test.no.AOH %>%
        filter(test.no.AOH@data$PAOH>0)
      valid.table[i,"Valid.PAOH.Num"] <- length(test.PAOH)
      valid.table[i,"Valid.PAOH.Per"] <- valid.table[i,"Valid.PAOH.Num"]/test.length*100
      valid.table[i,"Valid.Hull.Num"] <- length(test.no.AOH)-length(test.PAOH)
      valid.table[i,"Valid.Hull.Per"] <- valid.table[i,"Valid.Hull.Num"]/test.length*100
    }
    
    ########################################################################################################
    ########################################MAPPING#########################################################
    ########################################################################################################
    print("Mapping Results...")
    
    presences <- subset(nn.points, nn.points@data$Presence == 1)
    
    suppressWarnings(range_map <- leaflet() %>%
      addProviderTiles(providers$Esri.WorldTopoMap) %>%
      addRasterImage(habitat.refine, colors = hab.refine.col, opacity = 0.7, group = "Full Map") %>%
      addRasterImage(final.range, colors = hab.final.col, opacity = 1, group = "Full Map") %>%
      addPolygons(data = alpha.hull, stroke = TRUE, color = alpha.col, opacity = 1, weight = 3, fillOpacity = 0) %>%
      addLayersControl(overlayGroups = c("BirdLife Range","eBird Presences","Non-Detection"),
                       options = layersControlOptions(collapsed = FALSE)) %>%
      addMiniMap(
        tiles = providers$Esri.WorldTopoMap,
        width = 150,
        height = 150) %>%
      addLegend("topright", 
                colors = leg.col, 
                labels = values, 
                opacity = 1, 
                title = paste(sci.name, "<br> Alpha =",floor(alpha/1000))) %>%
      addScaleBar(options = scaleBarOptions(metric = TRUE, imperial = FALSE)))
    
    if(length(spp.bl)>0){
      range_map <- range_map %>%
        addPolygons(data = spp.bl, color = iucn.col, opacity = 1, weight = 4, fillOpacity = 0, group = "BirdLife Range")
    }
    
    if(sum(!is.na(non.detection@data@values))>0){
      non.detect.poly <- rasterToPolygons(non.detection)
      non.detect.labs <- non.detect.poly@data$layer
      
      non.detect.color <- colorNumeric(
        palette = "YlOrRd",
        domain = non.detect.poly$layer)
      
      range_map <- range_map %>%
        addPolygons(data = non.detect.poly,
                    fillColor = ~non.detect.color(layer),
                    color = ~non.detect.color(layer),
                    opacity = 1,
                    weight = 1,
                    fillOpacity = 0.75,
                    popup = ~paste("<b>Absences: </b>",layer,"<br>"),
                    group = "Non-Detection") %>%
        addLegend("bottomleft", pal = non.detect.color, values = non.detect.poly$layer,
                  title = "Number of Absences",
                  opacity = 1)
    }
    
    if(keep.gbif){
      if(nrow(gbif)>0){
        range_map <- range_map %>%
          addCircleMarkers(data = gbif,
                           radius = 4,
                           fillColor = "#FF00FF",
                           fillOpacity = 1,
                           stroke = TRUE,
                           opacity = 1,
                           weight = 1,
                           color = "#4d004d",
                           popup = ~paste("<b>Type of Record: </b>",basisOfRecord,"<br>",
                                          "<b>Date: </b>",date,"<br>",
                                          "<b>GBIF ID: </b>",gbifID),
                           group = "GBIF Records")
      }
    }
    
    #if(class(ebd_hi)=="SpatialPointsDataFrame"){ ###################WHY??????#################
    if(keep.hi){
      range_map <- range_map %>%
        addCircleMarkers(data = ebd_hi,
                         radius = 4,
                         fillColor = "#414141",
                         fillOpacity = 1,
                         stroke = TRUE,
                         opacity = 0.5,
                         weight = 1,
                         color = "#000000",
                         popup = ~paste("<b>Protocol: </b>",protocol_type,"<br>",
                                        "<b>Date: </b>",observation_date,"<br>",
                                        "<b>Checklist: </b>","<a href='",url,"' target='_blank'>",checklist_id,"</a>"),
                         group = "Historical/Incidental")
    }
    
    range_map <- range_map %>%
      addCircleMarkers(data = species,
                       radius = 4,
                       fillColor = "#a9eb75",
                       fillOpacity = 1,
                       stroke = TRUE,
                       opacity = 1,
                       weight = 1,
                       popup = ~paste("<b>Protocol: </b>", protocol_type, "<br>",
                                      "<b>Date: </b>", observation_date, "<br>",
                                      "<b>Elevation (m): </b>", elevation, "<br>",
                                      "<b>Forest Cover (%): </b>", forest_cover, "<br>",
                                      "<b>Locality: </b>", locality, "<br>",
                                      "<b>Checklist: </b>","<a href='",url,"' target='_blank'>",checklist_id,"</a>"),
                       color = "#4d7e29",
                       group = "eBird Presences")
    if(validate){
      range_map <- range_map %>%
        addRasterImage(train.habitat.refine, colors = hab.refine.col, opacity = 0.7, group = "Training Map") %>%
        addRasterImage(train.final, colors = hab.final.col, opacity = 1, group = "Training Map") %>%
        addCircleMarkers(data = species.train,
                         radius = 4,
                         fillColor = "#C60404",
                         fillOpacity = 1,
                         stroke = TRUE,
                         opacity = 1,
                         weight = 1,
                         popup = ~paste("<b>Protocol: </b>",protocol_type,"<br>",
                                        "<b>Date: </b>",observation_date,"<br>",
                                        "<b>Checklist: </b>","<a href='",url,"' target='_blank'>",checklist_id,"</a>"),
                         color = "#7E191B",
                         group = "Validation Points") %>%
        addCircleMarkers(data = species.test,
                         radius = 4,
                         fillColor = "#0066cc",
                         fillOpacity = 1,
                         stroke = TRUE,
                         opacity = 1,
                         weight = 1,
                         popup = ~paste("<b>Protocol: </b>",protocol_type,"<br>",
                                        "<b>Date: </b>",observation_date,"<br>",
                                        "<b>Checklist: </b>","<a href='",url,"' target='_blank'>",checklist_id,"</a>"),
                         color = "#002952",
                         group = "Validation Points") %>%
        addLayersControl(
          baseGroups = c("Full Map", "Training Map"),
          overlayGroups = c("BirdLife Range","eBird Presences","Non-Detection","Historical/Incidental", "GBIF Records","Validation Points"),
          options = layersControlOptions(collapsed = FALSE))
    }
    
    range_map
    
    mapshot(range_map, file= paste0("Maps/",sci.name.abbrv,"_",floor(alpha/1000),".png"), remove_url = TRUE, remove_controls = TRUE)
    mapshot(range_map, url= paste0("Maps/",sci.name.abbrv,"_",floor(alpha/1000),".html"))
    
    
    end.time <- Sys.time()
    report.table[i,"Time"] <- end.time - start.time
    
    unlink(file.path("./Scratch/",sci.name.abbrv), recursive = TRUE)
    
  }, error = function(e){
    conditionMessage(e)
  })
  if(is.null(has.error)|has.error==0){
    next
  } else{
    report.table[i,"Errors"] <- has.error
    pushover(paste(sci.name,as.character(has.error)))
    has.error<-NULL
  }
}

write.csv(report.table, "Report Table_10_5.csv")
write.csv(valid.table, "Validation Table_9_21.csv")
