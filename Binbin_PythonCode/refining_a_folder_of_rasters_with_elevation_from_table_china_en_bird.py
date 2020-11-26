## Binbin Li, Dec 2012
## For China umbrella species project
## Refine a folder of polygon ranges with elevational preferences 

##--------------------------------------------------------------------------------------------------

import arcgisscripting
gp = arcgisscripting.create()

#create the workspace and the fixed variables
gp.workspace = r"H:\\map\\binbin\\bird_endemic_new\\zero"
#the DEM to get elevations
demchina = r'H:\China\landcover_China\DEM\90mchn_alber'
shape=r'H:\\map\\binbin\\bird_endemic_new\\sum_shape\\info.shp'


#check the sptaial analyst extension
gp.CheckOutExtension("Spatial")
gp.toolbox = "analysis"

#create the ouput file
outraster=r"H:\map\\binbin\\bird_endemic_new\\ele\\eleX"

FCs = gp.ListRasters("*")
FCs.Reset()
FC = FCs.Next()
while FC:
    print FC
    #refine by elevation
    #first get the elevation for the species
    recs = gp.searchcursor(shape)
    for rec in recs:
        if rec.SCINAME == FC[4:FC.rfind('.')]:
            min_elev = rec.getvalue('Min')
            print min_elev
            max_elev = rec.getvalue('Max')
            print max_elev
        ##Second part: do the algebra expression:
        #replace output name

    OutRast = outraster.replace("X",FC)
    #do the map algebra to refine the range by elevation
    gp.SingleOutputMapAlgebra_sa("CON((%s > %d AND %s < %d AND %s > 0),1,0)" % (demchina, min_elev, demchina, max_elev, FC), OutRast)
    print FC
    FC = FCs.Next()

FCs = None





