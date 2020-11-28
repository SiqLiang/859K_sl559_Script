# This script takes a bunch of rasters in a folder and extracts the count values, 
# multiplies it by the cell size, and outputs the area in a table (readable to Excel)

# import necessary arc functions.
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"

# create constant and loop variables.
# for projection World_Eckert_IV
cellsize = 94.126759784775*94.126759784775/1000000
#cellsize= 94.126759784775m*94.126759784775m/1000000 = 0.0088598469075807 square km2
areaOut = open('‪C:\\859K_sl559\\Doc\\BL_Map_RasterArea.txt')
areaOut.write('Species, '+'Area'+"\n")

fileList = arcpy.ListRasters('BL_Map_*', 'All')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    print(fileName)
    scientific_name = fileName[7:fileName.rfind('.')]
    
