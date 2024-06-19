
# -----------------------------------------------------------------------------
# Name:        1_listingData.py
# Purpose:     starter script for GS2110
# Author:      Malik Awan
# Created:     16/01/2014
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

    arcpy.env.workspace = r"C:\Data\GS2110\Labs\2_GS2110_listingData_Awan\2_GS2110_listingData\GDB\listingData.gdb"

    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True

    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    # ListFeatureClasses({wild_card}, {feature_type}, {feature_dataset})
    # READ the help and understand each function parameter
    # Note the Return Value ie. What do you get from running the function?

    # fc_list = arcpy.ListFeatureClasses()
    # for fc in fc_list:
    #     print(fc)
    # List all feature classes in workspace starting with "bike"
    # fc_list = arcpy.ListFeatureClasses("bike*")
    # for fc in fc_list:
    #     print(fc)
    # 12. Use the copy, paste comment technique to add a new section of code to list only point featureclasses.
    # You will have to skip the wildcard argument. Run the code. The result should be featureclasses

    # List all Point feature classes in workspace
    # fc_list = arcpy.ListFeatureClasses("","Point")
    # for fc in fc_list:
    #     print(fc)
    # fc_list = arcpy.ListFeatureClasses("", "PolyLine")
    # for fc in fc_list:
    #     print(fc)
    # 15. Comment out the previous section of code and add the following code which will find
    # featureclasses that start with a z or p by performing a union on the two sets.
    # z_set = set(arcpy.ListFeatureClasses("z*"))
    # p_set = set(arcpy.ListFeatureClasses("p*"))
    # zp_list = list(z_set | p_set)
    # print(zp_list)

    # 16. Use the copy, paste comment technique to experiment with the following:find featureclasses that do not start p
    # all_set = set(arcpy.ListFeatureClasses("*"))
    # p_set = set(arcpy.ListFeatureClasses("p*"))
    # notp_list = list(all_set - p_set)
    # print(notp_list)
    ##17. Use the copy, paste comment technique to experiment with the following:
    # find featureclasses that contain both "a" and "s" in the name.

    # a_set = set(arcpy.ListFeatureClasses("*a*"))
    # s_set = set(arcpy.ListFeatureClasses("*s*"))
    # as_list = list(a_set & s_set)
    # print(as_list)
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
    # Fill-in the the blanks to complete the function
    # using your parameter variables as arguments
    # For functions that return a value use a return variable


main()
