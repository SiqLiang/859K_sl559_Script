import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.workspace = "C:\\859K_sl559\\Scratch4"
arcpy.env.extent = "C:\\859K_sl559\\Data\\RegionOfInterest.shp"
#
print("import arcpy")
fileList = arcpy.ListRasters('RcReBy_DEMFC30_*')
len(fileList) #Check how many Reclassified rasters are avaiable now
for fileName in fileList:
    scientific_name = fileName[15:fileName.rfind('.')]
    input_raster= 'RcReBy_DEMFC30_'+scientific_name+".tif"
    output_kmz= "C:/859K_sl559/Scratch5/"+"DEMFC30_"+scientific_name+".kmz"
    print("arcpy.LayerToKML_conversion(\"{0}\",\"{1}\", \"0\", \"NO_COMPOSITE\", \" \", \"2048\", \"96\", \"CLAMPED_TO_GROUND\")".format(input_raster,output_kmz))
###AndThen Run these code in the python window in arcMap.These code can run in arcpro too, but all the kml in black instead of with different colors.