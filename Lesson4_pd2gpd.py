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

fn = "C:/Users/Dmitry/Documents/Nurmi_scripts/transport/map"
graph = ox.core.graph_from_file(fn, bidirectional=False, simplify=True, retain_all=False, name='unnamed')
fig, ax = ox.plot_graph(graph)