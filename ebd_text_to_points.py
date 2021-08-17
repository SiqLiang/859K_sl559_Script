# XYTableToPoint.py
# Description: Creates a point feature class from input table

# import system modules 
import arcpy
import os
import pandas as pd
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

path= "C:\\859K_sl559\\Data\\Ebird\\ebird_csv"
filelist= os.listdir(path)
for file in filelist:
  ebd_sp_name = file[0:file.rfind('.')]
  print(ebd_sp_name)
  in_table = file
  out_feature_class = "C:\\859K_sl559\\Scratch_ebird\\"+str(ebd_sp_name)+".shp"
  x_coords = "LONGITUDE"
  y_coords = "lATITUDE"
  z_coords = ""
  # Make the XY event layer...
  arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords,z_coords,
                                arcpy.SpatialReference(4759, 115700))

