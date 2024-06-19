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
    rasters = arcpy.ListRasters(wild_card, raster_type)
    with open("rasterReport.txt", "w") as new_file:
        for raster in rasters:
            desc = arcpy.Describe(raster)
            new_file.write(f"{'Raster Name :':<20}{desc.name}\n")
            new_file.write(f"{'Band count :':<20}{desc.bandCount}\n")
            new_file.write(f"{'Raster Data Type :':<20}{desc.dataType}\n")
            for band in desc.children:
                new_file.write(f"{band.name}\n")
                descBand = arcpy.Describe(raster + "/" + band.name)
                new_file.write(f"{'Mean Cell Height :':<20}{descBand.meanCellHeight:<.6f}\n")
                new_file.write(f"{'Mean Cell Width :':<20}{descBand.meanCellWidth:<.5f}\n")
            new_file.write(f"{'_' * 50}\n")
        new_file.close
main()