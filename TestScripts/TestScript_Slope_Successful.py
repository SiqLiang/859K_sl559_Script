import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:\\859K_sl559\\Data"
outRas = Slope("Area_mask_DEM90m_final.tif")
outRas.save("C:\\859K_sl559\\Data\\SlopeTest1.tif")
