# This script aims at run raster claculator times to 
#produce DEMFC30_PA_+scientific_name+".tif"

#PA means De-jure in this script
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
DeJure= "C:\\859K_sl559\\Data\\SumUp_Dejure_Defacto\\Classified_Dejure_PA_2020Dec16.tif"
# Classified_Sum_PA_2020Dec16.tif is made of WDPA_shp012, China loal, China NNA, and DeFacto
fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    outRas = Raster(fileName)*Raster(SumPA)
    outRas.save("DEMFC30_Dejure_"+scientific_name+".tif")
    print(outRas)
    