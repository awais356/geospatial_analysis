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
    #arcpy.analysis.Select(in_features, out_feature_class, where_clause)
    ##############################
    # Step 3
    ##############################
    output_ws = "../GDB/output.gdb/"

    ##############################
    # Step 4
    ##############################
    in_features = "bike_routes"
    out_feature_class = output_ws + in_features + "_highUse"
    where_clause = "USE_RATING = 'H'"
    arcpy.analysis.Select(in_features, out_feature_class, where_clause)


main()