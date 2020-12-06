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
remap = "1 112 NODATA; NODATA NODATA"
BL_Map= "BL_Map_"+scientific_name+".tif"
arcpy.gp.Reclassify_sa(RegionG_rCNoDataTC2000_test2_tif, reclassField, remap, Reclass_RegionG_rCNTC2000_tif)