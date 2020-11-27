# Import arcpy module
import arcpy


arcpy.env.overwriteOutput = True
# Local variables:
Area_mask_DEM90m_final_tif = "C:\\859K_sl559\\Data\\Area_mask_DEM90m_final.tif"
Input_true_raster_or_constant_value = "1"
Input_false_raster_or_constant_value = "0"
Con_tif3 = "C:\\859K_sl559\\Scratch1\\Con_tif3.tif"

Min_elevation=3000
Max_elevation=4000
whereClause = "\"Value\" >= {} AND \"Value\" <={}".format(Min_elevation, Max_elevation)
print(whereClause)

# Process: Con
arcpy.gp.Con_sa(Area_mask_DEM90m_final_tif, Input_true_raster_or_constant_value, 
                Con_tif3, Input_false_raster_or_constant_value, 
                whereClause)


