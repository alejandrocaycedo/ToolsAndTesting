# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:25:25 2023

@author: ALEJANDRO
"""

import pyproj
import math

import sqlite3


conexion = sqlite3.connect("/app/toolsandtesting/DataBase/DataBase.db")
conexion.execute("insert into Coordenadas(NamePozo,Latitud,Longitud) values(?,?)",("Prueba", 11 , -74))
conexion.commit()
conexion.close()

p1=pyproj.Proj(proj='utm', zone=17, ellps='WGS84', preserve_units=False)
(lat,lon)=p1(1265557.88, 1032328.78, inverse=True)


