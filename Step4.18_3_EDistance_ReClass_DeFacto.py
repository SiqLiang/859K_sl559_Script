
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
arcpy.env.outputCoordinateSystem ="EucDist_reC_RegionG2_TC2000_Proj.tif"

# Local variables:
EucDist_reC_RegionG2_TC2000_Proj_tif = "EucDist_reC_RegionG2_TC2000_Proj.tif"
DeFacto_EucDist_reC_RegionG2_TC2000_Proj_tif = "C:\\859K_sl559\\Scratch3\\DeFacto_EucDist_reC_RegionG2_TC2000_Proj.tif"

# Process: Reclassify
arcpy.gp.Reclassify_sa(EucDist_reC_RegionG2_TC2000_Proj_tif, "VALUE", "0 3000 NODATA;3000 13604 1", DeFacto_EucDist_reC_RegionG2_TC2000_Proj_tif, "DATA")

 