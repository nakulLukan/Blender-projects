import bpy

# Check if an object is selected
if bpy.context.active_object is None:
    print("Please select an object first.")
else:
    obj = bpy.context.active_object

    # Define property details
    prop_name = "Door Angle"
    prop_type = "INTEGER"  # Can be "INTEGER", "FLOAT", "STRING", or "BOOLEAN"
    default_value = 5
    min_value = 0
    max_value = 360

    # Check if property already exists (optional)
    if prop_name not in obj:
        # Create the custom property
        obj[prop_name] = bpy.props.IntProperty(
            name=prop_name,
            description="A custom property for this object",
            default=default_value,
            min=min_value,
            max=max_value,
            subtype=prop_type,
        )
        print(f"Custom property '{prop_name}' created for object '{obj.name}'.")
    else:
        print(f"Object '{obj.name}' already has a property named '{prop_name}'.")
