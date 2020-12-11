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


##Mosaic several TIFF images to a new TIFF image
arcpy.MosaicToNewRaster_management("landsatb4a.tif;landsatb4b.tif","Mosaic2New", "landsat.tif", "World_Mercator.prj",\
                                   "8_BIT_UNSIGNED", "40", "1", "LAST","FIRST")