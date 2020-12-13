import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\Dejure_PA"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
#input datasets
inputShapefile = "C:\\859K_sl559\\Data\\Dejure_PA\\WDPApolygon_ChinaPA_roiClip_Merge.shp"

#polygon to raster
BLraw = "rawDejure_2020Dec12" + ".tif"
cellSize = 0.0008333
field = "RasterValue"
arcpy.FeatureToRaster_conversion(inputShapefile, field, BLraw, cellSize)


