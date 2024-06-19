# -----------------------------------------------------------------------------
# Name:        GS2110_Cursor.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
# 2. Use a SearchCursor and the triple quoting method to create a where clause to print NAME, FIPS
# and SHAPE_AREA of Counties that start with a C.


# Import Modules and classes as required
import arcpy


# Main Function
def main():
    #################################
    # Step 1
    # Environment settings
    #################################
    # Set the Workspace for inputs
    # Remove unused paths
    arcpy.env.workspace = "../GDB/Florida.gdb"
    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True
    
    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    #arcpy.da.SearchCursor(in_table, field_names, {where_clause},
    # {spatial_reference}, {explode_to_points}, {sql_clause})

    ##############################
    # Step 3
    ##############################
    # For each required parameter set a variable

    ##############################
    # Step 4
    ##############################
    # fcList = arcpy.ListFeatureClasses()
    # for fc in fcList:
    #     print(fc)

    in_table = "Counties"
    field_names = ['NAME', 'FIPS','SHAPE_AREA']
    delimField = arcpy.AddFieldDelimiters(in_table, "NAME")
    #delimField + " = 'WASHINGTON' "
    with arcpy.da.SearchCursor(in_table, field_names, delimField + " = 'WASHINGTON' ") as cursor:
        print(f"{'Name':<14}{'FIPS':>10}{'SHAPE_AREA':>16}")
        for row in cursor:
            print(f"{row[0]:<20}{row[1]:<10}{row[2]:>15.2f}")





main()
