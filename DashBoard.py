# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: LUIS ALEJANDRO CAYCEDO VILLALOBOS
"""

# Importar librerias
import streamlit as st
import pandas as pd
import sqlite3
import os

#Definición del nombre de la App 

APP_TITLE = 'Tools And Testing - Monitoreo de Sólidos'
APP_SUB_TITLE = 'Ver 1.0 - todos los derechos reservados'

# Define el titulo de la pagina web
st.set_page_config('Tools and testing - 2023')    
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)

st.sidebar.title('Tools and Testing - 2023')
col1, col2 = st.columns(2) 

# Conectar a la base de datos
conexion = sqlite3.connect("/app/toolsandtesting/DataBase/Database.db") 
cursor = conexion.cursor()
cursor.execute(f"SELECT * FROM Info_Monitoreo")
data = c.fetchall
#pf = pd.read_sql_query('SELECT * from Info_Monitoreo', conexion)
with col1:
    st.write(conexion)    

with col2:
       st.write(data) 
    
    
    
    
if __name__ == "_main_":
    main()