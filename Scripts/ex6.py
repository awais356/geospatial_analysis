# -----------------------------------------------------------------------------
# Name:        GS2110_Cursor.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
#Use a SearchCursor and the escape quotes quoting method to create a where clause to print
# SITE_NAME, COUNTY and CLASSIFY for StParks with a CLASSIFY value = MUSEUM. Use a sql
# clause to order the results by COUNTY.


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
    field_names = ['SITE_NAME', 'COUNTY','CLASSIFY']
    where_clause = "{0}".format("CLASSIFY ='MUSEUM'")
    sql_clause = [None, 'ORDER BY "COUNTY"']
    with arcpy.da.SearchCursor(in_table, field_names, where_clause, sql_clause=sql_clause ) as cursor:
        print(f"{'SITE_NAME':<59}{'COUNTY':<20}{'CLASSIFY':<20}")
        for row in cursor:
            print(f"{row[0]:<60}{row[1]:<20}{row[2]:<20}")





main()
