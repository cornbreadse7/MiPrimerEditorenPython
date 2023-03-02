import PySimpleGUI as sg
import cv2
import filtros
import numpy as np
##from datetime import date

def main():      
    #sg.theme_previewer()
    sg.theme('DarkGray15')
    sg.set_options(element_padding=(0, 0))      

    # ------ Menu Definition ------ #      
    menu_def = [['Archivo', ['Abrir', 'Guardar', 'Salir'  ]],      
                ['Filtros', ['Imagen Original','Negativo','Logaritmica','Cosenoidal','Borde Gradiente'], ],      
                ['Ayuda', 'Acerca de'], ]      

    # ------ GUI Defintion ------ #      
    layout = [      
        [sg.Menu(menu_def, )], 
        [sg.Image(filename='', key='-IMAGE-')],     
        [sg.Output(size=(200, 50))]      
            ]
    imagen = np.ones((700,700))      
    window = sg.Window("Mi Primer editor de imagenes en Python", layout, default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,      
                    default_button_element_size=(12, 1)) 
    
    # ------ Loop & Process button menu choices ------ #      
    while True:      
        event, values = window.read() 

        if event == 'Abrir':
            print("Abrir imagen")
            filename = sg.popup_get_file('Abrir archivo (PNG, JPG)') # Abrir solo imagenes JPG o PNG
            imagen = cv2.imread(filename) #Validar que el nombre de archivo no este en blanco
            #imagen = cv2.imread("images/004.png",0)

        if event == 'Imagen Original':
            imagen = cv2.imread(filename)
            sg.popup('Mostrando la imagen Original')

        if event == 'Negativo':
            imagen = filtros.negativo(imagen)
            sg.popup('Mostrando la imagen Negativa')

        if event == 'Logaritmica':
            imagen = filtros.logaritmica(imagen)
            sg.popup('Mostrando la imagen con filtro logaritmico')

        if event == 'Cosenoidal':
            imagen = filtros.cosenoidal(imagen)
            sg.popup('Mostrando la imagen con filtro cosenoidal')

        if event == 'Borde Gradiente':
            imagen = filtros.borde_gradiente(imagen)
            sg.popup('Mostrando la imagen con borde gradiente')
        
        if event == 'Guardar':
            filename = sg.popup_get_file('Guardar Fotografia (PNG) to save to', save_as=True)
            #ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
            cv2.imwrite(filename, imagen)
            
        if event == 'Acerca de':      
            sg.popup('Aplicacion de Filtro de Imagenes con Python', 'Version 1.1', 'Cornbreadse7') 

        if event == 'Salir' or event == sg.WIN_CLOSED:
            sg.popup('Gracias por usar el programa')
            break
        
        imgbytes = cv2.imencode('.png', imagen)[1].tobytes()
        window['-IMAGE-'].update(data=imgbytes)
    
    window.close()


main()