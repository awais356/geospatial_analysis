import arcpy

def main():

    arcpy.env.workspace = "../GDB/Fields.gdb"
    arcpy.env.overwriteOutput = True

    fieldlist = arcpy.ListFields("Parks")
    for field in fieldlist:
        print(field.name)
        print(field.length)

    field_name = "Village"
    field_type = "TEXT"
    in_table= "Parks"
    if "Village" not in [f.name for f in arcpy.ListFields(in_table)]:
        arcpy.AddField_management(in_table, field_name, field_type)
    else:
        print(f"The field {field_name} Exists")



main()