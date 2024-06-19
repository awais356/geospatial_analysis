# -----------------------------------------------------------------------------
# Name:        GS2110.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
#. Using the elevation raster as input write a script to create a slope, hill-shade and aspect raster
#name them as follows:
# Import Modules and classes as required
import arcpy


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
    # ListRasters ({wild_card}, {raster_type})
   ##############################
    # Step 3
    ##############################

    ##############################
    # Step 4
    ##############################
    wild_card = "*"
    raster_type = "TIF"
    # Get and print a list of GRIDs from the workspace
    rasters = arcpy.ListRasters(wild_card, raster_type)
    for raster in rasters:
        #desc = arcpy.Describe(raster)

        print(raster)


main()
