import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Data\\SumUp_Dejure_Defacto"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
DeJure= "C:\\859K_sl559\\Data\\SumUp_Dejure_Defacto\\Classified_Dejure_PA_2020Dec16.tif"
DeFacto4000m="C:\\859K_sl559\\Data\\SumUp_Dejure_Defacto\\Reclass_DeFacto_4000m.tif"

raw_DeJure_DeFacto4000m = Raster(DeJure)+Raster(DeFacto4000m)
raw_DeJure_DeFacto4000m.save("raw_DeJure_DeFacto4000m.tif")

reclassField = "Value"
remap = "0 0; 1 2 1; NODATA 0"
DeJure_DeFacto4000m_tif= "DeJure_DeFacto4000m.tif"
arcpy.gp.Reclassify_sa("raw_DeJure_DeFacto4000m.tif", reclassField, remap, DeJure_DeFacto4000m_tif)
