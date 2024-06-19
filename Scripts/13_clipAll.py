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
    output_ws = "../GDB/output.gdb/"


    ##############################
    # Step 4
    ##############################

    all = set(arcpy.ListFeatureClasses())
    zipfc = set(arcpy.ListFeatureClasses("zip*"))
    fc_list = list(all-zipfc)
    print(fc_list)
    clip_features = "zip"


    for fc in fc_list:
        in_features = fc
        out_feature_class = output_ws + "clip_" + fc
        print(f"Processing {fc}")
        #sanity check
        #print(fc, clip_features, output_ws + "clip_" + fc)
        arcpy.analysis.Clip(in_features, clip_features, out_feature_class)
    # print messages
    # print(arcpy.GetMessages(0))
    # last message print
    msg_count = arcpy.GetMessageCount()
    print(arcpy.GetMessages(msg_count - 1))


main()
