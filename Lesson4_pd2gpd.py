# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:14:08 2019

@author: Dmitry
"""


import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

fn = "C:/Users/Dmitry/Documents/Nurmi_scripts/transport/map.osm"
vdk = ox.core.graph_from_file(fn, bidirectional=False, simplify=True, retain_all=False, name='unnamed')

ox.plot.plot_graph(vdk)#, bbox=(43.12079, 43.11733, 131.88711, 131.87890))