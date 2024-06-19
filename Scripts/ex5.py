# -----------------------------------------------------------------------------
# Name:        GS2110_Cursor.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
#5. Modify the previous script (save as ex5.py) to add a sql clause to order the results by POP_2000.


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

    in_table = "Cities"
    field_names = ['NAME', 'POP_2000']
    where_clause = "{0}".format("POP_2000 >=100000")
    sql_clause = [None, 'ORDER BY "POP_2000"']
    with arcpy.da.SearchCursor(in_table, field_names, where_clause, sql_clause=sql_clause ) as cursor:
        print(f"{'Name':<25}{'POP_2000'}")
        for row in cursor:
            print(f"{row[0]:<25}{row[1]}")





main()
