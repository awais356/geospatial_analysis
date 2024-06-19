# -----------------------------------------------------------------------------
# Name:        templateScript.py
# Purpose:     starter script for GS2110
# Author:      rick.wheeler
# Created:     28/01/2014
# -----------------------------------------------------------------------------

# Import Modules and classes as required
import arcpy


# Main Function
def main():
    #################################
    # Step 1
    # Environment settings
    #################################

    arcpy.env.workspace = "../GDB/analysisToolsArgs.gdb"

    arcpy.env.overwriteOutput = True
    
    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    # arcpy.analysis.Clip(in_features, clip_features,
    # out_feature_class, {cluster_tolerance})


    ##############################
    # Step 3
    ##############################
    # For each required parameter set a variable
    # Set the output path or workspace if required
    # Note the trailing /
    output_ws = "../GDB/output.gdb/"

    in_features = "bike_routes"
    clip_features = "zip"
    prefix = "clip_"

    # method 1
    # out_feature_class = output_ws + "clip_" + in_features
    #method 2
    out_feature_class = output_ws + prefix + in_features

    ##############################
    # Step 4
    ##############################
    # Fill-in the the blanks to complete the function
    # using your parameter variables as arguments
    # For functions that return a value use a return variable
    arcpy.analysis.Clip(in_features, clip_features, out_feature_class)
    #print messages
    # print(arcpy.GetMessages(0))
    #last message print
    msg_count = arcpy.GetMessageCount()
    print(arcpy.GetMessages(msg_count-1))




main()
