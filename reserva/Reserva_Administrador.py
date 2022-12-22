import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexion_db.Reservas_Administrador_BD import buscar, lista_datos


class Reserva_Administrador(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.root = root
        self.config(background='gray17')
        self.widgets_frame()
    

    def widgets_frame(self):
        frame_top = tk.Frame(self, background='gray17')
        frame_top.pack()
        tk.Label(frame_top,
            text='Reservas de Clientes',
            bg='gray17',
            fg='white',
            font=('Tahoma', 26, 'bold')).pack(pady=(10, 30))


        tk.Label(frame_top,
            text='Buscar cliente',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack()
        self.var_buscar = tk.StringVar()
        tk.Entry(frame_top, 
            textvariable=self.var_buscar,
            width=40,
            fg='gray',
            font=('Verdana', 9, 'bold')).pack(side=tk.LEFT)
        tk.Button(frame_top, 
            text='Buscar',
            command=self.resultado,
            bg='green',
            fg='white',
            cursor='hand2', #Cambio de cursor de flecha a mano cuando se posiciona en el widgets
            activebackground='white', #Cambia color del fondo cuando se hace click
            activeforeground='green', #Cambia color de la fuente cuando se hace click
            font=('Verdana', 9, 'bold')).pack(ipady=5, padx=5, side=tk.LEFT)


        self.frame_tabla = tk.Frame(self, background='gray17')
        self.frame_tabla.pack()
        #Recuperamos la lista de datos de reservas
        lista_reservas = lista_datos()

        #Diseñando tabla
        self.tabla = ttk.Treeview(self.frame_tabla,
            column=('Pelicula', 'Cliente', 'Nro Sala', 'Fecha', 'Capacidad', 'Precio'), # Nombre de las columnas de la tabla
            height=14 #Altura de la tabla
        )
        self.tabla.grid(row=0, column=0,pady=10, columnspan=7, sticky='ns')#Ocupa 7 columnas
        
        # Scrollbar para la tabla
        self.scroll = ttk.Scrollbar(self.frame_tabla,
            orient='vertical',
            command=self.tabla.yview
        )
        self.scroll.grid(row=0, column=7, sticky='ns')
        self.tabla.config(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')#Posicion y nombre de la columna
        self.tabla.heading('#1', text='PELICULA')
        self.tabla.heading('#2', text='CLIENTE')
        self.tabla.heading('#3', text='NRO SALA')
        self.tabla.heading('#4', text='FECHA')
        self.tabla.heading('#5', text='BUTACAS')
        self.tabla.heading('#6', text='PRECIO')

        self.tabla.column('#0', anchor=tk.CENTER, width=40, stretch=tk.NO)
        self.tabla.column('#1', anchor=tk.CENTER, minwidth=0, width=300, stretch=tk.NO)
        self.tabla.column('#2', anchor=tk.CENTER)
        self.tabla.column('#3', anchor=tk.CENTER, width=70, stretch=tk.NO)
        self.tabla.column('#4', anchor=tk.CENTER, width=80, stretch=tk.NO)
        self.tabla.column('#5', anchor=tk.CENTER, width=80, stretch=tk.NO)
        self.tabla.column('#6', anchor=tk.CENTER, width=70, stretch=tk.NO)

        for reserva in lista_reservas:
            self.tabla.insert('', #Lleno tabla con los registros de la BD
                'end', 
                text=reserva[0], 
                values=(reserva[1], reserva[2], reserva[3], reserva[4], reserva[5], reserva[6]))
        
        #Al frame lo creo y lo empaqueto aqui para evitar error al mostrar resultado
        self.frame_buscar = tk.Frame(self, background='gray17', relief='sunken', borderwidth=4)
        self.frame_buscar.pack(pady=(30, 0))

    def resultado(self):
        #Obtengo todos los registros del cliente
        if self.var_buscar.get() != '':
            reservas = buscar(int(self.var_buscar.get()))
            if len(reservas) != 0:
                self.tabla.config(height=0) #Desaparece la tabla
                #Diseñando tabla
                tabla_resultado = ttk.Treeview(self.frame_tabla,
                    column=('Pelicula', 'Cliente', 'Nro Sala', 'Fecha', 'Capacidad', 'Precio'), # Nombre de las columnas de la tabla
                    height=5 #Altura de la tabla
                )
                tabla_resultado.grid(row=0, column=0,pady=10, columnspan=7, sticky='ns')#Ocupa 7 columnas
                # Scrollbar para la tabla
                scroll = ttk.Scrollbar(self.frame_tabla,
                    orient='vertical',
                    command=tabla_resultado.yview
                )
                scroll.grid(row=0, column=7, sticky='ns')
                tabla_resultado.config(yscrollcommand=scroll.set)

                tabla_resultado.heading('#0', text='ID')#Posicion y nombre de la columna
                tabla_resultado.heading('#1', text='PELICULA')
                tabla_resultado.heading('#2', text='CLIENTE')
                tabla_resultado.heading('#3', text='NRO SALA')
                tabla_resultado.heading('#4', text='FECHA')
                tabla_resultado.heading('#5', text='BUTACAS')
                tabla_resultado.heading('#6', text='PRECIO')

                tabla_resultado.column('#0', anchor=tk.CENTER, width=40, stretch=tk.NO)
                tabla_resultado.column('#1', anchor=tk.CENTER, minwidth=0, width=300, stretch=tk.NO)
                tabla_resultado.column('#2', anchor=tk.CENTER)
                tabla_resultado.column('#3', anchor=tk.CENTER, width=70, stretch=tk.NO)
                tabla_resultado.column('#4', anchor=tk.CENTER, width=80, stretch=tk.NO)
                tabla_resultado.column('#5', anchor=tk.CENTER, width=80, stretch=tk.NO)
                tabla_resultado.column('#6', anchor=tk.CENTER, width=70, stretch=tk.NO)
                
                for reserva in reservas:
                    tabla_resultado.insert('', 
                        'end', 
                        text=reserva[0], 
                        values=(reserva[1], reserva[2], reserva[3], reserva[4], reserva[5], reserva[6]))
            else: 
                messagebox.showerror('Error en Buscar', 'El cliente no esta en la base de datos')
            self.var_buscar.set('')
        else:
            messagebox.showinfo('Error en Buscar', 'Debe llenar el campo de busqueda.')
            self.root.mostrar_frame(Reserva_Administrador) #Sirve para resetear el frame
    
    
   