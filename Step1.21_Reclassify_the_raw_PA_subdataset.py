import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\Dejure_PA\\Dejure_PA_RawTif"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

fileList = arcpy.ListRasters('raw_*')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    subdataset_name = fileName[4:fileName.rfind('.')]
    reclassField = "Value"
    remap = "1 1; NODATA 0"
    outRas= "Classified_"+subdataset_name+".tif"
    arcpy.gp.Reclassify_sa(fileName, reclassField, remap, outRas)
    print(outRas)

#the outputs were transported to C:\859K_sl559\Data\Dejure_PA\Dejure_PA_RawTifClassified