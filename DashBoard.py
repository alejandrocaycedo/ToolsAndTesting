# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: LUIS ALEJANDRO CAYCEDO VILLALOBOS
"""

# import pandas
import pandas as pd

# importar Folium
import folium
import webbrowser
from folium import plugins
from folium.plugins.marker_cluster import MarkerCluster # Agrega los puntos espaciales
from folium.plugins import HeatMap
#from folium.folium import Map
from folium.map import Marker

# importar streamlit para diagramar la APP
import streamlit as st
from streamlit_folium import st_folium



#Definición del nombre de la App 

APP_TITLE = 'Monitoreo de arrastre de sólidos - TOOLS AND TESTING'
APP_SUB_TITLE = 'Ver 1.0 - todos los derechos reservados'

# Define el titulo de la pagina web
st.set_page_config('Tools and testing - 2023')    
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)

st.sidebar.title("Consultas")
columns = st.beta_columns((3,1))
#--------------------------------------------------------------------------

#CARGA DE LOS DATOS DESDE LAS FUENTES 
#GITHUB :  RUTA /app/toolsandtesting/

#---------------------------------------------------------------------  
        #LOAD Data
pozos = pd.read_csv('/app/toolsandtesting/Pozos.csv', sep=';')

# CARGAR LOS CAMPOS DE DATOS EN LAS LISTAS
nombre = list(pozos["NamePozo"])
Latitud = list(pozos["Latitud"])
Longitud = list(pozos["Longitud"])
BWPD = list(pozos["BWPD"])
BOPD = list(pozos["BOPD"])
BFPD = list(pozos["BFPD"])
BSW = list(pozos["BSW"])
PPMp = list(pozos["PPMp"])
PPMm = list(pozos["PPMm"])
um25to45 = list(pozos["25_45um"])
um45to106 = list(pozos["45_106um"])
um106to212 = list(pozos["106_212um"])
um212to425 = list(pozos["212_425um"])
um425 = list(pozos["mayor_425um"])
color_i = list(pozos["color_icono"])
prefijo = list(pozos["Prefijo"])
#Ticono = list(pozos["icono"])

#--------------------------------------------------
# Calculo del maximo de PPMp .
#--------------------------------------------------
MaxPPMp = max(PPMp)
st.write(MaxPPMp)

#--------------------------------------------------
#  Normalización de PPMp
#--------------------------------------------------
NorPPMp = []
for i in range(len(PPMp)):
    NorPPMp.append(PPMp[i]/MaxPPMp)


#-------------------------------------------------
#  Genera los datos para el mapa de calor
#-------------------------------------------------
DataHeat = [0]
for lat, log, NorPPM in zip(Latitud, Longitud, NorPPMp):
    DataHeat.append([lat, log, NorPPM])
del DataHeat[0]

#-------------------------------------------------
# Calculos  MAP
#-------------------------------------------------
mc_pozos = MarkerCluster()
mapa = folium.Map(location = [7.10, -73.98],
                     zoom_start = 5)
#Pozos al mapa
for nomb,lat,lon, bw, bo, bf, bs, PMp, PMm, um25, um45, um106, um212, um42, col_i, pref in zip(nombre, Latitud, Longitud, BWPD, BOPD, BFPD, BSW, PPMp, PPMm, um25to45, um45to106, um106to212, um212to425, um425, color_i, prefijo):
    mc_pozos.add_child(folium.Marker(location=[float(lat),float(lon)],
    popup= "<b> Pozo: </b>" +str(nomb)+ "<br><b> PPM Promedio: <b>" +str(PMp)+"<br><b> BWPD: <b>"+str(bw)+ "<br><b> BSW: <b>"+str(bs), max_width=8000, min_width=4000,
    icon=folium.Icon(color=col_i,
    icon_color="blue",
    icon="tower-observation",
    prefix=pref)))           

capa_pozos = folium.FeatureGroup(name="pozos")
mc_pozos.add_to(capa_pozos)
mapa.add_child(capa_pozos)
HeatMap(DataHeat).add_to(mapa)

#------------------------------------------------
# Diseño visual DashBoard
#------------------------------------------------
with columns [1]:
    st.write(MaxPPMp)

with columns [0]:
    st.write("Mapa de calor, valores PPM promedio y Ubicación de los pozos ")
    st_mapa = st_folium(mapa, width=900, height=600)

    # DISPLAY METRICS

#st.write(pozos.shape)
#st.write(pozos.head())
    
    
    
    
    
    
if __name__ == "_main_":
    main()