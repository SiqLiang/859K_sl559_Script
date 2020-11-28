import arcpy
from arcpy.sa import *

arcpy.env.workspace = "C:\\859K_sl559\\Scratch"
arcpy.env.overwriteOutput = True

ReClassRasters = arcpy.ListRasters("ReClassRaster_*")
len(ReClassRasters)

#scientific_name = ReClassRasters[1][14:sp1.rfind('.')]
#outRas= "ReBy_FC30_"+scientific_name+".tif"
#print(outRas)

for ReClassRaster in ReClassRasters:
    outRas = Raster(ReClassRaster)*Raster("H_TC2000_ReC.tif")
    scientific_name = ReClassRaster[14:ReClassRaster.rfind('.')]
    outRas.save("ReBy_FC30_"+scientific_name+".tif")
    print(ReClassRaster)
    print(outRas)


#Reclass_out= "ReClassRaster_"+scientific_name+".tif"