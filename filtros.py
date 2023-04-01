import numpy as np
import math
from skimage import io
import cv2

def umbral(imagen):
    valor_temporal = np.copy(imagen)
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
    return valor_temporal

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

def borde_gradiente(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])
    for i in range(0, largo-1):
        for j in range(0, ancho-1):
            pixel_esquina = imagen[i+1, j+1,0]
            #pixel_esquina2 = imagen[i+1, j+1,1]
            #pixel_esquina3 = imagen[i+1, j+1,2]
            pixel_derecha = imagen[i+1,j,0]*1
            #pixel_derecha2 = imagen[i+1,j,1]*1
            #pixel_derecha3 = imagen[i+1,j,2]*1
            pixel_abajo = imagen[i,j+1,0]*1
            #pixel_abajo2 = imagen[i,j+1,1]*1
            #pixel_abajo3 = imagen[i,j+1,2]*1
            pixel_actual = imagen[i,j,0]*1
            #pixel_actual2 = imagen[i,j,1]*1
            #pixel_actual3 = imagen[i,j,2]*1

            derivada_h = abs(pixel_esquina - pixel_actual)
            #derivada_h2 = abs(pixel_esquina2 - pixel_actual2)
            #derivada_h3 = abs(pixel_esquina3 - pixel_actual3)
            derivada_v = abs(pixel_abajo - pixel_derecha)
            #derivada_v2 = abs(pixel_abajo2 - pixel_derecha2)
            #derivada_v3 = abs(pixel_abajo3 - pixel_derecha3)

            color = math.sqrt(derivada_h**2 + derivada_v**2)
            #color2 = math.sqrt(derivada_h2**2 + derivada_v2**2)
            #color3 = math.sqrt(derivada_h3**2 + derivada_v3**2)

            if (color > 255):
                color = 255

            #if (color2 > 255):
                #color2 = 255
            
            #if (color3 > 255):
                #color3 = 255
            
            temp[i,j] = int(color)
    return temp

def suavizado(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])

    pond = [[1,2,1],[2,4,2],[1,2,1]]

    for i in range(1, largo-1):
        for j in range(1, ancho-1):
            media0 = 0
            media1 = 0
            media2 = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    temp_canal0 = 1 / 16 * (pond[x + 1][y + 1] * imagen[i + x, j + y,0])
                    temp_canal1 = 1 / 16 * (pond[x + 1][y + 1] * imagen[i + x, j + y,1])
                    temp_canal2 = 1 / 16 * (pond[x + 1][y + 1] * imagen[i + x, j + y,2])
                    media0 = media0 + temp_canal0
                    media1 = media1 + temp_canal1
                    media2 = media2 + temp_canal2
            temp[i,j,0] = media0
            temp[i,j,1] = media1
            temp[i,j,2] = media2

    return temp

def disminucion_ruido(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])
    for i in range(1, largo - 1):
        for j in range(1, ancho - 1):
            mediana0 = []
            mediana1 = []
            mediana2 = []
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    mediana0.append(imagen[i + x, j + y,0])
                    mediana1.append(imagen[i + x, j + y,1])
                    mediana2.append(imagen[i + x, j + y,2])

            mediana0.sort()
            mediana1.sort()
            mediana2.sort()

            temp[i, j,0] = mediana0[4]
            temp[i, j,1] = mediana1[4]
            temp[i, j,2] = mediana2[4]
    return temp

def relieve(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])
    q = 127  # (256-1) /2

    for i in range(0, largo - 1):
        for j in range(0, ancho - 1):
            nuevo_pixel0 = q + abs(imagen[i, j + 1,0] * 1) - abs(imagen[i, j,0] * 1)
            nuevo_pixel1 = q + abs(imagen[i, j + 1,1] * 1) - abs(imagen[i, j,1] * 1)
            nuevo_pixel2 = q + abs(imagen[i, j + 1,2] * 1) - abs(imagen[i, j,2] * 1)


            if (nuevo_pixel0 > 255):
                nuevo_pixel0 = 255
            temp[i, j,0] = nuevo_pixel0

            if (nuevo_pixel1 > 255):
                nuevo_pixel1 = 255
            temp[i, j,1] = nuevo_pixel1

            if (nuevo_pixel2 > 255):
                nuevo_pixel2 = 255
            temp[i, j,2] = nuevo_pixel2

    return temp

