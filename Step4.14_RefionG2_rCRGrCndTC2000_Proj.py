# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Data\\ForestCover2000"
arcpy.env.extent = "C:\\859K_sl559\\Data\\ROI\\RegionOfInterest_expanded.shp"

# Local variables:
RegionG2_rCRGrCndTC2000_tif = "C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000_ROIexpanded.tif"
RegionG2_rCRGrCndTC2000_Proj_tif="C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000_Proj_ROIexpanded.tif"
# Process: Project
arcpy.ProjectRaster_management(RegionG2_rCRGrCndTC2000_tif, RegionG2_rCRGrCndTC2000_Proj_tif, "PROJCS['World_Eckert_IV',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Eckert_IV'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],UNIT['Meter',1.0]]", "NEAREST", "94.1231502405956 94.1231502405956", "", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000_Proj.tif"))

#Check The documentaion standalone script; 
#It is a little bit complex, So I conducted this step in ArcMap(My PC)__Suessfully
