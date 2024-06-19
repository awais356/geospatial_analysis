# -----------------------------------------------------------------------------
# Name:        DescribingDataReport.py
# Purpose:     GS2110_describingData
# Author:      Malik Owais Ullah Awan
# Created:     23/01/2024
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
    arcpy.env.workspace = "../GDB/describingData.gdb/"

    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True

    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    # Descirbe(value,{datatype})

    ##############################
    # Step 3
    ##############################
    # Q7:
    in_feature = "Parks"
    desc = arcpy.Describe(in_feature)
    print(f" The baseName is: {desc.baseName}")

    # 8.Add the following lines f code and run the script:
    print(f"The baseName is: {desc.baseName}")
    print(f"The catalogPath is: {desc.catalogPath}")
    print(f"The dataType is: {desc.dataType}")
    print(f"The file is: {desc.file}")
    print(f"The name is: {desc.name}")
    print(f"The path is: {desc.path}")

    # Question 9
    fc_list = arcpy.ListFeatureClasses()
    for fc in fc_list:
        desc = arcpy.Describe(fc)
        print(f" The baseName is: {desc.baseName}")
        print(40 * '#')
        print(f"Feature Class Name: {desc.baseName}")
        print(40 * '#')
        print(f"The baseName is: {desc.baseName}")
        print(f"The catalogPath is: {desc.catalogPath}")
        print(f"The dataType is: {desc.dataType}")
        print(f"The file is: {desc.file}")
        print(f"The name is: {desc.name}")
        print(f"The path is: {desc.path}")

    # 10.Add a   print   function  to print the shapeType property from the FeatureClass group.
    # print(f"The shapetype is: {desc.shapeType}")
    fc_list = arcpy.ListFeatureClasses()

    # Q11. Te use the extent object properties, add the following code:
    # print(f"XMin: {desc.extent.XMin}")
    # print(f"YMin: {desc.extent.YMin}")
    # print(f"XMax: {desc.extent.XMax}")
    # print(f"YMax: {desc.extent.YMax}")
    for fc in fc_list:
        desc = arcpy.Describe(fc)
        print(f" The baseName is: {desc.baseName}")
        print(40 * '#')
        print(f"Feature Class Name: {desc.baseName}")
        print(40 * '#')
        print(f"The baseName is: {desc.baseName}")
        print(f"The catalogPath is: {desc.catalogPath}")
        print(f"The dataType is: {desc.dataType}")
        print(f"The file is: {desc.file}")
        print(f"The name is: {desc.name}")
        print(f"The path is: {desc.path}")
        print(f"The shapetype is: {desc.shapeType}")
        print(f"XMin: {desc.extent.XMin}")
        print(f"YMin: {desc.extent.YMin}")
        print(f"XMax: {desc.extent.XMax}")
        print(f"YMax: {desc.extent.YMax}")
    # # Q:12
    # print(f"The spatial refrence is: {desc.spatialReference.name}")
    for fc in fc_list:
        desc = arcpy.Describe(fc)
        print(f" The baseName is: {desc.baseName}")
        print(40 * '#')
        print(f"Feature Class Name: {desc.baseName}")
        print(40 * '#')
        print(f"The baseName is: {desc.baseName}")
        print(f"The catalogPath is: {desc.catalogPath}")
        print(f"The dataType is: {desc.dataType}")
        print(f"The file is: {desc.file}")
        print(f"The name is: {desc.name}")
        print(f"The path is: {desc.path}")
        print(f"The shapetype is: {desc.shapeType}")
        print(f"XMin: {desc.extent.XMin}")
        print(f"YMin: {desc.extent.YMin}")
        print(f"XMax: {desc.extent.XMax}")
        print(f"YMax: {desc.extent.YMax}")
        print(f"The spatial refrence is: {desc.spatialReference.name}")

main()
