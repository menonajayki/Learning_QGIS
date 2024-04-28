import os

# Get the active layer in QGIS
layer = iface.activeLayer()

# File name for the output text file
output_file_name = 'airports.txt'

# Define the directory path for the Downloads folder
downloads_dir = os.path.expanduser('~\\Downloads')

# Combine directory path and file name to get the full output file path
output_file_path = os.path.join(downloads_dir, output_file_name)

# Open the output file in write mode
with open(output_file_path, 'w') as file:
    # Iterate over each feature in the layer
    for feature in layer.getFeatures():
        # Retrieve feature attributes
        name = feature['name']
        iata_code = feature['iata_code']

        # Retrieve feature geometry and extract coordinates
        geom = feature.geometry()
        latitude = geom.asPoint().y()
        longitude = geom.asPoint().x()

        # Write formatted data to the output file
        line = '{},{},{:.2f},{:.2f}\n'.format(name, iata_code, latitude, longitude)
        file.write(line)

# Print message indicating successful completion
print("Data extraction completed. Output saved to:", output_file_path)
