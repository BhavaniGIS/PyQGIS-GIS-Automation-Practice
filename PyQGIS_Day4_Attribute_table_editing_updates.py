# ==============================================================================
# Title       : Day 4 - Attribute Table Editing & Batch Updates
# Description : PyQGIS script demonstrating iterator traversal (next/while),
#               dictionary-based value mapping, and safe batch attribute updates.
# ==============================================================================

# 1. Import required modules
from qgis.core import QgsProject, QgsField, edit
from PyQt5.QtCore import QVariant

# 2. Target configurations
target_layer_name = 'hyd_primary_roads'
source_field = 'highway'          # Replace with your actual column name if different
new_field_name = 'road_zone'

# Dictionary Mapping (Replaces multiple if-elif-else blocks cleanly)
category_map = {
    'primary': 'ZONE-A',
    'trunk': 'ZONE-A',
    'secondary': 'ZONE-B'
}

# 3. Access the layer from the current project
layers = QgsProject.instance().mapLayersByName(target_layer_name)

if layers:
    layer = layers[0]

    # 4. Safely open an edit session (auto-commits on exit, rolls back on error)
    with edit(layer):

        # Add new field if it does not already exist
        if new_field_name not in layer.fields().names():
            layer.addAttribute(QgsField(new_field_name, QVariant.String, len=15))
            layer.updateFields()

        target_idx = layer.fields().indexOf(new_field_name)

        # 5. Iterator + While Loop traversal (Memory-efficient alternative to 'for')
        feature_iterator = layer.getFeatures()
        updated_records = []

        while True:
            feature = next(feature_iterator, None)
            if feature is None:
                break

            raw_val = str(feature[source_field]).strip().lower()

            # Fast dictionary lookup with fallback default value
            assigned_zone = category_map.get(raw_val, 'ZONE-GENERAL')

            # Update attribute directly in the layer
            layer.changeAttributeValue(feature.id(), target_idx, assigned_zone)
            updated_records.append(feature.id())

        # 6. List Comprehension summary validation
        even_id_count = len([fid for fid in updated_records if fid % 2 == 0])
        print(f"Total records updated via iterator: {len(updated_records)}")
        print(f"Even ID features verified: {even_id_count}")

else:
    print(f"Error: Layer '{target_layer_name}' not found. Please load it in QGIS.")
