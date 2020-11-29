import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data\\RawData"
#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

# Local variables:
All_Species_Row = "All_Species_CopyFeatures.shp"
All_Species_Dissolve = "All_Species_Dissolve"

# Process: Dissolve
arcpy.Dissolve_management(All_Species_Row, All_Species_Dissolve, "SISID", "", "MULTI_PART", "DISSOLVE_LINES")
