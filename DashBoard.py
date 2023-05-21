# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: ALEJANDRO
"""
import streamlit as st
from streamlit_folium import folium
import folium

m = folium.Map (location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282],
    popup="Liberty Bell",
    tooltip="Liberty Bell"
    ).add_to(m)
st_data = st.folium(m, width = 725)
