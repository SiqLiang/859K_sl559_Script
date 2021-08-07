#2020Dec4
# Import arcpy module
import arcpy
import os
arcpy.env.workspace = "C:\\859K_sl559\\Scratch_DistanceToEdge"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")


FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\FC2000_MtoNR_rC_FC30_ROIexpanded_300m.tif"
RegionG_FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded_300m.tif"
arcpy.gp.RegionGroup_sa(FC2000_MtoNR_rC_FC30_tif, RegionG_FC2000_MtoNR_rC_FC30_tif, "FOUR", "WITHIN", "ADD_LINK", "")
print (os.path.exists("C:\\859K_sl559\\Scratch_DistanceToEdge\\RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded_300m.tif"))