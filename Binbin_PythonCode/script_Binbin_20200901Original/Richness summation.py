import arcpy
import arcgisscripting
from arcpy import env
from arcpy.sa import *
env.workspace = 'C:\\Users\\bl113\\Desktop\\research_project\\earthquake and biodiversity\\process\\rx5day_rasters\\1980-2019'
print env.workspace
# system configuration
gp = arcgisscripting.create()
gp.CheckOutExtension("Spatial")
gp.toolbox = "analysis"

#set the environment (using arcpy)
#tempEnvironment0 = arcpy.env.snapRaster
#arcpy.env.snapRaster = "G:\\map\\binbin\\bird_endemic_new\\sum_shape\\sumBirdnew.img"
#tempEnvironment1 = gp.extent
#arcpy.env.outputCoordinateSystem ="G:\China\landcover_China\DEM\90mchn_alber"

# set init value
sumRas = 0
n=0

# loop through file list
fileList = arcpy.ListRasters('*', 'All')
for fileName in fileList:
    print(fileName)
    #maxcell=arcpy.GetRasterProperties_management (fileName, "ROWCOUNT")
    #print maxcell
    sumRas = arcpy.Raster(fileName) + sumRas
    #print arcpy.GetRasterProperties_management (sumRas, "MAXIMUM")
    n=n+1
print n
sumRas.save('C:\\Users\\bl113\\Desktop\\research_project\\earthquake and biodiversity\\process\\rx5day_rasters\\1980_2019.img')
