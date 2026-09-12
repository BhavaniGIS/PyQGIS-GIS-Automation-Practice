"""
PyQGIS Day 1: Basic Commands & Layer Access
Concepts:
- Fetching active layers from QgsProject
- Iterating features with .getFeatures()
- Attribute filtering and data extraction
Dataset: Hyderabad Fuel Stations (amenity_fuel_hyd)
"""

from qgis.core import QgsProject

# Define target vector layer name
target_layer_name = 'amenity_fuel_hyd'

# Fetch matching layers from active QGIS project
layers = QgsProject.instance().mapLayersByName(target_layer_name)

if len(layers) > 0:
    layer = layers[0]
    named_fuels = []
    
    # Iterate through features and collect valid names
    for feature in layer.getFeatures():
        if feature['name']:
            named_fuels.append(feature['name'])
            
    print(f"Layer '{target_layer_name}' loaded successfully.")
    print("Named Fuel stations Count:", len(named_fuels))
else:
    print(f"Error: Layer '{target_layer_name}' not found. Please ensure the layer is loaded in the project.")
