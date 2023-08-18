# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:25:25 2023

Procedimiento para cargar los datos desde archivos de excel a la base de datos

Archivos de excel:
    1. COORDENADAS.XLSX
    2. Monitoreo.XLSX
    3. PRODUCCION sheet_name='VOLUMEN'
    4. PRODUCCION sheet_name='BSW'
    
Base de datos:
    DataBase.db
    
@author: ALEJANDRO
"""
import pandas as pd
import pyproj
import math

import sqlite3


# ------------------------------------------------------
# Conexión a la base de datos
# ------------------------------------------------------
conexion = sqlite3.connect(
    "C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/DataBase.db"
)  # ("/app/toolsandtesting/DataBase/DataBase.db")

# Conexión a los archivos de excel

# Archivo con la información de los pozos, coordenadas , Tipo, Estructura y MOP
pozos = pd.read_excel(
    "C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/COORDENADAS.XLSX"
)

# Estructura pozos
nombre = list(pozos["NAME"])
X = list(pozos["TOPX"])
Y = list(pozos["TOPY"])
Currenttype = list(pozos["CURRENTTYPE"])
STRUCTURE = list(pozos["STRUCTURE"])
MOP = list(pozos["MOP"])

# Correccion a los valores de latitud y longitud para ajuste a coordenadas UTM coordenadas de referencia pozo 2830 Cira Barranca (lat = 6.9941 , long = -73.7666)
ajusteLogitud = -2.3408
ajusteLatitud = 4.4102

# Archivo con la información del monitoreo
monitoreo = pd.read_excel(
    "C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/Monitoreo.XLSX"
)

# Estructura Monitoreo
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

# Archivo con la información del pozo producción
prodVolumen = pd.read_excel(
    "C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/PRODUCCION.XLSX",
    sheet_name="VOLUMEN",
)
prodBSW = pd.read_excel(
    "C:/Users/ALEJANDRO/Documents/GitHub/ToolsAndTesting/DataBase/PRODUCCION.XLSX",
    sheet_name="BSW",
)

# estructura produccion Volumen
Vpozo = list(prodVolumen["POZO"])
Vfecha = list(prodVolumen["FECHA"])
VBFD = list(prodVolumen["BFD"])
Vtipo = list(prodVolumen["TIPO"])

# estructura produccion BSW
BSWpozo = list(prodBSW["POZO"])
BSWfecha = list(prodBSW["FECHA"])
BSWbsw = list(prodBSW["BSW"])

# escribir en la base de datos la tabla Info_Produccion
for Vpoz, Vfec, Vbf, Vtip in zip(Vpozo, Vfecha, VBFD, Vtipo):
    conexion.execute(
        "insert into Info_Produccion(NamePoz, Fecha, BFPD, Tipo) values(?,?,?,?)",
        (Vpoz, str(Vfec), Vbf, Vtip),
    )

# escribir en la base de datos la tabla Info_BSW
for BSWpoz, BSWfec, BSWbs in zip(BSWpozo, BSWfecha, BSWbsw):
    conexion.execute(
        "insert into Info_BSW(NamePoz, Fecha, BSW) values(?,?,?)",
        (BSWpoz, str(BSWfec), BSWbs),
    )

# escribir en la base de datos la tabla Coordenadas
for nom, x, y in zip(nombre, X, Y):
    p1 = pyproj.Proj(proj="utm", zone=17, ellps="WGS84", preserve_units=False)
    (lon, lat) = p1(x, y, inverse=True)
    conexion.execute(
        "insert into Coordenadas(NamePoz,Latitud,Longitud) values(?,?,?)",
        (nom, (lat - ajusteLatitud), (lon - ajusteLogitud)),
    )

# escribir en la base de datos la tabla Info_Pozo
for nom, cur, struc, mop in zip(nombre, Currenttype, STRUCTURE, MOP):
    conexion.execute(
        "insert into Info_Pozo(NamePozo, CurrentType, Structure, MOP) values(?,?,?,?)",
        (nom, cur, struc, mop),
    )

# escribir en la base de datos la tabla Info_Monitoreo
for (
    regi,
    poz,
    al,
    form,
    are,
    fecham,
    bw,
    bo,
    bf,
    bs,
    Paverage,
    Pmax,
    pu25,
    pu45,
    pu106,
    pu250,
    pu425,
    cuadri,
) in zip(
    regist,
    pozo,
    als,
    formacion,
    area,
    fechaMonitoreo,
    bwpd,
    bopd,
    bfpd,
    bsw,
    PPMaverage,
    PPMmax,
    p25to45,
    p45to106,
    p106to250,
    p250to425,
    pm425,
    cuadrilla,
):
    conexion.execute(
        "insert into Info_Monitoreo(REGISTROTYT, NamePoz, ALS, Formacion, AREA, FechaMonitoreo, BWPD, BOPD, BFPD, BSW, PPMaverage, PPMmax, P25to45, P45to106, P106to250, P250to425, PM425, Cuadrilla) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
            regi,
            poz,
            al,
            form,
            are,
            str(fecham),
            bw,
            bo,
            bf,
            bs,
            Paverage,
            Pmax,
            pu25,
            pu45,
            pu106,
            pu250,
            pu425,
            cuadri,
        ),
    )

# conexion.execute('DELETE FROM Coordenadas;'); # borrar la informacion de una tabla de la base de datos
# actualizar la base de datos
conexion.commit()


# cerrar la conexion a la base de datos
conexion.close()
