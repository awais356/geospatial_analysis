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
    #arcpy.analysis.SplitByAttributes(Input_Table, Target_Workspace, Split_Fields)
    ##############################
    # Step 3
    ##############################
    output_ws = "../GDB/output.gdb/"

    ##############################
    # Step 4
    ##############################
    Input_Table = r"C:\Data\GS2210\Skillsheets\5_GS2110_analysisToolsArgs\5_GS2110_analysisToolsArgs_Awan\GDB\analysisToolsArgs.gdb\bike_routes"
    Target_Workspace = r"C:\Data\GS2210\Skillsheets\5_GS2110_analysisToolsArgs\5_GS2110_analysisToolsArgs_Awan\GDB\analysisToolsArgs.gdb"
    Split_Fields = ['USE_RATING']
    arcpy.analysis.SplitByAttributes(Input_Table, Target_Workspace, Split_Fields)


main()