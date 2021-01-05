# This script aims at run raster claculator times to 
#produce DEMFC30_DeJure_+scientific_name+".tif"

#PA means De-jure in this script
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
DeJure_roi= "C:\\859K_sl559\\Data\Dejure_PA\\Classified_Dejure_PA_2020Dec16.tif"

fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    outRas = Raster(fileName)*Raster(DeJure_roi)
    outRas.save("DEMFC30_DeJure_"+scientific_name+".tif")
    print(outRas)
    