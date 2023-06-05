# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:25:25 2023

@author: ALEJANDRO
"""

import pyproj
import math



p1=pyproj.Proj(proj='utm', zone=17, ellps='WGS84', preserve_units=False)
(lat,lon)=p1(1265557.88, 1032328.78, inverse=True)


def LatLon_To_XY(Lat,Lon):
    p1=pyproj.Proj(PROJ,preserve_units=True)
    (x,y)=p1(Lat,Lon)
    return(x,y)


def XY_To_LatLon(x,y):
    p1=pyproj.Proj(PROJ,preserve_units=True)
    (lat,lon)=p1(x,y,inverse=True)
    return(lat,lon)

def distance(x1,y1,x2,y2):
    d1=x1-x2
    d2=y1-y2
    out=math.sqrt(d1*d1+d2*d2)
    return(out)

