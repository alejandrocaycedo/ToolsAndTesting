# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: ALEJANDRO
"""
#Librerias
# importar Folium
import streamlit as st
from streamlit_folium import st.folium
import folium
import pandas as pd
import webbrowser

from folium import plugins
from folium.plugins.marker_cluster import MarkerCluster # Agrega los puntos espaciales

#from folium.folium import Map
from folium.map import Marker

# importar streamlit para diagramar la APP
import streamlit as st

APP_TITLE = 'DASHBOARD MONITOREO DE SOLIDOS - TOOLS AND TESTING'
APP_SUB_TITLE = 'VER 1.0'

def main():
    st.set_page_config(APP_TITLE)
    st.title('DASHBOARD MONITOREO DE SOLIDOS - TOOLS AND TESTING')
    st.caption('VER 1.0')
    
    # LOAD DATA
    # -- lee los datos del archivo de excel 
    pozos = pd.read_excel('C:/Users/ALEJANDRO/Downloads/pozos.xlsx')
    
    st.write(pozos.shape)
    st.write(pozos.Head())
    st.write(pozos.columns)
    
    # DISPLAY FILTERS AND MAP
    
    
    # DISPLAY METRICS
    
    
    
    
    
    
    
    
if __name__ == "_main_":
    main()