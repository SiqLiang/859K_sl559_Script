import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\TropicalAndes\\Scratch1"
arcpy.env.extent = "C:\\TropicalAndes\\Data\\Hotspot_TropicalAndes.shp"

#input datasets
inputShapefile = "‪C:\\TropicalAndes\\Data\\BirdsEndemicTo_TropicalAndes.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
#Try later: 54012 is the WKID of World Eckert IV
#Try later: outputSR = arcpy.SpatialReference(54002)
#Try later: arcpy.CreateFeatureclass_management(outPath,outName,"POINT","","","",outputSR)

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(inputShapefile,['FID', "Scientific"]) 
row = rows.next()

for i in range (0,122,1):
    fid = row[0]
    scientific_name=row[1]
    print(row)
    
    
    #multishapefile to single shapfiles 
    arcpy.AddMessage("Producing {} indivial shapfile".format(row[1]))
    poly_out = "Sp_"+scientific_name+".shp"
    arcpy.Select_analysis(inputShapefile,poly_out,"\"FID\"= %i"%i) 
    
    #Execute BL_Map Feature to Raster
    arcpy.AddMessage("Producing {} raw raster".format(row[1]))
    BLraw = "BLraw_"+scientific_name+".tif"
    cellSize = 0.000833333333333333
    field = "id_no"
    arcpy.FeatureToRaster_conversion(poly_out, field, BLraw, cellSize)
    
    #Execute Reclassify BL_Map
    arcpy.AddMessage("Reclassifying {} raw raster".format(row[1]))
    reclassField = "Value"
    remap = "0 0; 1 100000000000 1; NODATA 0"
    BL_Map= "BL_Map_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(BLraw, reclassField, remap, BL_Map)
    row = rows.next()
del rows     

#fileList = arcpy.ListRasters('BL_Map_*', 'All')
#len(fileList)

#fileList = arcpy.ListRasters('ReBy_DEM_*', 'All')
#len(fileList)

#fileList = arcpy.ListRasters('ReBy_FC30_*', 'All')
#len(fileList)

fileList = arcpy.ListRasters('BL_Map_*', 'All')
len(fileList)





