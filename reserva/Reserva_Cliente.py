import tkinter as tk
from tkinter import ttk
from conexion_db.Reservas_Cliente_BD import lista_datos

from pelicula.Pelicula_Administrador import Pelicula_Administrador


class Reserva_Cliente(tk.Frame): # Muestra la reservas de un cliente si tiene y si inicio sesion
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.config(background='gray17')

        self.widgets_frame()
    

    def widgets_frame(self):
        tk.Label(self,
            text='Mis Reservas',
            font=('Tahoma', 26, 'bold'),
            bg='gray17',
            fg='white').pack(pady=(20, 30))



        frame_tabla = tk.Frame(self, background='gray17')
        frame_tabla.pack()

        ##################

        #Diseñando tabla
        self.tabla = ttk.Treeview(frame_tabla,
            column=('Pelicula', 'Nro Sala', 'Butacas', 'Fecha', 'Genero', 'Duracion'), # Nombre de las columnas de la tabla
            height=15
        )
        self.tabla.grid(row=1, column=0,pady=6, columnspan=7, sticky='ns')#Ocupa 7 columnas
        
        # Scrollbar para la tabla si exede 10 registros
        scroll = ttk.Scrollbar(frame_tabla,
            orient='vertical',
            command=self.tabla.yview
        )
        scroll.grid(row=1, column=7, sticky='ns')
        self.tabla.config(yscrollcommand=scroll.set)

        self.tabla.heading('#0', text='ID')#Posicion y nombre de la columna
        self.tabla.heading('#1', text='PELICULA')
        self.tabla.heading('#2', text='NRO SALA')
        self.tabla.heading('#3', text='BUTACAS')
        self.tabla.heading('#4', text='FECHA')
        self.tabla.heading('#5', text='GENERO')
        self.tabla.heading('#6', text='DURACION')

        self.tabla.column('#0', anchor=tk.CENTER, width=50, stretch=tk.NO)# stretch evita que las columnas se agranden
        self.tabla.column('#1', anchor=tk.CENTER, width=340, stretch=tk.NO)
        self.tabla.column('#2', anchor=tk.CENTER, width=70, stretch=tk.NO)
        self.tabla.column('#3', anchor=tk.CENTER, width=70, stretch=tk.NO)
        self.tabla.column('#4', anchor=tk.CENTER, width=60, stretch=tk.NO)
        self.tabla.column('#5', anchor=tk.CENTER, stretch=tk.NO)
        self.tabla.column('#6', anchor=tk.CENTER, width=70, stretch=tk.NO)

        # for r in mis_reservas:
        #     self.tabla.insert('', #Inserto los valores de los registros de la tabla de base de datos
        #         'end', 
        #         text=r[0], 
        #         values=(r[1], r[2], r[3], r[4], r[5], r[6]))
        

        frame_boton = tk.Frame(self, background='gray17')
        frame_boton.pack(pady=25)

        #___________________________ Botones ____________________________________
        tk.Button(frame_boton, 
            text='Modificar',
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=1, column=3, padx=10, pady=10)
        
        tk.Button(frame_boton, 
            text='Eliminar',
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#f2104d",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=1, column=4, padx=10, pady=10)
    #
        