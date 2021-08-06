# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:10:20 2020

@author: sl559
"""

# Import arcpy module
import arcpy
from arcpy.sa import *
# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\ForestCover2000"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
cellSize = 0.000833333333333333 #90m

# Local variables:
ForestCover2000_MosaictoNewRater_tif = "C:\\859K_sl559\\Data\\ForestCover2000\\ForestCover2000_MosaictoNewRater_ROIexpanded.tif"
FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Data\\ForestCover2000\\FC2000_MtoNR_rC_FC30_ROIexpanded.tif"
#Execute Reclassify 
reclassField = "Value"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha
remap = "0 30 NODATA;30 100 1; NODATA NODATA" # (0, 30]
arcpy.gp.Reclassify_sa(ForestCover2000_MosaictoNewRater_tif, reclassField, remap, FC2000_MtoNR_rC_FC30_tif)
#run successfully, however the output cellsize is still 0.00025 instead of the mentioned 0.0008333