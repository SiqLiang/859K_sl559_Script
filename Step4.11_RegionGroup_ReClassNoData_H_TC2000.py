#2020Dec4
# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Data\\ForestCover2000"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
print (os.path.exists("C:\\859K_sl559\\Data\\ForestCover2000\\FC2000_MtoNR_rC_FC30_ROIexpanded.tif"))

# Local variables:
##ReclassNoData_H_TC2000_tif = "C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"
##RegionG_rCNoDataTC2000_test2_tif = "C:\\859K_sl559\\Scratch3\\RegionG_rCNoDataTC2000_test2.tif"

# Process: Region Group
##arcpy.gp.RegionGroup_sa(ReclassNoData_H_TC2000_tif, RegionG_rCNoDataTC2000_test2_tif, "FOUR", "WITHIN", "ADD_LINK", "")

##print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG_rCNoDataTC2000_test2.tif"))

FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Data\\ForestCover2000\\FC2000_MtoNR_rC_FC30_ROIexpanded.tif"
RegionG_FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Data\\ForestCover2000\\RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded.tif"
arcpy.gp.RegionGroup_sa(FC2000_MtoNR_rC_FC30_tif, RegionG_FC2000_MtoNR_rC_FC30_tif, "FOUR", "WITHIN", "ADD_LINK", "")
print (os.path.exists("C:\\859K_sl559\\Data\\ForestCover2000\\RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded.tif"))