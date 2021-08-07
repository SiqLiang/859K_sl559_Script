# The patch with cellsize smaller than 113 i.e. 100 hacter were reclassified into NoData in arcgis pro
import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch_DistanceToEdge"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")


RegionG_FC2000_MtoNR_rC_FC30_tif= "C:\\859K_sl559\\Scratch_DistanceToEdge\\RegionG_FC2000_MtoNR_rC_FC30_ROIexpanded_300m.tif"
Reclass_RegionG_FC2000_tif = "C:\\859K_sl559\\Scratch_DistanceToEdge\\Reclass_RegionG_FC2000_ROIexpanded_300m.tif"

#Execute Reclassify 
reclassField = "Count"
#for projection World_Eckert_IV
#cellsize= 94.126759784775m*94.126759784775m/10000 = 0.88598469075807 ha
#100ha/cellsize=112.87  ; patch with 113cell is bigger than 100ha

#for projection World_Eckert_IV
#cellsize= 321.977497514191m*321.977497514191m/10000 = 10.36695089055009 ha
#100ha/cellsize=9.64603778447086  ; patch with 10cell is bigger than 100ha
remap = "1 9 NODATA; NODATA NODATA"
arcpy.gp.Reclassify_sa(RegionG_FC2000_MtoNR_rC_FC30_tif, reclassField, remap, Reclass_RegionG_FC2000_tif)

