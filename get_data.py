# -*- coding: utf-8 -*-
"""
Created on Sun May 26 08:55:03 2019

@author: Dmitry
"""

import osmnx as ox
import matplotlib.pyplot as plt
#matplotlib inline
ox.config(log_console=True, use_cache=True)
print(ox.__version__)

melbourne = ox.gdf_from_place('Vladivostok, Russia')
melbourne = ox.project_gdf(melbourne)
fig, ax = ox.plot_shape(melbourne)