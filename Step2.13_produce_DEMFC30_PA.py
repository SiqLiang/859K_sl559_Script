# This script aims at run raster claculator times to 
#produce DEMFC30_PA_+scientific_name+".tif"
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\859K_sl559\Data\Dejure_PA\Dejure_PA_RawTif"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

PA_roi= "C:\\859K_sl559\\Data\\SumPA_rC.tif"
       
sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    reclassField = "Value"
    remap = "1 1; NODATA 0"
    outRas= "DEMFC30_PA_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(fileName, reclassField, remap, outRas)
    print(outRas)


