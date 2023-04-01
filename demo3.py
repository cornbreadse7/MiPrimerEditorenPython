import PySimpleGUI as sg
import sys
import cv2
import filtros
import numpy as np
import webbrowser

def main():
    def test_display_GUI(self, mocker):
        """
        Tests that the GUI window is displayed with the correct layout and menu options.
        """
        # Mock the PySimpleGUI library functions
        mocker.patch('PySimpleGUI.theme')
        mocker.patch('PySimpleGUI.Menu')
        mocker.patch('PySimpleGUI.Text')
        mocker.patch('PySimpleGUI.Image')
        mocker.patch('PySimpleGUI.Window')

        # Call the main function
        main()

        # Assert that the PySimpleGUI functions were called with the correct arguments
        sg.theme.assert_called_once_with('DarkGray15')
        sg.Menu.assert_called_once()
        sg.Text.assert_called_once_with('Editor de Imagenes con Python', size=(80, 1), justification='center')
        sg.Image.assert_called_once_with(filename='', key='-IMAGE-')
        sg.Window.assert_called_once_with('Mi Primer editor de imagenes en Python', mocker.ANY, location=(800, 400))

        window.close()


main()