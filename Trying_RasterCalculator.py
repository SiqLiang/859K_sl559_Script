#Reby Forest Cover 30
import arcpy
from arcpy.sa import *
# Check out the Spatial Analyst extension license

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Data"

FC_raster= "C:\\859K_sl559\\Data\\H_TC2000_ReC.tif"
PA_raster= '‪C:\\859K_sl559\\Data\\SumPA_rC.tif'
out_raster= "‪C:\\859K_sl559\\Scratch\\out_raster.tif"



from arcpy.sa import *
out_rc_multi_raster = arcpy.gp.RasterCalculator_sa(["H_TC2000_ReC.tif", "SumPA_rC.tif"],
                                       ["x", "y"], "x-y")
out_rc_multi_raster.save("C:\\859K_sl559\\Data\\raster_rc_multi.tif")



