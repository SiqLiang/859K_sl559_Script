##This script takes the rsasters in a folder and refines them
##by a raster classified as 1=suitable and 0=unsuitable land cover
###German Forero
###MAy 2011

##--------------------------------------------------------------------------------------------------

import arcgisscripting
gp = arcgisscripting.create()

import arcpy
#arcpy.env.outputCoordinateSystem = "PROJCS['SIRGAS_Transverse_Mercator',GEOGCS['GCS_SIRGAS',DATUM['D_SIRGAS',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1000000.0],PARAMETER['False_Northing',1000000.0],PARAMETER['Central_Meridian',-74.07750791666666],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',4.596200416666666],UNIT['Meter',1.0]]"

#create the workspace and the fixed variables
gp.workspace = r"G:\China\Bird\Endangered\forest\ele"
#the habitat variable to get suitable habitat (=1)
#habitat1 = r'C:\Users\bl113\Documents\China\landcover_China\ESA\China landcover classification\agri_wet'
#arcpy.ProjectRaster_management(habitat1,"C:/Users/bl113/Documents/China/landcover_China/ESA/China_landcover_clssification_albers/agri_wet","PROJCS['Asia_North_Albers_Equal_Area_Conic',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',105.0],PARAMETER['Standard_Parallel_1',27.0],PARAMETER['Standard_Parallel_2',45.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","NEAREST","315.640355247801","#","#","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
habitat="G:\\China\\landcover_China\\ESA\\China_landcover_clssification_albers\\forest"
#check the sptaial analyst extension
gp.CheckOutExtension("Spatial")
gp.toolbox = "analysis"

#create the ouput file
outraster=r'G:\China\Bird\Endangered\forest\habitat\\reftX'
i=0
FCs = gp.ListRasters("*")
FCs.Reset()
FC = FCs.Next()
while FC:
    print FC
    #refine by habitat
    ##do the algebra expression:
    #replace output name
    OutRast = outraster.replace("X",FC)
    #do the map algebra to refine the range by suitable habitat:
    arcpy.gp.SingleOutputMapAlgebra_sa("CON((%s > 0 AND %s > 0), 1,0)" % (habitat, FC), OutRast)
    #gp.Reclassify_sa(OutRast1, "Value", "1 1;NODATA 0",OutRast)
    i+=1
    FC = FCs.Next()
	
FCs = None
