# -----------------------------------------------------------------------------
# Name:        GS2110.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
# . Using the elevation raster as input write a script to create a slope, hill-shade and aspect raster
# name them as follows:
# Import Modules and classes as required
import arcpy
from arcpy.sa import *

# Main Function
def main():
    #################################
    # Step 1
    # Environment settings
    #################################
    # Set the Workspace for inputs
    arcpy.env.workspace = "../Raster"

    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True

    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment

    ##############################
    # Step 3
    ##############################

    ##############################
    # Step 4
    ##############################
    inreclass = "elevation"
    myRemapRange = RemapRange([[1000, 2000, 1], [2000, 3000, 2], [3000, 4000, 3]])
    outReclassRR = Reclassify(inreclass, "VALUE", myRemapRange)
    outReclassRR.save("evel_reclass.tif")
main()