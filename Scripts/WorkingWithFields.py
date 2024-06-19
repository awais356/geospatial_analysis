# -----------------------------------------------------------------------------
# Name:        workingWithFields.py
# Purpose:     GS2110
# Author:      Malik Owais Ullah Awan
# Created:     30/01/2024
# -----------------------------------------------------------------------------

# Import Modules and classes as required
import arcpy
from arcpy import env
# Main Function
def main():
    #################################
    # Step 1
    # Environment settings
    #################################
    arcpy.env.workspace = "../GDB/Fields.gdb"


    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True
    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    # ListFields (dataset, {wild_card}, {field_type})

    ##############################
    # Step 3
    ##############################
    # For each required parameter set a variable
    # Set the output path or workspace if required(not the same as inputs)
    # output_ws = "../Vector/Results/"
    # output_ws = "../GDB/GDB_OUTPUT_NAME.gdb"

    #5. Copy the listFields() function syntax from the help and add it to the script.

    #6. Add the following code in the correct section:
    in_features = "Parks"
    field_list = arcpy.ListFields(in_features)
    field_list = arcpy.ListFields(in_features)
    #7. In the Step 4 section add the following code
    for field in field_list:
        print(f"{field.name} is a type of {field.type} with a length of {field.length}")
    ##############################
    # Step 4
    ##############################
    fc_list = arcpy.ListFeatureClasses()
    for fc in fc_list:
        print(f"#" * 24)
        print(f"# {fc} Fields")
        print("#" * 24)
        field_list = arcpy.ListFields(fc)
        for field in field_list:
            print(f"{field.name} is a type of {field.type} with a length of {field.length}")
    ##############################

    # Q_9
    ##############################
    fc_list = arcpy.ListFeatureClasses()
    for fc in fc_list:
        print(f"#" * 24)
        print(f"# {fc} Fields")
        print("#" * 24)
        field_list = arcpy.ListFields(fc)
        for field in field_list:
            print(f"{field.name} is a type of {field.type} with a length of {field.length}")
        print(f"Total Fields {len(field_list)}")
main()
