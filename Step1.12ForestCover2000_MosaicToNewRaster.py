# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ArcMap_MosaicToNewRaster.py
# Created on: 2020-12-11 20:53:48.00000
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy.sa import *
# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch_DistanceToEdge\\ForestCover_2000"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
cellSize =0.00277777777777778#300m as in ESA LC2000 #0.000833333333333333 #90m


# Local variables:
Treecover2000_20N_070E_tif = "Hansen_GFC2015_treecover2000_20N_070E.tif"
Treecover2000_20N_080E_tif = "Hansen_GFC2015_treecover2000_20N_080E.tif"
Treecover2000_20N_090E_tif = "Hansen_GFC2015_treecover2000_20N_090E.tif"
Treecover2000_20N_100E_tif = "Hansen_GFC2015_treecover2000_20N_100E.tif"
Treecover2000_20N_110E_tif = "Hansen_GFC2015_treecover2000_20N_110E.tif"


Treecover2000_30N_070E_tif = "Hansen_GFC2015_treecover2000_20N_070E.tif"
Treecover2000_30N_080E_tif = "Hansen_GFC2015_treecover2000_20N_080E.tif"
Treecover2000_30N_090E_tif = "Hansen_GFC2015_treecover2000_20N_090E.tif"
Treecover2000_30N_100E_tif = "Hansen_GFC2015_treecover2000_20N_100E.tif"
Treecover2000_30N_110E_tif = "Hansen_GFC2015_treecover2000_20N_110E.tif"


Treecover2000_40N_070E_tif = "Hansen_GFC2015_treecover2000_40N_070E.tif"
Treecover2000_40N_080E_tif = "Hansen_GFC2015_treecover2000_40N_080E.tif"
Treecover2000_40N_090E_tif = "Hansen_GFC2015_treecover2000_40N_090E.tif"
Treecover2000_40N_100E_tif = "Hansen_GFC2015_treecover2000_40N_100E.tif"
Treecover2000_40N_110E_tif = "Hansen_GFC2015_treecover2000_40N_110E.tif"



Scratch_DistanceToEdge = "C:\\859K_sl559\\Scratch_DistanceToEdge"
ForestCover2000_MosaictoNewRater_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\ForestCover2000_MosaictoNewRater_ROIexpanded_300m.tif"

# Process: Mosaic To New Raster
arcpy.MosaicToNewRaster_management("'Hansen_GFC2015_treecover2000_20N_070E.tif';'Hansen_GFC2015_treecover2000_20N_080E.tif';'Hansen_GFC2015_treecover2000_20N_090E.tif';'Hansen_GFC2015_treecover2000_20N_100E.tif';'Hansen_GFC2015_treecover2000_20N_110E.tif';'Hansen_GFC2015_treecover2000_30N_070E.tif';'Hansen_GFC2015_treecover2000_30N_080E.tif';'Hansen_GFC2015_treecover2000_30N_090E.tif';'Hansen_GFC2015_treecover2000_30N_100E.tif';'Hansen_GFC2015_treecover2000_30N_110E.tif';'Hansen_GFC2015_treecover2000_40N_070E.tif';'Hansen_GFC2015_treecover2000_40N_080E.tif';'Hansen_GFC2015_treecover2000_40N_090E.tif';'Hansen_GFC2015_treecover2000_40N_100E.tif';'Hansen_GFC2015_treecover2000_40N_110E.tif';", 
                                   Scratch_DistanceToEdge, "ForestCover2000_MosaictoNewRater_ROIexpanded_300m.tif", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "8_BIT_UNSIGNED", "", "1", "MAXIMUM", "FIRST")

#run successfully, however the output cellsize is still 0.00025 instead of the mentioned 0.0008333