import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\Dejure_PA\\Dejure_PA_RawTifClassified"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")


sumRas = 0 # set init value and then loop through file list
fileList = arcpy.ListRasters('Classified_*')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    sumRas = arcpy.Raster(fileName) + sumRas
sumRas.save('C:\\859K_sl559\\Data\Dejure_PA\\Dejure_PA_2020Dec16.tif')
#Dejure_PA_2020Dec16 is made of WDPA_shp012, China loal, China NNA

reclassField = "Value"
remap = "1 5 1; 0 0"
inRas= 'C:\\859K_sl559\\Data\Dejure_PA\\Dejure_PA_2020Dec16.tif'
outRas= "C:\\859K_sl559\\Data\Dejure_PA\\Classified_Dejure_PA_2020Dec16.tif"
arcpy.gp.Reclassify_sa(inRas, reclassField, remap, outRas)

