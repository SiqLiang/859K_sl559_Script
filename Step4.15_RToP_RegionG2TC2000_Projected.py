#Before I calculate the area and perimeter of each forest patch,
#I need to project the shapfile into World_Eckert_IV

# Import arcpy module
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
#
print (os.path.exists("C:\\859K_sl559\\Data\\RegionOfInterest.shp"))
#
print (os.path.exists("C:\\859K_sl559\\Scratch3\\RasterToPolygon_RegionG2TC2000.shp"))

# Local variables:
RasterToPolygon_RegionG2TC2000_shp = "C:\\859K_sl559\\Scratch3\\RasterToPolygon_RegionG2TC2000.shp"
RToP_RegionG2TC2000_Projected1_shp= "C:\\859K_sl559\\Scratch3\\RToP_RegionG2TC2000_Projected1.shp"
# Process: Project
arcpy.Project_management(RasterToPolygon_RegionG2TC2000_shp, RToP_RegionG2TC2000_Projected1_shp, "PROJCS['World_Eckert_IV',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Eckert_IV'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")


