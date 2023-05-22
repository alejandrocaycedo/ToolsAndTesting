# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: ALEJANDRO
"""
#Librerias
# importar Folium
from pathlib import Path
import folium
import pandas as pd
import webbrowser

from folium import plugins
from folium.plugins.marker_cluster import MarkerCluster # Agrega los puntos espaciales

#from folium.folium import Map
from folium.map import Marker

# importar streamlit para diagramar la APP
import streamlit as st
from streamlit_folium import st_folium

APP_TITLE = 'Monitoreo de arrastre de sólidos - TOOLS AND TESTING'
APP_SUB_TITLE = 'Ver 1.0 - todos los derechos reservados'

#def main():
st.set_page_config('Tools and testing - 2023')   
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)
    
    #Load Data
pozos = pd.read_csv('/app/toolsandtesting/Pozos.csv')

st.write(pozos.shape)
st.write(pozos.head())


    
    # DISPLAY FILTERS AND MAP
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
Ticono = list(pozos["icono"])

mc_pozos = MarkerCluster()
mapa = folium.Map(location = [7.10, -73.98],
                     zoom_start = 12)
#Pozos al mapa
for nomb,lat,lon, bw, bo, bf, bs, PMp, PMm, um25, um45, um106, um212, um42, col_i, pref, Tico in zip(nombre, Latitud, Longitud, BWPD, BOPD, BFPD, BSW, PPMp, PPMm, um25to45, um45to106, um106to212, um212to425, um425, color_i, prefijo, Ticono):
    mc_pozos.add_child(folium.Marker(location=[lat,lon],
    popup= "<b> Nombre: </b>" +str(nomb)+ "<br><b> PPM Promedio: <b>" +str(PMp)+"<br>", max_width=4000, min_width=4000,
    icon=folium.Icon(color=col_i,
    icon_color="blue",
    icon=Tico,
    prefix=pref)))           

capa_pozos = folium.FeatureGroup(name="pozos")
mc_pozos.add_to(capa_pozos)
mapa.add_child(capa_pozos)

st_mapa = st_folium(mapa, width=700, height=450)
    # DISPLAY METRICS
    
    
    
    
    
    
    
    
if __name__ == "_main_":
    main()