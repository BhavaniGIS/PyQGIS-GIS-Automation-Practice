"""
PyQGIS Day 2: Extracting Point Coordinates & Geometry
Concepts:
- Accessing geometry with feature.geometry()
- Converting geometry to QgsPointXY with geom.asPoint()
- Extracting X (Longitude) and Y (Latitude) coordinates
Dataset: Hyderabad Schools (amenity_school)
"""

from qgis.core import QgsProject

# Target layer name
target_layer_name = 'amenity_school'
layers = QgsProject.instance().mapLayersByName(target_layer_name)

if layers:
    layer = layers[0]
    print(f"Layer '{target_layer_name}' found. Extracting school coordinates...\n")
    
    # Iterate through each school point
    for feature in layer.getFeatures():
        school_name = feature['name'] if feature['name'] else "Unnamed School"
        
        # 1. Access feature geometry
        geom = feature.geometry()
        
        # 2. Check if geometry exists and is valid
        if geom and not geom.isEmpty():
            point = geom.asPoint()
            
            # 3. Extract coordinates
            x_coord = point.x()  # Longitude
            y_coord = point.y()  # Latitude
            
            print(f"School: {school_name} | Longitude (X): {x_coord:.4f}, Latitude (Y): {y_coord:.4f}")

else:
    print(f"Error: Layer '{target_layer_name}' not found. Please load it in QGIS.")
