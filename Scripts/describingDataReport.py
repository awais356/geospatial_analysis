
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
    fclist = arcpy.ListFeatureClasses()

    with open("practice.txt","w") as newfile:
        for fc in fclist:
            desc = arcpy.Describe(fc)
            newfile.write(f"The baseName is: {desc.baseName}\n")
            newfile.write(f"The Spatial Refernce is: {desc.spatialReference.Name}\n")
        newfile.close()

    # # 8.Add thefollowing lines f code and run the script:
    # print(f"The baseName is: {desc.baseName}")
    # print(f"The catalogPath is: {desc.catalogPath}")
    # print(f"The dataType is: {desc.dataType}")
    # print(f"The file is: {desc.file}")
    # print(f"The name is: {desc.name}")
    # print(f"The path is: {desc.path}")
    #
    # # Question 9
    # fc_list = arcpy.ListFeatureClasses()
    # for fc in fc_list:
    #     desc = arcpy.Describe(fc)
    #     print(f" The baseName is: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"Feature Class Name: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"The baseName is: {desc.baseName}")
    #     print(f"The catalogPath is: {desc.catalogPath}")
    #     print(f"The dataType is: {desc.dataType}")
    #     print(f"The file is: {desc.file}")
    #     print(f"The name is: {desc.name}")
    #     print(f"The path is: {desc.path}")
    #
    # # 10.Add a   print   function  to print the shapeType property from the FeatureClass group.
    # # print(f"The shapetype is: {desc.shapeType}")
    # fc_list = arcpy.ListFeatureClasses()
    #
    # # Q11. Te use the extent object properties, add the following code:
    # # print(f"XMin: {desc.extent.XMin}")
    # # print(f"YMin: {desc.extent.YMin}")
    # # print(f"XMax: {desc.extent.XMax}")
    # # print(f"YMax: {desc.extent.YMax}")
    # for fc in fc_list:
    #     desc = arcpy.Describe(fc)
    #     print(f" The baseName is: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"Feature Class Name: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"The baseName is: {desc.baseName}")
    #     print(f"The catalogPath is: {desc.catalogPath}")
    #     print(f"The dataType is: {desc.dataType}")
    #     print(f"The file is: {desc.file}")
    #     print(f"The name is: {desc.name}")
    #     print(f"The path is: {desc.path}")
    #     print(f"The shapetype is: {desc.shapeType}")
    #     print(f"XMin: {desc.extent.XMin}")
    #     print(f"YMin: {desc.extent.YMin}")
    #     print(f"XMax: {desc.extent.XMax}")
    #     print(f"YMax: {desc.extent.YMax}")
    # # # Q:12
    # # print(f"The spatial refrence is: {desc.spatialReference.name}")
    # for fc in fc_list:
    #     desc = arcpy.Describe(fc)
    #     print(f" The baseName is: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"Feature Class Name: {desc.baseName}")
    #     print(40 * '#')
    #     print(f"The baseName is: {desc.baseName}")
    #     print(f"The catalogPath is: {desc.catalogPath}")
    #     print(f"The dataType is: {desc.dataType}")
    #     print(f"The file is: {desc.file}")
    #     print(f"The name is: {desc.name}")
    #     print(f"The path is: {desc.path}")
    #     print(f"The shapetype is: {desc.shapeType}")
    #     print(f"XMin: {desc.extent.XMin}")
    #     print(f"YMin: {desc.extent.YMin}")
    #     print(f"XMax: {desc.extent.XMax}")
    #     print(f"YMax: {desc.extent.YMax}")
    #     print(f"The spatial refrence is: {desc.spatialReference.name}")
    # #Q13
    #
    # with open("DescribingDataReport.txt", "w") as new_file:
    #     for fc in fc_list:
    #         new_file.write(f"#" * 40 + '\n')
    #         new_file.write(f"Feature Class Name : {fc}\n")
    #         new_file.write(f"#" * 40 + '\n')
    #         desc = arcpy.Describe(fc)
    #         new_file.write(f"The baseName is: {desc.baseName}\n")
    #         new_file.write(f"The dataType is: {desc.dataType}\n")
    #         new_file.write(f"The catalogPath is: {desc.catalogPath}\n")
    #         new_file.write(f"The file is: {desc.file}\n")
    #         new_file.write(f"The name is: {desc.name}\n")
    #         new_file.write(f"The path is: {desc.path}\n")
    #         new_file.write(f"The shapetype is: {desc.shapeType}\n")
    #         new_file.write(f"XMin: {desc.extent.XMin}\n")
    #         new_file.write(f"YMin: {desc.extent.YMin}\n")
    #         new_file.write(f"XMax: {desc.extent.XMax}\n")
    #         new_file.write(f"YMax: {desc.extent.YMax}\n")
    #         new_file.write(f"The Spatial Reference:{desc.spatialReference.name}\n")
    #     new_file.close()


main()
