# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:38:59 2019

@author: Dmitry
"""

import geopandas as gpd

fp = "C:/Users/Dmitry/Documents/Nurmi_scripts/transport/Data/Data/DAMSELFISH_distributions.shp"
data = gpd.read_file(fp)
print(type(data))

print(data.head())

data.plot()

out = r"C:/Users/Dmitry/Documents/Nurmi_scripts/transport/Data/Data/DAMSELFISH_distributions_SELECTION.shp"
selection = data[0:50]

print(data['geometry'].head())

selection.plot()

selection = data[0:5]

selection.plot()

for index, row in selection.iterrows():
    poly_area = row['geometry'].area
    print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))
    
   
print('data_area')
data['area'] = data.area
print(data['area'].head(2))

import pandas as pd
from shapely.geometry import Point, Polygon
import fiona

newdata = gpd.GeoDataFrame()

newdata['geometry'] = None

print(newdata)

coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]

poly = Polygon(coordinates)

newdata.loc[0, 'geometry'] = poly

print(newdata.crs)

from fiona.crs import from_epsg

newdata.crs = from_epsg(4326)

print(newdata.crs)

out = r"C:/Users/Dmitry/Documents/Nurmi_scripts/transport/Data/Data/DAMSELFISH_distributions_newdata.shp"

newdata.to_file(out)

grouped = data.groupby('BINOMIAL')

for key, values in grouped:
    individual_fish = values
    
outFolder = r"C:/Users/Dmitry/Documents/Nurmi_scripts/transport/Data/Data"

import os

resultFolder = os.path.join(outFolder, 'Results')
if not os.path.exists(resultFolder):
    os.makedirs(resultFolder)
    
for key, values in grouped:
    # Format the filename (replace spaces with underscores)
    outName = "%s.shp" % key.replace(" ", "_")

    # Print some information for the user
    print("Processing: %s" % key)

    # Create an output path
    outpath = os.path.join(resultFolder, outName)

    # Export the data
    values.to_file(outpath)
    
