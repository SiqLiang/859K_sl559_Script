# This script aims at run raster claculator times to 
#produce DEMFC30_PA_+scientific_name+".tif"
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

PA_roi= "C:\\859K_sl559\\Data\\SumPA_rC.tif"
       
sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    outRas = Raster(fileName)*Raster(PA_roi)
    outRas.save("DEMFC30_PA_"+scientific_name+".tif")