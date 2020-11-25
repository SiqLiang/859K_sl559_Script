import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch\\KMZ"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"


# Specify the feature class to examine
inputShapefile = "C:\\859K_sl559\\Data\\EndemicBirdSpecies_inROI.shp"

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(inputShapefile,['FID','83LandBi_5']) #Field names shall be changed according to the input shapefile
row = rows.next()
for i in range (0,83,1):
    fid = row[0]
    scientific_name = row[1]
    
    #multishapefile to single shapfiles
    poly_out = "Sp_"+scientific_name+".shp"
    arcpy.Select_analysis(inputShapefile,poly_out,"\"FID\"= %i"%i) 
    
    #Execute Feature to KML
    kml_out= "KMZ_"+scientific_name+".kmz"
    arcpy.LayerToKML_conversion(poly_out, kml_out)
    
    row = rows.next()
del rows














