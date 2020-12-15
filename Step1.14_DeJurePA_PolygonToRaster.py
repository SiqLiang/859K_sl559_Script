import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\Dejure_PA\\DejurePA.gdb"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
#input datasets
inputShapefile = "DejurePA_2020Dec12"

#polygon to raster
raster_raw = "rawDejure_2020Dec12"
cellSize = 0.0008333
field = "RasterValu"
arcpy.FeatureToRaster_conversion(inputShapefile, field, raster_raw, cellSize)


