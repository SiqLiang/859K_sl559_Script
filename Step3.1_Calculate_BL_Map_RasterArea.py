# This script takes a bunch of rasters in a folder and extracts the count values, 
# multiplies it by the cell size, and outputs the area in a table (readable to Excel)

# import necessary arc functions.
import arcpy
import os
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scaratch1_1_BL_Map_rasters_and_doc"

#print the current working directory
#print (os.getcwd())
#Check the existence of the target txt file
print (os.path.exists("C:\\859K_sl559\\Scaratch1_1_BL_Map_rasters_and_doc\\BL_Map_RasterArea.txt"))
# Create a new file in the current working directory, write some text, and remember to close it
BL_Map_fileObj = open("BL_Map_RasterArea.txt",'w')
BL_Map_fileObj.truncate(0) # clear eveything already in the txt file
BL_Map_fileObj.write('Species, '+'Area'+"\n")
#BL_Map_fileObj.close()

# create constant and loop variables.
# for projection World_Eckert_IV
cellsize = 94.126759784775*94.126759784775/1000000
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.0088598469075807 square km2

fileList = arcpy.ListRasters('BL_Map_*', 'All')
len(fileList)
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[7:fileName.rfind('.')]
    print( scientific_name)
    # Create a search cursor for desired raster VALUE, extract COUNT and multiply by cellsize to get area.
    sCur = arcpy.da.SearchCursor(fileName, ["Value", "Count"], '"VALUE" = 1')
    print (sCur[1])
    for row in sCur:
        cellCount = row.getValue("Count")
        area = cellCount*cellsize
        BL_Map_fileObj.write(str(scientific_name)+', '+str(area)+"\n")
        fileName = fileList.Next()



#for fileName in fileList:
    #print(fileName)
    #scientific_name = fileName[7:fileName.rfind('.')]
    #sCur = arcpy.da.SearchCursor(fileName, "Value", '"Value" = 1')
    #cellCount = sCur.getValue("COUNT")
    #area = cellCount*cellsize
    #areaOut.write(str(scientific_name)+', '+str(area)+"\n")
#fileObj.write("Hello there!")
BL_Map_fileObj.close()
