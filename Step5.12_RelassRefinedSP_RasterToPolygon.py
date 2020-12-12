# Import arcpy module
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\859K_sl559\\Scratch1"


# Local variables:
ReBy_DEMFC30_Zoothera_salimalii_tif = "ReBy_DEMFC30_Zoothera_salimalii.tif"
RcReBy_DEMFC30_Zoothera_salimalii_tif= "RcReBy_DEMFC30_Zoothera_salimalii.tif"


arcpy.gp.Reclassify_sa(ReBy_DEMFC30_Zoothera_salimalii_tif, "VALUE", 
                       "0 NODATA;1 1;NODATA NODATA", 
                       RcReBy_DEMFC30_Zoothera_salimalii_tif, "DATA")

RtP_RcReBy_DEMFC30_Zoothera_salimalii_shp = "RtP_RcReBy_DEMFC30_Zoothera_salimalii.shp"

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(RcReBy_DEMFC30_Zoothera_salimalii_tif, RtP_RcReBy_DEMFC30_Zoothera_salimalii_shp, "NO_SIMPLIFY", "Value")

