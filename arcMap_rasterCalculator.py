# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# arcMap_rasterCalculator.py
# Created on: 2020-11-26 17:53:44.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
H_TC2000_ReC_tif = "H_TC2000_ReC.tif"
SumPA_rC_tif = "SumPA_rC.tif"
rastercalc = "C:\\Users\\sl559\\Documents\\ArcGIS\\Default.gdb\\rastercalc"

# Process: Raster Calculator
arcpy.gp.RasterCalculator_sa("\"%H_TC2000_ReC.tif%\" * \"%SumPA_rC.tif%\"", rastercalc)

