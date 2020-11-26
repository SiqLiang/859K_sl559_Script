# This script takes a bunch of rasters in a folder and extracts the count values, multiplies it by the cell size, and outputs the area in a table (readable to Excel)

# import necessary arc functions.
import arcgisscripting
import arcpy
import os
gp = arcgisscripting.create()
gp.overwriteoutput = 1


# check spatial analyst extension, and set workspace.
gp.CheckOutExtension("Spatial")
gp.toolbox = "analysis"
gp.workspace= r'G:\China\Bird\Endangered\forest\chn_habitat'

# create constant and loop variables.
cellsize = 96.91030926*96.91030926/1000000
areaOut = open(r'G:\China\General_Data_Sheet\GAP\endangered\for_bird_area', 'a')
areaOut.write('Species, '+'Area'+"\n")

# create list of rasters in directory.
fileList = gp.ListRasters("*")
fileList.Reset()
fileName = fileList.Next()


while fileName:
    # Create a search cursor for desired raster VALUE, extract COUNT and multiply by cellsize to get area.
    sCur = gp.SearchCursor(fileName, '"VALUE" = 1')
    for row in sCur:
        cellCount = row.getValue("COUNT")
        area = cellCount*cellsize
        print 'Current species: '+str(fileName)
        print 'computing area...'
        print 'Area = '+str(area)+' square kilometers'
        areaOut.write(str(fileName)+', '+str(area)+"\n")
        print 'Species area information successfully appended to output file.'
        print '---------------------------------------------------------------'
        fileName = fileList.Next()

fileList = None
# Final .csv file has each file name with its corresponding area as a row. File can be read into Excel.
