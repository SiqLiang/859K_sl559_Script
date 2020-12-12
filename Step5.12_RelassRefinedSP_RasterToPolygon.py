import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch4"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
#
fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    outRas= "RcReBy_DEMFC30_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(fileName, "VALUE", 
                       "0 NODATA;1 1;NODATA NODATA", 
                       outRas, "DATA")
    print(outRas)
    outShp="DEMFC30_"+scientific_name+".shp"
    arcpy.RasterToPolygon_conversion(outRas, outShp, "NO_SIMPLIFY", "Value")
    print(outShp)

    
