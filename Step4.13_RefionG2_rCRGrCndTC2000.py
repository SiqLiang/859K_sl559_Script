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

#---------
# Local variables:
RegionG2_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\RegionG2_Reclass_RegionG_FC2000_ROIexpanded_300m.tif"
ReC2_RegionG2_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\ReC2_RegionG2_ReC1_RegionG1_FC2000_ROIexpanded_300m.tif"
#Execute Reclassify 
reclassField = "Count"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha
remap = "9 9904221 NODATA; NODATA 1"
arcpy.gp.Reclassify_sa(RegionG2_tif, reclassField, remap, ReC2_RegionG2_tif)
#---------

#--------
#I conducted raster projection in arcmap pro with World Eckert Iv (NearstNeighbor)
# I also conducted EDistance in arcmap pro; distance method:Planar
#-------
