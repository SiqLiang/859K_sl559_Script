# -*- coding: utf-8 -*-
"""
Reclassify_ESA_LC2018_forCategory1:Forest
Created on Wed Feb 24 18:26:27 2021

@author: sl559
"""

import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\ESA"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

inRas="LC2018_ROI.tif"
reclassField = "Value"
remap = "10 0;11 0;12 0;20 0;30 1;40 1;50 1;60 1;61 1;70 1;80 1;90 1;100 1;110 1;120 1;121 1;122 1;130 1;150 1;153 1;170 1;180 1;190 0;200 0;201 0;202 0;210 0;220 0;NODATA 0"
outRas= "‪LC2018_ROI_Category3.tif"
arcpy.gp.Reclassify_sa(inRas, reclassField, remap, outRas)
print(outRas)


