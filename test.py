import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

inputShapefile = "C:\\859K_sl559\\Data\\EndemicBirdSpecies_inROI_final.shp"
DEM_roi = "C:\\859K_sl559\\Data\\Area_mask_DEM90m_final.tif"

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(inputShapefile,['FID', "Scientific", "Min", "Max"]) 
row = rows.next()

for i in range (0,83,1):
    fid = row[0]
    scientific_name=row[1]
    Min_elevation=row[2]
    Max_elevation=row[3]
    print(row)
    print(Min_elevation)
    print(Max_elevation)
    
    #multishapefile to single shapfiles
    arcpy.AddMessage("Producing {} indivial shapfile".format(row[1]))
    poly_out = "Sp_"+scientific_name+".shp"
    arcpy.Select_analysis(inputShapefile,poly_out,"\"FID\"= %i"%i) 
    
    #Execute Feature to Raster
    arcpy.AddMessage("Producing {} raw raster".format(row[1]))
    RawRaster_out = "RawRaster_"+scientific_name+".tif"
    cellSize = 0.0008333
    field = "83LandBird"
    arcpy.FeatureToRaster_conversion(poly_out, field, RawRaster_out, cellSize)
    
    #Execute Reclassify
    arcpy.AddMessage("Reclassifying {} raw raster".format(row[1]))
    reclassField = "Value"
    remap = "0 0; 1 100000000000 1; NODATA 0"
    Reclass_out= "ReClassRaster_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(RawRaster_out, reclassField, remap, Reclass_out)
   
    #Execute Con DEM, failed
    Input_true_raster_or_constant_value = "1"
    Input_false_raster_or_constant_value = "0"
    ConDEM_out = "ConDEM_"+scientific_name+".tif"
    whereClause = "\"Value\" >= {} AND \"Value\" <={}".format(Min_elevation, Max_elevation)
    print(whereClause)
    arcpy.gp.Con_sa(DEM_roi, Input_true_raster_or_constant_value, 
                ConDEM_out, Input_false_raster_or_constant_value, 
                whereClause)
    
    row = rows.next()
del rows




