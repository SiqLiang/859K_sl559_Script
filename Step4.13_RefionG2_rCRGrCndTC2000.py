# -*- coding: utf-8 -*-
"""
Created on 2021Aug6

@author: sl559
I have regiongrouped the FC2000_MtoNR_rC_FC30_ROIexpanded.tif file to
RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded_300m.tif, and classified the clusters with 
cellsize smaller than 113 to nodata, the result is
Reclass_RegionG_FC2000_ROIexpanded_300m.tif 
Now, I run the 2nd regiongroup to sign a sequantial name to each cluster.
"""
#2020Dec4
# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch_DistanceToEdge"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

# Local variables:
Reclass_RegionG_FC2000_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\Reclass_RegionG_FC2000_ROIexpanded_300m.tif"
RegionG2_rCRGrCndTC2000_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\RegionG2_Reclass_RegionG_FC2000_ROIexpanded_300m.tif"
# Process: Region Group
arcpy.gp.RegionGroup_sa(Reclass_RegionG_FC2000_tif, RegionG2_rCRGrCndTC2000_tif, "FOUR", "WITHIN", "ADD_LINK", "")


