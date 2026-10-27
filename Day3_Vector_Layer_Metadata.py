# ==============================================================================
# Title       : Day 3 - Vector Layer Metadata & Attribute Inspection
# Description : PyQGIS script to inspect geometry type, layer extent, 
#               field names, unique values, and sample attributes.
# ==============================================================================

# 1. Import required modules
from qgis.core import QgsProject, QgsWkbTypes

# 2. Target configurations (Define target layer and field names)
target_layer_name = 'traffic_bumb'
check_field = 'traffic_ca'

# 3. Access the layer from the current project
layers = QgsProject.instance().mapLayersByName(target_layer_name)

# 4. Check layer existence and extract layer metadata
if layers:
    layer = layers[0]

    # Inspect and print geometry type
    print("Geometry Type:", QgsWkbTypes.displayString(layer.wkbType()))

    # Calculate spatial bounding extent (X, Y minimum and maximum limits)
    extent = layer.extent()
    print(f"Extent X: {extent.xMinimum():.4f} to {extent.xMaximum():.4f}")
    print(f"Extent Y: {extent.yMinimum():.4f} to {extent.yMaximum():.4f}")

    # Retrieve all attribute table field names
    field_names = layer.fields().names()
    print("Field Names:", field_names)

    # Check for target field and extract distinct/unique values
    if check_field in field_names:
        idx = layer.fields().indexOf(check_field)
        print(f"Unique values in '{check_field}':", layer.uniqueValues(idx))
    else:
        print(f"Field '{check_field}' not found in this layer.")

    # Inspect attributes of the first 5 sample features
    print("\nFirst 5 features:")
    for i, feature in enumerate(layer.getFeatures()):
        if i >= 5:
            break
        print(feature.id(), feature.attributes())

# 5. Handle missing layer error
else:
    print(f"Error: Layer '{target_layer_name}' not found. Please load it in QGIS.")
