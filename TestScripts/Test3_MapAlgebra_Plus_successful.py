import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:\\859K_sl559\\Data"
outRas = Raster("WCountriesG_B50_rC.tif") + Raster("SumPA_rC.tif")
outRas.save("Test3_MapAlgebra_Plus.tif")

