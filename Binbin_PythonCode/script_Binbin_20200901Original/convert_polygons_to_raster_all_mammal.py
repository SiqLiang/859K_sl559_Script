##Binbin Li / Oct 31/2012 arcpy
##This script takes a shapefile with mutliple polygons, selects each
##indidivual polygon (row) and converts it into a raster. Output in same folder

#import arcgisscripting
import arcpy
from arcpy import analysis

#gp = arcgisscripting.create(10)
arcpy.env.overwriteOutput = True

#check the sptaial analyst extension
arcpy.CheckOutExtension("Spatial")
#gp.toolbox = "analysis"

arcpy.env.workspace = r'G:\\map\\first_paper\\data\\all_mammal_raster'
inShp = 'G:\\China\\General_Data_Sheet\\IUCN_new_range\\MAMMTERR\\MAMMTERR\\mammal_all_chn_pj_new.shp'


#set the environment (using arcpy)
tempEnvironment0 = arcpy.env.snapRaster
arcpy.env.snapRaster = "G:\\map\\binbin\\bird_endemic_new\\sum_shape\\sumBirdnew.img"
#tempEnvironment1 = gp.extent
arcpy.env.extent = "-2656565.139027 1868513.05239 2221544.027142 5889911.130334"
arcpy.env.outputCoordinateSystem ="G:\China\landcover_China\DEM\90mchn_alber"

names = []
rows = arcpy.SearchCursor(inShp)
row = rows.next()
print "Getting list of names\n"
while row:
    print (row.binomial)
    names.append(row.binomial)
    row = rows.next()

print "extracting ranges\n"
arcpy.MakeFeatureLayer_management(inShp, 'inLyr')
for name in names:
    expr = '"BINOMIAL" = \'%s\'' %(name)
    print expr
    arcpy.SelectLayerByAttribute_management ('inLyr', "NEW_SELECTION", expr)
    #Convert to a raster:need to specifiy the field name which has only 1
    arcpy.PolygonToRaster_conversion('inLyr',"Origin", name + '.img', "CELL_CENTER", "","315.6403552")
###up to here the script takes the list of sp and transform them into raster and puts them in same folder

    
##The End
