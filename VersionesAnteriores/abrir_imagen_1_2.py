import PySimpleGUI as sg
import sys
import cv2
import filtros
import numpy as np
import webbrowser
##from datetime import date


def main():
    sg.theme('DarkGray15')

    menu_def = [['Archivo', ['Abrir', 'Guardar', 'Salir']],
                ['Operaciones', ['Mostrar la Imagen Original', 'Negativo', 'Logaritmica', 'Cosenoidal','Vaciar Imagen']],
                ['Filtros', [ 'Borde Gradiente','Suavizado','Disminucion del ruido','Relieve' ], ],
                ['Ayuda', ['Acerca de', 'Codigo Fuente']], ]

    layout = [
        [sg.Text('Editor de Imagenes con Python', size=(80, 1), justification='center')],
        [sg.Menu(menu_def, )],
        [sg.Image(filename='', key='-IMAGE-')]
    ]

    imagen = np.ones((550,700))
    window = sg.Window('Mi Primer editor de imagenes en Python', layout, location=(800, 400))

    while True:
        event, values = window.read(timeout=20)

        if event == 'Salir' or event == sg.WIN_CLOSED:
            sg.popup('Gracias por usar el programa')
            break

        if event == 'Imagen Original':
            try:
                imagen = cv2.imread(filename)
                sg.popup('Mostrando la imagen Original')
            except Exception:
                sg.popup('Por favor, elija una imagen')
                pass

        if event == 'Negativo':
            try:
                imagen = filtros.negativo(imagen)
                sg.popup('Mostrando la imagen Negativa')
            except Exception:
                sg.popup('Por favor, elija una imagen')
                pass

        if event == 'Logaritmica':
            try:
                imagen = filtros.logaritmica(imagen)
                sg.popup('Mostrando la imagen con filtro logaritmico')
            except Exception:
                sg.popup('Por favor, elija una imagen')
                pass

        if event == 'Cosenoidal':
            try:
                imagen = filtros.cosenoidal(imagen)
                sg.popup('Mostrando la imagen con filtro cosenoidal')
            except Exception:
                sg.popup('Por favor, elija una imagen')
                pass

        if event == 'Borde Gradiente':
            try:
                imagen = filtros.borde_gradiente(imagen)
                sg.popup('Mostrando la imagen con borde gradiente')
            except Exception:
                sg.popup('Por favor, elija una imagen')
                pass

        if event == 'Suavizado':
            try:
                imagen = filtros.suavizado(imagen)
                sg.popup('Mostrando la imagen con suavizado')
            except Exception:
                sg.popup('Por favor, elija una imagen')

        if event == 'Disminucion del ruido':
            try:
                imagen = filtros.disminucion_ruido(imagen)
                sg.popup('Mostrando la imagen con suavizado')
            except Exception:
                sg.popup('Por favor, elija una imagen')

        if event == 'Relieve':
            try:
                imagen = filtros.relieve(imagen)
                sg.popup('Mostrando la imagen con relieve')
            except Exception:
                sg.popup('Por favor, elija una imagen')

        if event == 'Acerca de':
            sg.popup('Aplicacion de Filtro de Imagenes con Python', 'Version 1.1', 'Cornbreadse7')

        if event == 'Codigo Fuente':
            webbrowser.open('https://github.com/cornbreadse7/MiPrimerEditorenPython', new=1)


        if event == 'Vaciar Imagen':
            imagen = np.ones((500, 500))

        if event == 'Abrir':
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Abrir archivo (PNG, JPG)')

            if not filename:
                sg.popup("Por favor, escoja una imagen")
            else:
                imagen = cv2.imread(filename)  # Validar que el nombre de archivo no este en blanco
                # imagen = cv2.imread("images/004.png",0)

        if event == 'Guardar':
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Guardar Fotografia (PNG) to save to', save_as=True)
            if not filename:
                sg.popup("Por favor, escoja una ruta")
            else:
                # ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
                cv2.imwrite(filename, imagen)

        imgbytes = cv2.imencode('.png', imagen)[1].tobytes()
        window['-IMAGE-'].update(data=imgbytes)

    window.close()


main()