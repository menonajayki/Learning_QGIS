import os
from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsProject

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File name for the input text file
input_file_name = 'airports.txt'

# Combine directory path and file name to get the full input file path
input_file_path = os.path.join(script_dir, input_file_name)

# Define field names for attributes
field_names = ['name', 'iata_code', 'latitude', 'longitude']

# Create a new point layer
crs = QgsProject.instance().crs()
layer = QgsVectorLayer('Point?crs=' + crs.authid(), 'Airports', 'memory')
provider = layer.dataProvider()

# Add attribute fields to the layer
fields = []
for field_name in field_names:
    field = QgsField(field_name, QVariant.String)
    fields.append(field)

provider.addAttributes(fields)
layer.updateFields()

# Open the input file and read data
with open(input_file_path, 'r') as file:
    for line in file:
        # Parse the line and extract attributes
        name, iata_code, latitude, longitude = line.strip().split(',')

        # Create a new feature (point)
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(longitude), float(latitude))))
        feature.setAttributes([name, iata_code, latitude, longitude])

        # Add the feature to the layer
        provider.addFeature(feature)

# Add the layer to the map
QgsProject.instance().addMapLayer(layer)

# Save the layer as a shapefile
output_shapefile_path = os.path.join(script_dir, 'airports.shp')
QgsVectorFileWriter.writeAsVectorFormat(layer, output_shapefile_path, 'utf-8', layer.crs(), 'ESRI Shapefile')

print("Shapefile created successfully:", output_shapefile_path)
