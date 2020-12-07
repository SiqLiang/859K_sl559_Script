import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

# Local variables:
RegionG2_rCRGrCndTC2000_Proj_tif= "C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000_Proj.tif"
reC_RegionG2_TC2000_Proj_tif= "C:\\859K_sl559\\Scratch3\\reC_RegionG2_TC2000_Proj.tif"
#Execute Reclassify 
reclassField = "Count"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha
remap = "113 63623690 NODATA; NODATA 1"
arcpy.gp.Reclassify_sa(RegionG2_rCRGrCndTC2000_Proj_tif, reclassField, remap, reC_RegionG2_TC2000_Proj_tif)
