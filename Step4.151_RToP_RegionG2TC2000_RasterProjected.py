#Before I calculate the area and perimeter of each forest patch,
#I need to project the tif into World_Eckert_IV

# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
#
print (os.path.exists("C:\\859K_sl559\\Data\\RegionOfInterest.shp"))
#
print (os.path.exists("‪C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000.tif"))

# Local variables:
RegionG2_rCRGrCndTC2000_tif = "‪C:\\859K_sl559\\Scratch3\\RegionG2_rCRGrCndTC2000.tif"
RegionG2TC2000_RasterProjected_tif= "C:\\859K_sl559\\Scratch3\\RegionG2TC2000_RasterProjected.tif"
# Process: Project
arcpy.ProjectRaster_management(RegionG2_rCRGrCndTC2000_tif, RegionG2TC2000_RasterProjected_tif, "PROJCS['World_Eckert_IV',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Eckert_IV'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],UNIT['Meter',1.0]]", "NEAREST", "94.1231502405956 94.1231502405956", "", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

print (os.path.exists("C:\\859K_sl559\\Scratch3\\RegionG2TC2000_RasterProjected.tif"))
