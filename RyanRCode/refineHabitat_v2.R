refineHabitat <- function(forest, DEM, presences, hull, bl.min= NULL, bl.max = NULL){
  
  require(tmaptools)
  
  print("Refining Forest Cover...")
  
  presences@data$forest_cover <- raster::extract(forest, presences)
  sp_forest <- presences@data %>% filter(year>1999) %>% select(forest_cover)
  sp_forest <- sp_forest[!is.na(sp_forest)]
  sp_forest <- sp_forest[sp_forest>0]
  threshold <- unname(quantile(sp_forest, probs = 0.25))
  forest.rcl <- matrix(
    c(0, threshold, threshold, 100,NA, 1),
    nrow = 2, ncol = 3)
  forest.poly <- raster::mask(forest, hull)
  forest.poly <- crop(x = forest.poly, y = extent(hull))
  forest.range <- reclassify(forest.poly, forest.rcl, right = FALSE)
  
  print("Refining Elevation...")
  
  presences@data$elevation <- raster::extract(DEM, presences)
  sp_DEM <- presences@data$elevation[!is.na(presences@data$elevation)]
  DEM.limits <- unname(quantile(sp_DEM, probs = c(.01,.99)))
  if(!is.null(bl.min) & !is.null(bl.max)){
    DEM.min <- min(c(DEM.limits[1], bl.min))
    DEM.max <- max(c(DEM.limits[2], bl.max))
  }else{
    DEM.min <- DEM.limits[1]
    DEM.max <- DEM.limits[2]
  }
  
  DEM.rcl <- matrix(
    c(DEM@data@min, DEM.min, DEM.max, DEM.min, DEM.max, DEM@data@max, NA, 1, NA),
    nrow = 3, ncol = 3)
  DEM.poly <- mask(DEM, hull)
  DEM.poly <- crop(x = DEM.poly, y = extent(hull))
  DEM.range <- reclassify(DEM.poly, DEM.rcl, right = FALSE)
  
  if(extent(DEM.range) != extent(forest.range)){
    extent(DEM.range) <- extent(forest.range)
    DEM.range <- resample(DEM.range, forest.range)
  }

  habitat.refine <- mask(forest.range, DEM.range)

  
  refined.habitat <- list("Presences" = presences,
                          "ForestLimit" = threshold,
                          "ForestRast" = forest.range,
                          "DEMLimit.Min" = DEM.min,
                          "DEMLimit.Max" = DEM.max,
                          "DEMRast" = DEM.range,
                          "HabitatRast" = habitat.refine)
  return(refined.habitat)
}