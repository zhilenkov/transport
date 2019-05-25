# -*- coding: utf-8 -*-
"""
Created on Sun May 26 08:55:03 2019

@author: Dmitry
"""

import mercantile

west = 100.393
south = 50.986
east = 111.182
north = 56.559
zoom = 5 # для начала нам хватит зума поменьше, чтобы не сильно нагружать osm

tiles = list(mercantile.tiles(west, south, east, north, zoom))
print(tiles)