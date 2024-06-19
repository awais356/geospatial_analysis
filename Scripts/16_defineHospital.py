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

    #arcpy.management.DefineProjection(in_dataset, coor_system)
    ##############################
    # Step 3
    ##############################
    #output_ws = "../GDB/output.gdb/"

    ##############################
    # Step 4
    ##############################



    desc = arcpy.Describe("zip")
    print(f"The spatial refrence zip is: {desc.spatialReference.name}")

    coor_system = desc.spatialReference

    in_dataset = "hospitals"
    arcpy.management.DefineProjection(in_dataset, coor_system)
    esc = arcpy.Describe("hospitals")
    print(f"The spatial refrence of {in_dataset} is: {desc.spatialReference.name}")



main()