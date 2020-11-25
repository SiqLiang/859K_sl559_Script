import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\ScratchV1"
arcpy.env.extent = arcpy.GetParameterAsText(0)

# Specify the feature class to examine
inputShapefile = arcpy.GetParameterAsText(1)

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(inputShapefile,['FID','83LandBi_5']) #Field names shall be changed according to the input shapefile
row = rows.next()
for i in range (0,83,1):
    fid = row[0]
    scientific_name = row[1]
    
    #multishapefile to single shapfiles
    arcpy.AddMessage("Producing {} indivial shapfile".format(row[1]))
    poly_out = "Sp_"+scientific_name+".shp"
    arcpy.Select_analysis(inputShapefile,poly_out,"\"FID\"= %i"%i) 
    
    #Execute Feature to Raster
    arcpy.AddMessage("Producing {} raw raster".format(row[1]))
    RawRaster_out = "RawRaster_"+scientific_name+".tif"
    cellSize = 0.0008333
    field = "83LandBird"
    arcpy.FeatureToRaster_conversion(poly_out, field, RawRaster_out, cellSize)
    
    #Execute Reclassify
    arcpy.AddMessage("Reclassifying {} raw raster".format(row[1]))
    reclassField = "Value"
    remap = "0 0; 1 100000000000 1; NODATA 0"
    Reclass_out= "ReClassRaster_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(RawRaster_out, reclassField, remap, Reclass_out)
    
    row = rows.next()
del rows

# Sum up all the classified rasters into the final output--Bird Species Richness map          
sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('ReClassRaster*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    arcpy.AddMessage("Processing {} to produce bird species richness map".format(fileName))
    sumRas = arcpy.Raster(fileName) + sumRas
sumRas.save('C:\\859K_sl559\\Scratch\\BirdSpeciesRichnessMap.tif')
arcpy.AddMessage("BirdSpeciesRichnessMap is avaiable at Scratch now" )