def reflejo_horizontal(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])
    for i in range(0, largo):
        for j in range(0, ancho):
            temp[i, j, 0] = imagen[i, ancho - j - 1, 0]
            temp[i, j, 1] = imagen[i, ancho - j - 1, 1]
            temp[i, j, 2] = imagen[i, ancho - j - 1, 2]
    return temp

def escalado(image, escala):
    imagen_escalada = np.copy(image)
    altura, ancho, canales = image.shape
    nueva_altura = int(altura * escala)
    nuevo_ancho = int(ancho * escala)

    # Crear una matriz vacía para la imagen escalada
    imagen_escalada = np.zeros((nueva_altura, nuevo_ancho, canales), dtype=np.uint8)

    # Calcular la relación de escala inversa
    inv_escala = 1.0 / escala

    # Calcular los índices de píxel de la imagen escalada
    for i in range(nueva_altura):
        for j in range(nuevo_ancho):
            y = i * inv_escala
            x = j * inv_escala
            y1 = int(y)
            y2 = min(y1 + 1, altura - 1)
            x1 = int(x)
            x2 = min(x1 + 1, ancho - 1)
            fy = y - y1
            fx = x - x1
            # Calcular el valor del píxel interpolado
            for k in range(canales):
                p1 = image[y1, x1, k] * (1.0 - fx) + image[y1, x2, k] * fx
                p2 = image[y2, x1, k] * (1.0 - fx) + image[y2, x2, k] * fx
                imagen_escalada[i, j, k] = p1 * (1.0 - fy) + p2 * fy

    return imagen_escalada

def interrotacion(imagen, angulo):
    # Convertir el ángulo a radianes
    radianes = np.deg2rad(angulo)

    # Obtener el tamaño de la imagen original
    altura, ancho = imagen.shape[:2]

    # Calcular la matriz de transformación de rotación
    cos_theta = np.cos(radianes)
    sen_theta = np.sin(radianes)
    matriz_rot = cv2.getRotationMatrix2D((ancho / 2, altura / 2), angulo, 1)

    # Calcular los límites de la imagen rotada
    cos_theta_abs = abs(cos_theta)
    sen_theta_abs = abs(sen_theta)
    nuevo_ancho = int(altura * sen_theta_abs + ancho * cos_theta_abs)
    nueva_altura = int(altura * cos_theta_abs + ancho * sen_theta_abs)
    matriz_rot[0, 2] += (nuevo_ancho - ancho) / 2
    matriz_rot[1, 2] += (nueva_altura - altura) / 2

    # Crear la máscara con fondo transparente
    mascara = np.zeros((nueva_altura, nuevo_ancho, 3), dtype=np.uint8)
    mascara[0:altura, 0:ancho, :] = 255

    # Aplicar la matriz de transformación a la imagenn y a la máscara
    imagen_rotada = cv2.warpAffine(imagen, matriz_rot, (nuevo_ancho, nueva_altura), flags=cv2.INTER_LINEAR)
    rotated_mascara = cv2.warpAffine(mascara, matriz_rot, (nuevo_ancho, nueva_altura), flags=cv2.INTER_LINEAR)

    # Combinar la imagen rotada con la máscara para obtener el fondo transparente
    imagen_rotada = cv2.bitwise_and(imagen_rotada, rotated_mascara)

    return imagen_rotada


def reflejo_vertical(imagen):
    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[0])
    for i in range(0, largo):
        for j in range(0, ancho):
            temp[i, j, 0] = imagen[largo - i - 1, j, 0]
            temp[i, j, 1] = imagen[largo - i - 1, j, 1]
            temp[i, j, 2] = imagen[largo - i - 1, j, 2]
    return temp

def aclarar(imagen):
    return None

def oscurecer(imagen):
    return None

def mejorar(imagen):
    return None
