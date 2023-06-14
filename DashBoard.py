# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: LUIS ALEJANDRO CAYCEDO VILLALOBOS
"""

# Importar librerias
import streamlit as st
import pandas as pd
import numpy as np
#import mysql.connector
import os


# Importar projección a UTM
import pyproj
import math


# Folium
import folium
import webbrowser
from folium import plugins
from folium.plugins.marker_cluster import MarkerCluster # Agrega los puntos espaciales
from folium.plugins import HeatMap
#from folium.folium import Map
from folium.map import Marker
from streamlit_folium import st_folium


st.set_page_config('Tools and testing - 2023')

#---------------------------------------------------------------------------
#Estructura APP DashBoard
#--------------------------------------------------------------------------- 

APP_TITLE = 'Tools And Testing - Monitoreo de Sólidos'
APP_SUB_TITLE = 'Ver 1.0 - todos los derechos reservados'

# Define el titulo de la pagina web
    
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)

st.sidebar.title('Tools and Testing - 2023')
#col1, col2 = st.columns([0.7,0.3]) 


#---------------------------------------------------------------------------
#Definición de la fuente de datos 0: Archivos tipo CSV    1: Archivos en DB Azure
#---------------------------------------------------------------------------

ConectarDB = 0

if (ConectarDB == 0):
    pozos = pd.read_csv('/app/toolsandtesting/DataBase/COORDENADAS.csv', sep=';')
    monitoreo = pd.read_csv('/app/toolsandtesting/DataBase/Monitoreo.csv', sep=';')
    prodVolumen = pd.read_csv('/app/toolsandtesting/DataBase/PRODUCCION_Volumen.csv', sep=';')
    prodBSW = pd.read_csv('/app/toolsandtesting/DataBase/PRODUCCION_BSW.csv', sep=';')
    
else:
    import mysql.connector
    config = {
        'host': 'toolsandtestingdb.mysql.database.azure.com',
        'user': 'toolsandtesting',
        'password': "Aa94105280",
        'database':'mydatabase',
        'raise_on_warnings': True
        }
    # se realiza la conexion a la base de datos en azure. 
    conexion = mysql.connector.connect(**config)
    pf = pd.read_sql_query('SELECT * from Info_Monitoreo', conexion)


#---------------------------------------------------------------------------
#Estructuras para los datos datos 
#---------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Estructura pozos
nombre = list(pozos["NAME"])
X = list(pozos["TOPX"])
Y = list(pozos["TOPY"])
Currenttype = list(pozos["CURRENTTYPE"])
STRUCTURE= list(pozos["STRUCTURE"])
MOP = list(pozos["MOP"])

#Correccion a los valores de latitud y longitud para ajuste a coordenadas UTM coordenadas de referencia pozo 2830 Cira Barranca (lat = 6.9941 , long = -73.7666)
ajusteLogitud = -2.3408
ajusteLatitud = 4.4102


#--------------------------------------------------------------------------
#Estructura Monitoreo
pozo = list(monitoreo["POZO"])
regist = list(monitoreo["REGISTRO"])
als = list(monitoreo["ALS"])
formacion = list(monitoreo["FORMACION"])
area = list(monitoreo["AREA"])
#fechaMonitoreo = list(str(monitoreo["FechaMonitoreo"]))
bwpd = list(monitoreo["BWPD"]) 
bopd = list(monitoreo["BOPD"])
bfpd = list(monitoreo["BFPD"])
bsw = list(monitoreo["BSW"])
PPMaverage = list(monitoreo["PPMaverage"])
PPMmax = list(monitoreo["PPMmax"])
p25to45 = list(monitoreo["P25to45"])
p45to106 = list(monitoreo["P45to106"])
p106to250 = list(monitoreo["P106to250"])
p250to425 = list(monitoreo["P250to425"])
pm425 = list(monitoreo["PM425"])
cuadrilla = list(monitoreo["CUADRILLA"])

#----------------------------------------------------------------------------
# estructura produccion Volumen
Vpozo = list(prodVolumen["POZO"])
Vfecha = list(prodVolumen["FECHA"])
VBFD = list(prodVolumen["BFD"])
Vtipo =list(prodVolumen["TIPO"])

# estructura produccion BSW
BSWpozo = list(prodBSW["POZO"])
BSWfecha = list(prodBSW["FECHA"])
BSWbsw = list(prodBSW["BSW"])

# End estrucutras


#-----------------------------------------------------------------------------
# Convertir coordenadas a UTM
#-----------------------------------------------------------------------------
lon = 0
lat = 0
Snombre = [0]
Slatitud = [0]
Slongitud = [0]
for x, y, namepozo in zip(X, Y, nombre):
    p1 = pyproj.Proj(proj='utm', zone=17, ellps='WGS84', preserve_units=False)
    (lon,lat)=p1(x, y, inverse=True)  
    Snombre.append(namepozo)
    Slatitud.append(float(lat - ajusteLatitud))
    Slongitud.append(float(lon - ajusteLogitud))
del Snombre[0]
del Slatitud[0]
del Slongitud[0]

namep = list(Snombre)
lati = list(Slatitud)
longi = list(Slongitud)
#st.write(*namep , *lati, *longi)




# dashboard
#with col1:
mc_pozos = MarkerCluster()
mapa = folium.Map(location = [6.8, -73.8],
                     zoom_start = 5)
#Pozos al mapa
for nomb,lat,lon in zip(namep, lati, longi):
    mc_pozos.add_child(folium.Marker(location=[float(lat),float(lon)],
    popup= "<b> Pozo: </b> " +str(nomb) , max_width=14000, min_width=10000,
    icon=folium.Icon("green",
    icon_color="blue",
    icon="tower-observation",
    prefix='fa')))           
   
capa_pozos = folium.FeatureGroup(name="pozos")
mc_pozos.add_to(capa_pozos)
mapa.add_child(capa_pozos)
#st.write("Mapa de calor, valores PPM promedio y Ubicación de los pozos ")
st_mapa = st_folium(mapa, width=1200, height=500)
     
#with col2:
    # calcula el promedio , maximo y minimo del PPMaverage y BSW 
monitoreo_average = monitoreo.groupby(['POZO'])[['PPMaverage','BSW']].mean()
monitoreo_max = monitoreo.groupby(['POZO'])[['PPMaverage','BSW']].max()
monitoreo_min = monitoreo.groupby(['POZO'])[['PPMaverage','BSW']].min()   

monitoreo.plot()
    
    
if __name__ == "_main_":
    main()
