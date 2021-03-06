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
reC1_RegionG2_TC2000_Proj_tif = "reC1_RegionG2_TC2000_Proj.tif"
EucDist_reC_RegionG2_TC2000_Proj_tif = "C:\\859K_sl559\\Scratch3\\EucDist_reC_RegionG2_TC2000_Proj.tif"
Output_direction_raster = ""

# Process: Euclidean Distance
arcpy.gp.EucDistance_sa(reC1_RegionG2_TC2000_Proj_tif, EucDist_reC_RegionG2_TC2000_Proj_tif, "", "94.1231502405956", Output_direction_raster)

