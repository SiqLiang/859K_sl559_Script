# This script aims at run raster claculator times to 
#produce DEMFC30_DeFacto1000m_+scientific_name+".tif"

import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
DeFacto1000m_roi= "C:\\859K_sl559\\Data\\SumUp_Dejure_Defacto\\Reclass_DeFacto_1000m.tif"

fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    outRas = Raster(fileName)*Raster(DeFacto1000m_roi)
    outRas.save("DEMFC30_DeFacto1000m_"+scientific_name+".tif")
    print(outRas)
    
    