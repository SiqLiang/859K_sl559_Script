# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ArcMap_LayerToKML_original.py
# Created on: 2020-12-12 22:28:25.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
RtP_RcReBy_DEMFC30_Acanthoptila_nipalensis = "RtP_RcReBy_DEMFC30_Acanthoptila_nipalensis"
RtP_RcReBy_DEMFC30_Acanthopt_kmz = "C:\\859K_sl559\\Scratch4\\RtP_RcReBy_DEMFC30_Acanthopt.kmz"

# Process: Layer To KML
arcpy.LayerToKML_conversion(RtP_RcReBy_DEMFC30_Acanthoptila_nipalensis, RtP_RcReBy_DEMFC30_Acanthopt_kmz, "0", "NO_COMPOSITE", "79.9999999998693 19.9999999998856 108.10000000081 33.999999999612", "1024", "96", "CLAMPED_TO_GROUND")
