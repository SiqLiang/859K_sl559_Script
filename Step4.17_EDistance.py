# ---------------------------------------------------------------------------
# ArcMap_EDistance.py
# Created on: 2020-12-07 13:18:47.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
# Local variables:
ReC2_RegionG2_TC2000_Proj_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\ReC2_Proj_RegionG2_ReC1_RegionG1_FC2000_ROIexpanded_300m.tif"
EucDist_reC_RegionG2_TC2000_Proj_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\EucDist_ReC2_Proj_RegionG2_ReC1_RegionG1_FC2000_ROIexpanded_300m.tif"

#I conducted this step in Arcmap pro