# This script takes a bunch of rasters in a folder and extracts the count values, 
# multiplies it by the cell size, and outputs the area in a table (readable to Excel)

# import necessary arc functions.
import arcpy
import os
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scaratch1_1_BL_Map_rasters_and_doc"

fileList = arcpy.ListRasters('BL_Map_*', 'All')
len(fileList)

# print the current working directory
print (os.getcwd())
# Create a new file in the current working directory, write some text, and close it
BL_Map_fileObj = open("BL_Map_RasterArea.txt",'w')
print (os.path.exists("C:\\859K_sl559\\Scaratch1_1_BL_Map_rasters_and_doc\\BL_Map_RasterArea.txt"))
# create constant and loop variables.
# for projection World_Eckert_IV
cellsize = 94.126759784775*94.126759784775/1000000
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.0088598469075807 square km2
BL_Map_fileObj.write("Hello there!")
BL_Map_fileObj.write('Species, '+'Area'+"\n")

#fileList = arcpy.ListRasters('BL_Map_*')

#for fileName in fileList:
    #print(fileName)
    #scientific_name = fileName[7:fileName.rfind('.')]
    #sCur = arcpy.da.SearchCursor(fileName, "Value", '"Value" = 1')
    #cellCount = sCur.getValue("COUNT")
    #area = cellCount*cellsize
    #areaOut.write(str(scientific_name)+', '+str(area)+"\n")
#fileObj.write("Hello there!")
fileObj.close()
