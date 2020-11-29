# import necessary arc functions.
import arcpy
import os
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scaratch1_1_BL_Map_rasters_and_doc"

fileList = arcpy.ListRasters('BL_Map_*', 'All')
len(fileList)
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[7:fileName.rfind('.')]
    print( scientific_name)
    # Create a search cursor for desired raster VALUE, extract COUNT and multiply by cellsize to get area.
    rows = arcpy.da.SearchCursor(fileName, ["Value", "Count"], '"VALUE" = 1')
    row = rows.next()
    CellCount= row[1]
    print(CellCount)