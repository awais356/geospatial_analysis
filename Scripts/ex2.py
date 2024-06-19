# -----------------------------------------------------------------------------
# Name:        GS2110.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     14/03/2023
# -----------------------------------------------------------------------------

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
    # For each required parameter set a variable
    # Set the output path or workspace if required
    # Note the trailing /
    # output_ws = "../Vector/Results/"
    # output_ws = "../GDB/GDB_OUTPUT_NAME.gdb/"

    ##############################
    # Step 4
    ##############################
    wild_card = "*"
    raster_type = "*"
    # Get and print a list of GRIDs from the workspace
    rasters = arcpy.ListRasters(wild_card, raster_type)
    for raster in rasters:

        desc = arcpy.Describe(raster)
        print("*" * 50)
        print(f"Raster Name:{desc.name}")
        print(f"Band Count:{desc.bandCount}")
        for rb in desc.children:
            print(f"Layer: {rb.name}")
            descBand = arcpy.Describe(raster + "/" + rb.name)
            print(f"Mean Cell Height: {descBand.meanCellHeight}")
            print(f"Mean Cell Width: {descBand.meanCellWidth}")
            print(f"Raster Pixel Type: {descBand.pixelType}")

main()
