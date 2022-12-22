import tkinter as tk
from tkinter import ttk

from conexion_db.Pelicula_BD import get_nombres
from conexion_db.Sala_BD import guardar_sala

class Sala_Administrador(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.config(bg='gray17')
        self.widgets_frame()
    
    def widgets_frame(self):

        tk.Label(self,
            text='Crear Sala',
            bg='gray17',
            fg='white',
            font=('Tahoma', 26, 'bold')).pack(pady=(10, 30))


        frame_1 = tk.Frame(self, background='gray17')
        frame_1.pack()
        tk.Label(frame_1,
            text='Seleccionar Pelicula',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Nro de Sala',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).grid(row=1, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Fecha',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).grid(row=2, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Capacidad',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).grid(row=3, column=0, padx=10, pady=10)

        
        #_________________________________ Campos de texto ___________________________________
        self.var_pelicula = tk.StringVar()
        self.combobox_seleccionar = ttk.Combobox(frame_1, 
            textvariable = self.var_pelicula,
            state='readonly',
            width=38,
            foreground='gray',
            font=('Verdana', 9, 'bold'),
            values=get_nombres())
        self.combobox_seleccionar.set('Seleccione la pelicula') # Muestra el primer nombre de la lista por defecto
        self.combobox_seleccionar.grid(row=0, column=1)
        
        self.var_nro_sala = tk.StringVar()
        tk.Entry(frame_1, 
            textvariable=self.var_nro_sala,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=40).grid(row=1, column=1, padx=10, pady=10)
        
        self.var_fecha = tk.StringVar()
        tk.Entry(frame_1, 
            textvariable=self.var_fecha,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=40).grid(row=2, column=1, padx=10, pady=10)
        
        self.var_capacidad = tk.StringVar()
        tk.Entry(frame_1, 
            textvariable=self.var_capacidad,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=40).grid(row=3, column=1, padx=10, pady=10)



        frame_2 = tk.Frame(self, background='gray17')
        frame_2.pack(pady=(20, 0))
        #___________________________ Botones ____________________________________
        tk.Button(frame_2, 
            text='Crear Sala',
            command=self.crear_sala,
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=0, column=0, padx=10, pady=10)
        
        tk.Button(frame_2, 
            text='Cancelar',
            command=self.cancelar,
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#f2104d",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=0, column=1, padx=10, pady=10)
    

    def crear_sala(self):
        guardar_sala([
            self.var_pelicula.get(),
            self.var_nro_sala.get(),
            self.var_fecha.get(),
            self.var_capacidad.get()
        ])
    
    def cancelar(self):
        self.var_pelicula.set(get_nombres()[0])
        self.var_nro_sala.set('')
        self.var_fecha.set('')
        self.var_capacidad.set('')

        self.combobox_seleccionar.set('Seleccione la pelicula')
