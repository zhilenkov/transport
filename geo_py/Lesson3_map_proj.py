# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:45:50 2019

@author: Dmitry
"""

import geopandas as gpd

fp = "C:/Users/Dmitry/Documents/Nurmi_scripts/transport/Europe_borders/Europe_borders.shp"

data = gpd.read_file(fp)

print(data.crs)

print(data['geometry'].head())

data_proj = data.copy()

data_proj = data_proj.to_crs(epsg=3035)

data_proj['geometry'].head()

import matplotlib.pyplot as plt

data.plot(facecolor='gray')

plt.title("WGS84 projection")

plt.tight_layout()

data_proj.plot(facecolor='blue')

plt.title("ETRS Lambert Azimuthal Equal Area projection")

plt.tight_layout()

from fiona.crs import from_epsg

data_proj.crs = from_epsg(3035)

print(data_proj.crs)

from shapely.geometry import Point

hki_lon = 24.9417

hki_lat = 60.1666

proj4_txt = ('+proj=eqc +lat_ts=60 +lat_0=60.1666 +lon_0=24.9417 +x_0=0 +y_0=0' +
            ' +ellps=WGS84 +datum=WGS84 +units=m +no_defs')

data_d = data.to_crs(proj4_txt)

data_d.plot(facecolor='white')

plt.tight_layout()

hki = gpd.GeoSeries([Point(hki_lon, hki_lat)], crs=from_epsg(4326))

hki = hki.to_crs(proj4_txt)

data_d['country_centroid'] = data_d.centroid

data_d.head(2)


def calculateDistance(row, dest_geom, src_col='geometry', target_col='distance'):
    """
    Calculates the distance between a single Shapely Point geometry and a GeoDataFrame with Point geometries.

    Parameters
    ----------
    dest_geom : shapely.Point
        A single Shapely Point geometry to which the distances will be calculated to.
    src_col : str
        A name of the column that has the Shapely Point objects from where the distances will be calculated from.
    target_col : str
        A name of the target column where the result will be stored.
    """
    # Calculate the distances
    dist = row[src_col].distance(dest_geom)
    # Tranform into kilometers
    dist_km = dist/1000
    # Assign the distance to the original data
    row[target_col] = dist_km
    return row

hki_geom = hki.get(0)

print(hki_geom)

data_d = data_d.apply(calculateDistance, dest_geom=hki_geom, 
                      src_col='country_centroid', target_col='dist_to_Hki', axis=1)

data_d.plot()

max_dist = data_d['dist_to_Hki'].max()

mean_dist = data_d['dist_to_Hki'].mean()

print("Maximum distance to Helsinki is %.0f km, and the mean distance is %.0f km." % (max_dist, mean_dist))
