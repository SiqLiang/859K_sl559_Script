import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

inputShapefile = "C:\\859K_sl559\\Data\\EndemicBirdSpecies_inROI_final.shp"
FC_raster= "C:\\859K_sl559\\Data\\H_TC2000_ReC.tif"

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(inputShapefile,['FID', "Scientific", "Min", "Max"]) 
row = rows.next()
print(row)
for i in range (0,83,1):
    fid = row[0]
    scientific_name=row[1]
    Min_elevation=row[2]
    Max_elevation=row[3]
    
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
    
    #Execute Reby Forest Cover
    #out_fc_raster = arcpy.gp.RasterCalculator_sa([Reclass_out, FC_raster], ["x", "y"],"x*y", "", "FirstOf")
    #out_fc_raster.save("FC_"+scientific_name+".tif")
    
    row = rows.next()
del rows







