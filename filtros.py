import numpy as np
import math
from skimage import io

def contraste(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[1])
    for i in range(0, largo):
        
        for j in range(0, ancho):
            nuevo_color = 128
            color = temp[i,j]

            if (color < 128):
                nuevo_color = 0
            
            if (color > 128):
                nuevo_color = 255
            
            temp[i,j]=nuevo_color
    return temp

def umbral(imagen):
    valor_temporal =  np.copy(imagen)
    ancho = len(valor_temporal)
    largo = len(valor_temporal[0])
    valor_temporal =  np.copy(imagen)
    for i in range(ancho):
        for j in range(largo):

            nuevo_color1 = 128
            color1 = valor_temporal[i,j,0]
            if(color1 < 128):
                nuevo_color1 = 0
            if(color1 > 128):
                nuevo_color1 = 255
            valor_temporal[i,j,0] = nuevo_color1

            nuevo_color2 = 128
            color2 = valor_temporal[i,j,1]
            if(color2 < 128):
                nuevo_color2 = 0
            if(color2 > 128):
                nuevo_color2 = 255
            valor_temporal[i,j,1] = nuevo_color2

            nuevo_color3 = 128
            color3 = valor_temporal[i,j,2]
            if(color3 < 128):
                nuevo_color3 = 0
            if(color3 > 128):
                nuevo_color3 = 255
            valor_temporal[i,j,2] = nuevo_color3

def negativo(imagen):
    valor_temporal =  np.copy(imagen)
    ancho = len(valor_temporal)
    largo = len(valor_temporal[0])
    valor_temporal =  np.copy(imagen)
    for i in range(ancho):
        for j in range(largo):
            valor_temporal[i,j,0] = 255 - np.round(valor_temporal[i,j,0])
            valor_temporal[i,j,1] = 255- np.round(valor_temporal[i,j,1])
            valor_temporal[i,j,2] = 255 - np.round(valor_temporal[i,j,2])

    return valor_temporal

def logaritmica(imagen):
    valor_temporal =  np.copy(imagen)
    u = 255/math.log(256)
    ancho = len(valor_temporal)
    largo = len(valor_temporal[0])
    valor_temporal =  np.copy(imagen)
    for i in range(ancho):
        for j in range(largo):
            z0 = valor_temporal[i,j,0]
            z0cuadrado = u*math.log(z0+1)
            valor_temporal[i,j,0] = z0cuadrado

            if valor_temporal[i,j,0] > 255:
                valor_temporal[i,j,0] = 255
            if valor_temporal[i,j,0] < 0:
                valor_temporal[i,j,0] = 0

            z1 = valor_temporal[i,j,1]
            z1cuadrado = u*math.log(z1+1)
            valor_temporal[i,j,1] = z1cuadrado

            if valor_temporal[i,j,1] > 255:
                valor_temporal[i,j,1] = 255
            if valor_temporal[i,j,1] < 0:
                valor_temporal[i,j,1] = 0

            z2 = valor_temporal[i,j,2]
            z2cuadrado = u*math.log(z2+1)
            valor_temporal[i,j,2] = z2cuadrado

            if valor_temporal[i,j,2] > 255:
                valor_temporal[i,j,2] = 255
            if valor_temporal[i,j,2] < 0:
                valor_temporal[i,j,2] = 0

    return valor_temporal

def cosenoidal(imagen):

    valor_temporal =  np.copy(imagen)
    ancho = len(valor_temporal)
    largo = len(valor_temporal[0])
    valor_temporal =  np.copy(imagen)
    for i in range(ancho):
        for j in range(largo):
            z0 = valor_temporal[i,j,0]*1
            z0cuadrado = 128*(1-math.cos((math.pi*z0)/(2*128)))
            if(z0cuadrado < 0):
                z0cuadrado =0
            if(z0cuadrado > 255):
                z0cuadrado=255
            valor_temporal[i,j,0] = z0cuadrado*1

            if valor_temporal[i,j,0] > 255:
                valor_temporal[i,j,0] = 255
            if valor_temporal[i,j,0] < 0:
                valor_temporal[i,j,0] = 0

            z1 = valor_temporal[i,j,1]*1
            z1cuadrado = 128*(1-math.cos((math.pi*z1)/(2*128)))
            if(z1cuadrado < 0):
                z1cuadrado =0
            if(z1cuadrado > 255):
                z1cuadrado=255
            valor_temporal[i,j,1] = z1cuadrado*1

            if valor_temporal[i,j,1] > 255:
                valor_temporal[i,j,1] = 255
            if valor_temporal[i,j,1] < 0:
                valor_temporal[i,j,1] = 0

            z2 = valor_temporal[i,j,2]*1
            z2cuadrado = 128*(1-math.cos((math.pi*z2)/(2*128)))
            if(z2cuadrado < 0):
                z2cuadrado =0
            if(z2cuadrado > 255):
                z2cuadrado=255
            valor_temporal[i,j,2] = z2cuadrado*1

            if valor_temporal[i,j,2] > 255:
                valor_temporal[i,j,2] = 255
            if valor_temporal[i,j,2] < 0:
                valor_temporal[i,j,2] = 0

    return valor_temporal

def aclarar(imagen):
    return None

def oscurecer(imagen):
    return None

def mejorar(imagen):
    return None
