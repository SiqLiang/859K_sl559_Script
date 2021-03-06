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
arcpy.env.workspace = "C:\\859K_sl559\\Data\\ForestCover2000"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
cellSize = 0.0008333


# Local variables:
Hansen_GFC_2019_v1_7_treecover2000_40N_100E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_40N_100E (1).tif"
Hansen_GFC_2019_v1_7_treecover2000_40N_090E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_40N_090E (1).tif"
Hansen_GFC_2019_v1_7_treecover2000_40N_080E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_40N_080E (1).tif"
Hansen_GFC_2019_v1_7_treecover2000_30N_100E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_30N_100E (1).tif"
Hansen_GFC_2019_v1_7_treecover2000_30N_090E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_30N_090E (1).tif"
Hansen_GFC_2019_v1_7_treecover2000_30N_080E__1__tif = "Hansen_GFC-2019-v1.7_treecover2000_30N_080E (1).tif"
ForestCover2000 = "C:\\859K_sl559\\Data\\ForestCover2000"
SixForestCover2000_MosaictoNewRater_tif = "C:\\859K_sl559\\Data\\ForestCover2000\\SixForestCover2000_MosaictoNewRater.tif"

# Process: Mosaic To New Raster
arcpy.MosaicToNewRaster_management("'Hansen_GFC-2019-v1.7_treecover2000_40N_100E (1).tif';'Hansen_GFC-2019-v1.7_treecover2000_40N_090E (1).tif';'Hansen_GFC-2019-v1.7_treecover2000_40N_080E (1).tif';'Hansen_GFC-2019-v1.7_treecover2000_30N_100E (1).tif';'Hansen_GFC-2019-v1.7_treecover2000_30N_090E (1).tif';'Hansen_GFC-2019-v1.7_treecover2000_30N_080E (1).tif'", ForestCover2000, "SixForestCover2000_MosaictoNewRater.tif", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "8_BIT_UNSIGNED", "", "1", "MAXIMUM", "FIRST")

