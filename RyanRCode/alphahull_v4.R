alphahull <- function(points, polygon = NULL, buffer,
                      crs1 = CRS("+proj=aea +lat_1=-5 +lat_2=-42 +lat_0=-32 +lon_0=-60 +x_0=0 +y_0=0 +ellps=aust_SA +datum=WGS84 +units=m +no_defs"), 
                      crs2 = CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")){
  require(sf)
  require(alphahull)
  require(SpatialPosition)
  
  print("Generating Alpha Hull...")
  
  presences <- spTransform(points, crs1)
  hull.coords <- presences@coords
  
  pair.dist<-pointDistance(hull.coords, lonlat = FALSE, allpairs = TRUE)
  diag(pair.dist)<-NA
  #pair.dist<- pair.dist[-1,]
  alpha = median(pair.dist, na.rm=T)
  
  
  if(!is.null(polygon) & length(polygon)>0){
    poly.p <- spTransform(polygon, crs1)
    poly.p <- as_Spatial(st_segmentize(st_as_sf(poly.p), units::set_units((alpha/5), m)))

    for (k in 1:length(poly.p@polygons[[1]]@Polygons)){
      poly.coords <- poly.p@polygons[[1]]@Polygons[[k]]@coords
      colnames(poly.coords) <- colnames(hull.coords)
      hull.coords <- rbind(hull.coords, poly.coords)
    }
    
    if(is.na(alpha)){
      pair.dist<-pointDistance(hull.coords, lonlat = FALSE, allpairs = TRUE)
      diag(pair.dist)<-NA
      #pair.dist<- pair.dist[-1,]
      alpha = median(pair.dist, na.rm=T)
    }
    
    fill.points <- CreateGrid(poly.p, (alpha/2))
    fill.points <- fill.points[poly.p,]
    hull.coords <- rbind(hull.coords, fill.points@coords)
  }
  
  hull.coords <- hull.coords[!duplicated(hull.coords),]
  
  a.hull<-ahull(x = hull.coords[,1], y = hull.coords[,2], alpha = alpha)
  ah.lines <- ahull2lines(a.hull)
  ah.poly <- spLines2poly(ah.lines)
  proj4string(ah.poly) <- crs1
  alpha.hull <- gBuffer(ah.poly, width = buffer)
  alpha.hull <- spTransform(alpha.hull, crs2)
  return(list(alpha.hull, alpha))
}