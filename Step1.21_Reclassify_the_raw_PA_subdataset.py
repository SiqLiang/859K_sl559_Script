import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\Dejure_PA\\Dejure_PA_RawTif"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

fileList = arcpy.ListRasters('raw_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    subdataset_name = fileName[4:fileName.rfind('.')]
    outRas = Raster(fileName)*Raster(PA_roi)
    outRas.save("Classified_"+subdataset_name+".tif")
    print(outRas)
