import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Data\\Defacto_PA"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem ="C:\\859K_sl559\\Data\\RegionOfInterest.shp"

# Local variables:
in_shp = "Dissolved_DeFacto_3000m.shp"
PtR_DeFacto_3000m_tif= "PtR_DeFacto_3000m.tif"

cellsize = 0.00083333333
field = "gridcode"
arcpy.FeatureToRaster_conversion(in_shp, field, PtR_DeFacto_3000m_tif, cellsize)

# Process: Reclassify
Reclassified_PtR_DeFacto_3000m_tif= "Reclassified_PtR_DeFacto_3000m.tif"
arcpy.gp.Reclassify_sa(PtR_DeFacto_3000m_tif, "VALUE", "1 1;NODATA 0", Reclassified_PtR_DeFacto_3000m_tif, "DATA")

