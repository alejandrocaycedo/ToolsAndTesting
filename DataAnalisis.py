# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:25:25 2023

@author: ALEJANDRO
"""
import pandas as pd
import pyproj
import math

import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/DataBase.db")     #("/app/toolsandtesting/DataBase/DataBase.db")

#Conexión a los archivos de excel

# Archivo con la información de los pozos, coordenadas , Tipo, Estructura y MOP
pozos = pd.read_excel('C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/COORDENADAS.XLSX')

# Archivi con la información del monitoreo 
monitoreo = pd.read_excel('C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/Monitoreo.XLSX')

# Estructura pozos
nombre = list(pozos["NAME"])
X = list(pozos["TOPX"])
Y = list(pozos["TOPY"])
Currenttype = list(pozos["CURRENTTYPE"])
STRUCTURE= list(pozos["STRUCTURE"])
MOP = list(pozos["MOP"])

#Estructura Monitoreo
registro = list(monitoreo[""])


for nom, x, y in zip(nombre, X, Y):
     p1=pyproj.Proj(proj='utm', zone=17, ellps='WGS84', preserve_units=False)
     (lat,lon)=p1(x, y, inverse=True)
     conexion.execute("insert into Coordenadas(NamePozo,Latitud,Longitud) values(?,?,?)",(nom, lon , lat))

for nom, cur, struc, mop in zip(nombre, Currenttype, STRUCTURE, MOP):
    conexion.execute("insert into Info_Pozo(NamePozo, CurrentType, Structure, MOP) values(?,?,?,?)", (nom, cur, struc, mop))

conexion.commit()
conexion.close()




