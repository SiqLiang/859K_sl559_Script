# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ArcMap_DEM_MosaicToNewRaster.py
# Created on: 2021-01-04 20:55:54.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\RawData\\DEM90m"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
#outputlocation and file name
DEM90m = "C:\\859K_sl559\\Data\\RawData\\DEM90m"
DEM90_Mosaic_2021Jan4 = "C:\\859K_sl559\\Data\\RawData\\DEM90m\\DEM90_Mosaic_2021Jan4.tif"


# Local variables:
utm_srtm_52_06_img = "utm_srtm_52_06.img"

utm_srtm_53_06_img = "utm_srtm_53_06.img"
utm_srtm_53_07_img = "utm_srtm_53_07.img"
utm_srtm_53_08.img = 'srtm_53_08.img'#####################

utm_srtm_54_06_img = "utm_srtm_54_06.img"
utm_srtm_54_07_img = "utm_srtm_54_07.img"
utm_srtm_54_08_img = "srtm_54_08.img"########################

utm_srtm_55_06_img = "utm_srtm_55_06.img"
utm_srtm_55_07_img = "utm_srtm_55_07.img"
utm_srtm_55_08_img = "srtm_55_08.img"##########

utm_srtm_56_06_img = "utm_srtm_56_06.img"
utm_srtm_56_07_img = "utm_srtm_56_07.img"
utm_srtm_56_08_img = "utm_srtm_56_08.img"

utm_srtm_57_06_img = "utm_srtm_57_06.img"
utm_srtm_57_07_img = "utm_srtm_57_07.img"
utm_srtm_57_08_img = "utm_srtm_57_08.img"

utm_srtm_58_06_img = "utm_srtm_58_06.img"
utm_srtm_58_07_img = "utm_srtm_58_07.img"
utm_srtm_58_08_img = "utm_srtm_58_08.img"
utm_srtm_58_09_img = "utm_srtm_58_09.img"

# Process: Mosaic To New Raster
arcpy.MosaicToNewRaster_management("
                                   utm_srtm_52_06_img;
                                   utm_srtm_53_06_img;
                                   utm_srtm_53_07_img;
                                   utm_srtm_53_08_img;
                                   utm_srtm_54_06_img;
                                   utm_srtm_54_07_img;
                                   utm_srtm_54_08_img;
                                   utm_srtm_55_06_img;
                                   utm_srtm_55_07_img;
                                   utm_srtm_55_08_img;
                                   utm_srtm_56_06_img;
                                   utm_srtm_56_07_img;
                                   utm_srtm_56_08_img;
                                   utm_srtm_57_06_img;
                                   utm_srtm_57_07_img;
                                   utm_srtm_57_08_img;
                                   utm_srtm_58_06_img;
                                   utm_srtm_58_07_img;
                                   utm_srtm_58_08_img;
                                   utm_srtm_59_08_img;
                                   ", 
                                   DEM90m, 
                                   "DEM90_Mosaic_2021Jan4", 
                                   "GEOGCS['GCS_WGS_1984',
                                   DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
                                   PRIMEM['Greenwich',0.0],
                                   UNIT['Degree',0.0174532925199433]]", 
                                   "16_BIT_SIGNED", 
                                   "8.33333333333333E-04", 
                                   "1", 
                                   "MEAN", 
                                   "FIRST")
