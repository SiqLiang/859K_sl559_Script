import arcpy
from arcpy.sa import *

# allow overwrite
arcpy.env.overwriteOutput = True

# Set the analysis environments
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"

#input datasets
inputShapefile = "C:\\859K_sl559\\Data\\EndemicBirdSpecies_inROI_final.shp"
DEM_roi = "C:\\859K_sl559\\Data\\Area_mask_DEM90m_final.tif"
FC30_roi= "C:\\859K_sl559\\Data\\H_TC2000_ReC.tif"


#setting coordinate system
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
#Try later: 54012 is the WKID of World Eckert IV
#Try later: outputSR = arcpy.SpatialReference(54002)
#Try later: arcpy.CreateFeatureclass_management(outPath,outName,"POINT","","","",outputSR)

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
    
    #Execute BL_Map Feature to Raster
    arcpy.AddMessage("Producing {} raw raster".format(row[1]))
    BLraw = "BLraw_"+scientific_name+".tif"
    cellSize = 0.000833333333333333
    field = "83LandBird"
    arcpy.FeatureToRaster_conversion(poly_out, field, BLraw, cellSize)
    
    #Execute Reclassify BL_Map
    arcpy.AddMessage("Reclassifying {} raw raster".format(row[1]))
    reclassField = "Value"
    remap = "0 0; 1 100000000000 1; NODATA 0"
    BL_Map= "BL_Map_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(BLraw, reclassField, remap, BL_Map)
   
    #Execute Con to DEM, get ConRaw
    Input_true_raster_or_constant_value = "1"
    Input_false_raster_or_constant_value = "0"
    ConRaw = "ConRaw_"+scientific_name+".tif"
    whereClause = "\"Value\" >= {} AND \"Value\" <={}".format(Min_elevation, Max_elevation)
    print(whereClause)
    arcpy.gp.Con_sa(DEM_roi, Input_true_raster_or_constant_value, 
                ConRaw, Input_false_raster_or_constant_value, 
                whereClause)
    #Reclassify ConRaw
    reclassField = "Value"
    remap = "0 0; 1 1; NODATA 0"
    ConDEM= "ConDEM_"+scientific_name+".tif"
    arcpy.gp.Reclassify_sa(ConRaw, reclassField, remap, ConDEM)
    
    #BL_Map Refined by species elevation range
    ReBy_DEM = Raster(BL_Map)*Raster(ConDEM)
    ReBy_DEM.save("ReBy_DEM_"+scientific_name+".tif")
    
    #BL_Map Refined by Forest Cover >30
    ReBy_FC30 = Raster(BL_Map)*Raster(FC30_roi)
    ReBy_FC30.save("ReBy_FC30_"+scientific_name+".tif")
    
    #BL_Map Refined by both species elevation range and Forest Cover>30 (Double Refined)
    ReBy_DEMFC30 = Raster(BL_Map)*Raster(ConDEM)*Raster(FC30_roi)
    ReBy_DEMFC30.save("ReBy_DEMFC30_"+scientific_name+".tif")
    
    row = rows.next()
del rows     

#fileList = arcpy.ListRasters('BL_Map_*', 'All')
#len(fileList)

#fileList = arcpy.ListRasters('ReBy_DEM_*', 'All')
#len(fileList)

#fileList = arcpy.ListRasters('ReBy_FC30_*', 'All')
#len(fileList)

#fileList = arcpy.ListRasters('ReBy_DEMFC30_*', 'All')
#len(fileList)





