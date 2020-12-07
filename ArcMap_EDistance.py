# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ArcMap_EDistance.py
# Created on: 2020-12-07 13:07:52.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
RegionG_Ani_tif = "RegionG_Ani.tif"
EucDist_RegionG_raw_Ani_tif = "C:\\859K_sl559\\Scratch3\\EucDist_RegionG_raw_Ani.tif"
Output_direction_raster = ""

# Process: Euclidean Distance
arcpy.gp.EucDistance_sa(RegionG_Ani_tif, EucDist_RegionG_raw_Ani_tif, "", "94.1231502405956", Output_direction_raster)

