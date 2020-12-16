# This script aims at run raster claculator times to 
#produce DEMFC30_PA_+scientific_name+".tif"

#PA means De-jure in this script
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
DeFacto_roi= "C:\859K_sl559\Data\Defacto_PA\DeFacto_EucDist_reC_RegionG2_TC2000_Proj.tif"

       
sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[13:fileName.rfind('.')]
    outRas = Raster(fileName)*Raster(DeFacto_roi)
    outRas.save("DEMFC30_DeFacto_"+scientific_name+".tif")
    print(outRas)
    