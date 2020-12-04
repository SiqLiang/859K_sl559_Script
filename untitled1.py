# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:01:09 2020

@author: sl559
"""

import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\859K_sl559\Data\ModisFire2001_2019"
arcpy.env.extent = "C:\859K_sl559\Scratch3\ReclassNoData_H_TC2000.tif"