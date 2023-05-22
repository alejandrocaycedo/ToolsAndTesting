# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: ALEJANDRO
"""
#Librerias
# importar Folium
import folium
import pandas as pd
#import webbrowser

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
st.write(pozos.head())

    
    # DISPLAY FILTERS AND MAP
mapa = folium.Map(location = [7.10, -73.98],
                     zoom_start = 12)
st_mapa = st_folium(mapa)
    
    # DISPLAY METRICS
    
    
    
    
    
    
    
    
if __name__ == "_main_":
    main()