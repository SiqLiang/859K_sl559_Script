import arcpy
import os

arcpy.env.workspace ="C:\\859K_sl559\\Scratch\\KMZ"
arcpy.env.overwriteOutput = True
# Set Local Variables
composite = 'NO_COMPOSITE'
pixels = 2048
dpi = 96
clamped = 'CLAMPED_TO_GROUND'

# Use the ListFiles method to identify all lyr and lyrx files in workspace
layers = arcpy.ListFiles("*.shp") 
len(layers)

if len(layers) > 0:
    for layer in layers:        
        # Strips the '.lyr(x)' part of the name and appends '.kmz'
        outKML = os.path.join(os.path.splitext(layer), ".kmz")
        for scale in range(10000, 30001, 10000):
            # Execute LayerToKML
            arcpy.LayerToKML_conversion(layer, outKML, scale, composite, 
                                        '', pixels, dpi, clamped)
else:
    arcpy.AddMessage('There are no layer files in {}'.format(arcpy.env.workspace))