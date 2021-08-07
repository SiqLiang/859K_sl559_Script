#step4.15,4.16Compute Euclidean distance using non-habitat cells as the source. (Note: you'll first have to invert
#your habitat or patch raster so that habitat cells are given a value of NoData).

#?why I have step 4.16? it seems duplicated 
import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch_DistanceToEdge"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"

# Local variables:
RegionG2_rCRGrCndTC2000_Proj_tif="C:\\859K_sl559\\Scratch_DistanceToEdge\\Projected_RegionG2_Reclass_RegionG_FC2000_ROIexpanded_300m.tif"
ReC2_RegionG2_TC2000_Proj_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\ReC2_Proj_RegionG2_ReC1_RegionG1_FC2000_ROIexpanded_300m.tif"
#Execute Reclassify 
reclassField = "Count"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha
remap = "9 9904221 NODATA; NODATA 1"
arcpy.gp.Reclassify_sa(RegionG2_rCRGrCndTC2000_Proj_tif, reclassField, remap, ReC2_RegionG2_TC2000_Proj_tif)
