# -*- coding: utf-8 -*-
"""
Created on Sun May 26 08:55:03 2019

@author: Dmitry
"""

"""
Установка необходимых библиотек 
https://automating-gis-processes.github.io/2017/course-info/
Installing_Anacondas_GIS.html#install-python-gis-on-windows
"""

import osmnx as ox
import matplotlib.pyplot as plt
#matplotlib inline
ox.config(log_console=True, use_cache=True)
print(ox.__version__)

place_name = 'Vladivostok, Russia'

vdk = ox.graph_from_place(place_name, simplify=True)

print(type(vdk))
#
#

