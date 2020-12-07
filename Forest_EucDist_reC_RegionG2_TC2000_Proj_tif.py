#Because the Edistance Map was based on the area with no forest, The area with no forest was conted 
#distance too. I use the forest map (reC2_RegionG2_TC2000_Proj_tif) to mask out the forest area with EDistance

import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

# Local variables:
EucDist_reC_RegionG2_TC2000_Proj_tif = "C:\\859K_sl559\\Scratch3\\EucDist_reC_RegionG2_TC2000_Proj.tif"
reC2_RegionG2_TC2000_Proj_tif= "C:\\859K_sl559\\Scratch3\\reC2_RegionG2_TC2000_Proj.tif"

# Maskout the forest area from the Edistance Map
outRas = Raster(EucDist_reC_RegionG2_TC2000_Proj_tif)*Raster(reC2_RegionG2_TC2000_Proj_tif)
outRas.save("C:\\859K_sl559\\Scratch3\\Forest_EucDist_reC_RegionG2_TC2000_Proj_tif")
