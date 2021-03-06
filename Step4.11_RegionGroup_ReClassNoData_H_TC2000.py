#2020Dec4
# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"
print (os.path.exists("C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"))

# Local variables:
##ReclassNoData_H_TC2000_tif = "C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"
##RegionG_rCNoDataTC2000_test2_tif = "C:\\859K_sl559\\Scratch3\\RegionG_rCNoDataTC2000_test2.tif"

# Process: Region Group
##arcpy.gp.RegionGroup_sa(ReclassNoData_H_TC2000_tif, RegionG_rCNoDataTC2000_test2_tif, "FOUR", "WITHIN", "ADD_LINK", "")

##print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG_rCNoDataTC2000_test2.tif"))


SixFC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Data\\ForestCover2000\\SixFC2000_MtoNR_rC_FC30.tif"
RegionG_SixFC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Scratch3\\RegionG_SixFC2000_MtoNR_rC_FC30.tif"
arcpy.gp.RegionGroup_sa(SixFC2000_MtoNR_rC_FC30_tif, RegionG_SixFC2000_MtoNR_rC_FC30_tif, "FOUR", "WITHIN", "ADD_LINK", "")
print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG_SixFC2000_MtoNR_rC_FC30.tif"))