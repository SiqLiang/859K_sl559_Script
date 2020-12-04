# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:20:29 2020

@author: sl559
I have regiongrouped the ReclassNoData_H_TC2000.tif file to
RegionG_rCNoDataTC2000_test2.tif, and classified the clusters with 
cellsize smaller than 113 to nodata, the result is
Reclass_RegionG_rCNTC2000.tif. 
Now, I run the 2nd regiongroup to sign a sequantial name to each cluster.
"""
#2020Dec4
# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"
print (os.path.exists("C:\\859K_sl559\\Scratch3\\ReclassNoData_H_TC2000.tif"))
print (os.path.exists("C:\\859K_sl559\\Scratch3\\Reclass_RegionG_rCNTC2000.tif"))
# Local variables:
Reclass_RegionG_rCNTC2000_tif = "C:\\859K_sl559\\Scratch3\\Reclass_RegionG_rCNTC2000.tif"
RegionG2_rCRGrCndTC2000_tif = "C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000.tif"
# Process: Region Group
arcpy.gp.RegionGroup_sa(Reclass_RegionG_rCNTC2000_tif, RegionG2_rCRGrCndTC2000_tif, "FOUR", "WITHIN", "ADD_LINK", "")

print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000_tif"))
