# The patch with cellsize smaller than 113 i.e. 100 hacter were reclassified into NoData in arcgis pro
import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

RegionG_rCNoDataTC2000_test2_tif = "C:\\859K_sl559\\Scratch3\\RegionG_rCNoDataTC2000_test2.tif"
Reclass_RegionG_rCNTC2000_tif = "C:\\859K_sl559\\Scratch3\\Reclass_RegionG_rCNTC2000.tif"

#Execute Reclassify 
reclassField = "Count"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha
remap = "1 112 NODATA; NODATA NODATA"
arcpy.gp.Reclassify_sa(RegionG_rCNoDataTC2000_test2_tif, reclassField, remap, Reclass_RegionG_rCNTC2000_tif)