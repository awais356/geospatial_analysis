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
    # outRaster = Slope(raster)
    # outRaster.save("elev_slope.tif")

    ##############################
    # Step 3
    ##############################

    ##############################
    # Step 4
    ##############################
    raster = "elevation"
    outRaster = Slope(raster)
    outRaster.save("elev_slope.tif")
    hillRaster = Hillshade(raster)
    hillRaster.save("elev_hill.tif")
    aspectRaster = Aspect(raster)
    aspectRaster.save("elev_aspect.tif")
main()
