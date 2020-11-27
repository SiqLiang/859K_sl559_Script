## Binbin Li, Dec 2012
## For China umbrella species project
## Refine a folder of polygon ranges with elevational preferences 
##--------------------------------------------------------------------------------------------------
import arcpy
import arcgisscripting
gp = arcgisscripting.create()

#create the workspace and the fixed variables
gp.workspace = "C:\\859K_sl559\\Scratch"
#the DEM to get elevations
dem = r'‪C:\859K_sl559\Data\Area_mask_DEM90m_final.tif'
inputShapefile = "C:\\859K_sl559\\Data\\EndemicBirdSpecies_inROI_final.shp"

#check the sptaial analyst extension
gp.CheckOutExtension("Spatial")
gp.toolbox = "analysis"

#create the ouput file
outraster=r"C:\859K_sl559\Scratch_Con"

FCs = gp.ListRasters("ReClassRaster*")
FCs.Reset()
FC = FCs.Next()

rows = arcpy.da.SearchCursor(inputShapefile,['FID', "Scientific", "Min", "Max"]) 
row = rows.next()
print(row)
while FC:
    print (FC)
    #refine by elevation
    #first get the elevation for the species
    recs = gp.searchcursor(inputShapefile)
    for rec in recs:
        print ("continue")
        if rec.Scientific == FC[14:FC.rfind('.')]:
            min_elev = rec.getvalue('Min')
            print (min_elev)
            max_elev = rec.getvalue('Max')
            print (max_elev)
        ##Second part: do the algebra expression:
        #replace output name

    OutRast = outraster.replace("X",FC)
    #do the map algebra to refine the range by elevation
    gp.SingleOutputMapAlgebra_sa("CON((%s > %d AND %s < %d AND %s > 0),1,0)" % (dem, min_elev, dem, max_elev, FC), OutRast)
    print (FC)
    FC = FCs.Next()

FCs = None



