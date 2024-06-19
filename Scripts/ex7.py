# -----------------------------------------------------------------------------
# Name:        GS2110_Cursor.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------

#Use a SearchCursor and a sql clause print a report listing the DISTINCT values for the CLASSIFY
# attribute in the StParks featureclass. Order the results.

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

    in_table = "StParks"
    field_name = ['CLASSIFY']
    #where_clause = "{0}".format("CLASSIFY ='MUSEUM'")
    sql_clause = ['DISTINCT','ORDER BY "CLASSIFY"']
    with arcpy.da.SearchCursor(in_table, field_name, sql_clause=sql_clause ) as cursor:
        print("#"*40)
        print("Distinct Values for field: CLASSIFY")
        print("#" * 40)
        for row in cursor:
            print(f"{row[0]}")





main()
