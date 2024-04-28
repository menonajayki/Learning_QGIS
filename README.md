# QGIS Python Project

How to use Python scripting in QGIS to extract data from a shapefile and save it to a text file, as well as how to create a shapefile from a text file.

## How to Use (Extracting Data from Shapefile to Text File)

1. **Download the airports shapefile**: Download the airports shapefile from [Natural Earth](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/airports/).

2. **Load the shapefile in QGIS**: Open QGIS and load the airports shapefile.

3. **Execute the Python script**: Open the Python console (Plugins -> Python Console) and execute the provided Python script `readData.py`.

4. **Check the output file**: Check the root directory for the generated `airports.txt` file containing airport data.

## How to Use (Creating Shapefile from Text File)

1. **Prepare the input text file**: Create a text file named `airports.txt` with each line containing airport data in the format `name,iata_code,latitude,longitude`. For example:

2. **Execute the Python script**: Open new python file in the console and run `writeData.py`. This script will read data from the `airports.txt` file and create a new shapefile containing airport points.

3. **Check the output shapefile**: Check the root directory for the generated shapefile named `airports.shp`.
