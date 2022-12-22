import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog

from conexion_db.Pelicula_BD import guardar_pelis


class Pelicula_Administrador(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.config(bg='gray17')
        self.widgets_frame()
    

    def widgets_frame(self):
        tk.Label(self, 
            text='Cargar Pelicula',
            justify='center',
            fg='white', 
            bg='gray17', 
            font=('Tahoma', 26, 'bold')).pack(pady=(10, 30))
        #_____________________________________ Frame top _______________________________________
        frame_top = tk.Frame(self, bg='gray17')
        frame_top.pack()
        # ____________________________ Imagen de poster de una pelicula ______________________________

        frame_imagen = tk.Frame(frame_top)
        #ruta_imagen = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')]) #Seleccionar imagen de archivo
        self.imagen = Image.open('image/black_adam.jpg')
        self.imagen = self.imagen.resize((120, 170), Image.ANTIALIAS)# Reduce al tamaño dado y mejora la calidad de imagen
        self.nueva_imagen = ImageTk.PhotoImage(self.imagen)
        self.lbl_img = tk.Label(frame_imagen,image=self.nueva_imagen).pack()
        lbl_pelicula = tk.Label(frame_imagen, 
            text='Seleccione una imagen',
            bg='gray17',
            fg='white').pack()
        frame_imagen.pack()

        # _______________________________ Frame bottom _______________________________
        #______________________________________________________________________________
        frame_bottom = tk.Frame(self, bg='gray17')
        frame_bottom.pack()
        tk.Label(frame_bottom, 
            text='Nombre', 
            font=('Tahoma', 12, 'bold'),
            bg='gray17',
            fg='white').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(frame_bottom, 
            text='Genero', 
            font=('Tahoma', 12, 'bold'),
            bg='gray17',
            fg='white').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(frame_bottom, 
            text='Duración', 
            font=('Tahoma', 12, 'bold'),
            bg='gray17',
            fg='white').grid(row=2, column=0, padx=10, pady=10)


        #_____________________________ Campos de textos ________________________
        self.nombre = tk.StringVar()
        tk.Entry(frame_bottom, 
            textvariable=self.nombre, 
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30).grid(row=0, column=1, padx=10, pady=10)
        
        self.genero = tk.StringVar()
        self.combobox_seleccionar = ttk.Combobox(frame_bottom, 
            textvariable = self.genero,
            state='readonly',
            foreground='gray',
            font=('Verdana', 9, 'bold'),
            width=28,
            values=['Ciencia Ficción', 'Drama','Fantasía','Superheroes'])
        self.combobox_seleccionar.set('Seleccione género') # Muestra este valor por defecto
        self.combobox_seleccionar.grid(row=1, column=1)

      #  self.genero = tk.StringVar()
       # tk.Entry(frame_bottom, 
        #    textvariable=self.genero, 
         #   width=30).grid(row=1, column=1, padx=10, pady=10)
        
        self.duracion = tk.StringVar()
        tk.Entry(frame_bottom, 
            textvariable=self.duracion, 
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30).grid(row=2, column=1, padx=10, pady=10)
        

        #___________________________ Botones ____________________________________
        tk.Button(frame_bottom, 
            text='Cargar Pelicula',
            command= self.guardar,
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=3, column=0, padx=10, pady=30)
        
        tk.Button(frame_bottom, 
            text='Cancelar',
            command=self.cancelar,
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#f2104d",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=3, column=1, padx=10, pady=30)
    

    def cancelar(self):
        self.nombre.set('')
        self.genero.set('')
        self.duracion.set('')

        self.combobox_seleccionar.set('Seleccione género')
    
    def guardar(self):
        lista1=[self.nombre.get(), self.genero.get(), self.duracion.get()]
        guardar_pelis(lista1)
        


    