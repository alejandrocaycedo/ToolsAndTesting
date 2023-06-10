# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:18:17 2023

@author: LUIS ALEJANDRO CAYCEDO VILLALOBOS
"""

# Importar librerias
import streamlit as st
import pandas as pd
#import mysql.connector
import os

# Importar projección a UTM
import pyproj

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
col1, col2 = st.columns(2) 


#---------------------------------------------------------------------------
#Definición de la fuente de datos 0: Archivos tipo CSV    1: Archivos en DB Azure
#---------------------------------------------------------------------------

ConectarDB = 0

if (ConectarDB == 0):
    pozos = pd.read_csv('/app/toolsandtesting/DataBase/COORDENADAS.csv', sep=';')
    monitoreo = pd.read_csv('/app/toolsandtesting/DataBase/Monitoreo.csv', sep=';')
    prodVolumen = pd.read_csv('/app/toolsandtesting/DataBase/PRODUCCION_Volumen.csv', sep=';')
    prodBSW = pd.read_csv('/app/toolsandtesting/DataBase/PRODUCCION_BSW.csv', sep=';')
    st.write(head(monitoreo))
else:
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
fechaMonitoreo = list(monitoreo["FechaMonitoreo"])
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

posicion = [0]
for x, y, namepozo in zip(X, Y, nombre):
    p1=pyproj.Proj(proj='utm', zone=17, ellps='WGS84', preserve_units=False)
    (lon,lat)=p1(x, y, inverse=True)
    posicion.append([namepozo, (lat - ajusteLatitud), (lon - ajusteLogitud)])

with col1:
    st.write(posicion)    

with col2:
       st.write(posicion) 
    
    
    
    
if __name__ == "_main_":
    main()