import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Visor de Imagen con Filtro Negativo")

        # Crea la barra de menú y agrega opciones
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir imagen", command=self.open_image)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=master.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Filtro negativo", command=self.negative_filter)
        menubar.add_cascade(label="Editar", menu=editmenu)
        master.config(menu=menubar)

        # Crea el lienzo para mostrar la imagen
        self.canvas = tk.Canvas(master)
        self.canvas.pack()

    def open_image(self):
        # Abre el diálogo de archivo para seleccionar una imagen
        filename = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg;*.png;*.gif;*.bmp")])
        if filename:
            # Carga la imagen y la muestra en el lienzo
            self.image = Image.open(filename)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def negative_filter(self):
        # Invierte cada píxel de la imagen
        if hasattr(self, 'image'):
            self.image = ImageOps.invert(self.image)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


root = tk.Tk()
app = App(root)
root.mainloop()
