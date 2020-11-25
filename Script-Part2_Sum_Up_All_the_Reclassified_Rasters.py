import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

# Sum up all the classified rasters into the final output--Bird Species Richness map          
sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('ReClassRaster*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    arcpy.AddMessage("Processing {} to produce bird species richness map".format(fileName))
    sumRas = arcpy.Raster(fileName) + sumRas
sumRas.save('C:\\859K_sl559\\Scratch\\BirdSpeciesRichnessMap.tif')
arcpy.AddMessage("BirdSpeciesRichnessMap is avaiable at Scratch now" )


