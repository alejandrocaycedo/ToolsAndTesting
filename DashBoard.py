# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: LUIS ALEJANDRO CAYCEDO VILLALOBOS
"""

# Importar librerias
import streamlit as st
import MapaCalor 
from HistoricoPozos import Func_Historico
from EstimacionesPozos import Func_Estimaciones

#Definición del nombre de la App 

APP_TITLE = 'Tools And Testing - Monitoreo de Sólidos'
APP_SUB_TITLE = 'Ver 1.0 - todos los derechos reservados'

# Define el titulo de la pagina web
st.set_page_config('Tools and testing - 2023')    
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)

#Configuración de la pagina

st.sidebar.subheader('Tipo de análisis')
page_selection = st.sidebar.selectbox('Seleccionar tipo de análisis', ['Mapa de calor Concentración de sólidos por campo', 'Historico de concentración de sólidos por pozo','Estimaciones por pozo'])
pages_main = {'Mapa de calor Concentración de sólidos por campo' : Func_MapaCalor() ,
              'Historico de concentración de sólidos por pozo' : run_Historico ,
              'Estimaciones por pozo': run_Estimaciones
    }
pages_main[page_selection]()
# abre pagina seleccionada
st.sidebar.title("Selecione análisis")

def run_MapaCalor():
    Func_MapaCalor()

def run_Historico():
    Func_Historico()
    
def run_Estimaciones():
    Func_Estimaciones()
    
    
    
    
    
    
if __name__ == "_main_":
    main()