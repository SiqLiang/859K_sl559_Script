import arcpy
import os
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch3"
os.chdir("C:\\859K_sl559\\Doc")

fileName="DEMFC30_PA_Spelaeornis_longicaudatus.tif"
rows = arcpy.da.SearchCursor(fileName, ["Value", "Count"],'"VALUE" = 1')
scientific_name = fileName[11:fileName.rfind('.')]
print(scientific_name)


for row in rows:
    print("1")
else:
    print("No rows found")