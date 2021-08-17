presAbs <- function(checklists, presences, hull, habitat, distance, threshold,
                    crs1 = CRS("+proj=aea +lat_1=-5 +lat_2=-42 +lat_0=-32 +lon_0=-60 +x_0=0 +y_0=0 +ellps=aust_SA +datum=WGS84 +units=m +no_defs"), 
                    crs2 = CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")){
  checklists <- checklists[hull,]
  hab.refine.proj <- projectRaster(habitat, crs = crs1)
  checklists@data$habitat <- raster::extract(habitat, checklists, buffer = mean(res(hab.refine.proj)))
  checklists@data$habitat <- unlist(lapply(checklists@data$habitat, function(x) sum(!is.na(x))))
  checklists <- checklists %>%
    filter(checklists@data$habitat>0)
  
  effort <- raster(extent(habitat))
  res(effort) = res(habitat)*distance
  crs(effort) <- crs(habitat)
  
  tab <- table(cellFromXY(effort, checklists))
  effort[as.numeric(names(tab))] <- tab
  effort[effort < threshold] <- NA #############Checklist Threshold Amount
  
  pres.abs.rast <- effort
  ii <- extract(pres.abs.rast, presences, cellnumbers=TRUE)[,"cells"]
  pres.abs.rast[ii] <- NA
  non.detection <- pres.abs.rast
  abs.cells <- extract(pres.abs.rast, checklists, cellnumbers=TRUE)
  ii <- subset(abs.cells, !is.na(abs.cells[,"layer"]))[,"cells"]
  pres.abs.rast[ii] <- 0
  
  pres.abs <- data.frame(coordinates(pres.abs.rast), Presence=pres.abs.rast[])
  pres.abs <- pres.abs[!is.na(pres.abs$Presence), ]
  if(length(pres.abs$Presence)>0){
    coordinates(pres.abs) <- c("x", "y")
    proj4string(pres.abs) <- proj4string(habitat)
    nn.points <- matrix(
      c(pres.abs@coords[,1], species@coords[,1],
        pres.abs@coords[,2], species@coords[,2],
        rep(0, length(pres.abs@coords[,1])),rep(1, length(species@coords[,1]))),
      ncol = 3)
    nn.points<- nn.points[!duplicated(nn.points[,1:2], fromLast = TRUE),] #Remove potential absence duplicates
  }else {
    nn.points <- matrix(
      c(species@coords[,1],
        species@coords[,2],
        rep(1, length(species@coords[,1]))),
      ncol = 3)
  }
  
  colnames(nn.points) <- c("Long", "Lat","Presence")
  nn.points <- data.frame(nn.points)
  coordinates(nn.points) <- c("Long", "Lat")
  proj4string(nn.points) <- crs2
  #nn.points <- nn.points[hull,]
  
  Effort <- list("Points" = nn.points, "NonDetection" = non.detection)
  
  return(Effort)
}