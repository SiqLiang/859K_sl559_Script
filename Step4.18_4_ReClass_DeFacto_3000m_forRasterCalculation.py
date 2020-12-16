import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Data\\Defacto_PA"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem ="C:\\859K_sl559\\Data\\RegionOfInterest.shp"

# Local variables:
cellsize = "‪C:\859K_sl559\Data\Area_mask_DEM90m_final.tif"
DeFacto_EucDist_reC_RegionG2_TC2000_Proj_tif = "DeFacto_EucDist_reC_RegionG2_TC2000_Proj.tif"
Reclassified_DeFacto_3000m_tif= "Reclassified_DeFacto_3000m.tif"

# Process: Reclassify
arcpy.gp.Reclassify_sa(DeFacto_EucDist_reC_RegionG2_TC2000_Proj_tif, "VALUE", "1 1;NODATA 0", Reclassified_DeFacto_3000m_tif, "DATA")

