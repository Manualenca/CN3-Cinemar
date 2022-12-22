import tkinter as tk
from tkinter import ttk
from conexion_db.Login_BD import admin, estado_sesion, iniciar_sesion

from conexion_db.Reservas_Cliente_BD import lista_datos, lista_datos1


class Pelicula_Cliente(tk.Frame): #Para comprar boletos par ver una funcion
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.root = root
        self.config(background='gray17')

        self.widgets_frame()
    

    def widgets_frame(self):
        tk.Label(self,
            text='Peliculas',
            font=('Tahoma', 26, 'bold'),
            bg='gray17',
            fg='white').pack(pady=(20, 30))



        frame_tabla = tk.Frame(self, background='gray17')
        frame_tabla.pack()

        #Obtenemos los registros
        lista = lista_datos1()

        #Diseñando tabla
        self.tabla = ttk.Treeview(frame_tabla,
            column=('Pelicula', 'Genero', 'Duracion'),
            #column=('Pelicula', 'Nro Sala', 'Butacas', 'Fecha', 'Genero', 'Duracion'), # Nombre de las columnas de la tabla
            height=15
        )
        self.tabla.grid(row=1, column=0,pady=6, columnspan=7, sticky='ns')#Ocupa 7 columnas
        
        # Scrollbar para la tabla
        scroll = ttk.Scrollbar(frame_tabla,
            orient='vertical',
            command=self.tabla.yview
        )
        scroll.grid(row=1, column=7, sticky='ns')
        self.tabla.config(yscrollcommand=scroll.set)

        self.tabla.heading('#0', text='ID')#Posicion y nombre de la columna
        self.tabla.heading('#1', text='PELICULA')
       # self.tabla.heading('#2', text='NRO SALA')
       # self.tabla.heading('#3', text='BUTACAS')
       # self.tabla.heading('#4', text='FECHA')
        self.tabla.heading('#2', text='GENERO')
        self.tabla.heading('#3', text='DURACION')

        self.tabla.column('#0', anchor=tk.CENTER, width=50, stretch=tk.NO)# stretch evita que las columnas se agranden
        self.tabla.column('#1', anchor=tk.CENTER, width=290, stretch=tk.NO)
        self.tabla.column('#2', anchor=tk.CENTER, width=100, stretch=tk.NO)
        self.tabla.column('#3', anchor=tk.CENTER, width=70, stretch=tk.NO)
       # self.tabla.column('#4', anchor=tk.CENTER, width=60, stretch=tk.NO)
       # self.tabla.column('#5', anchor=tk.CENTER, stretch=tk.NO)
       # self.tabla.column('#6', anchor=tk.CENTER, width=70, stretch=tk.NO)

        for pelicula in lista:
            self.tabla.insert('', #Inserto los valores de los registros de la tabla de base de datos
                'end', 
                text=pelicula[0], #Es ID
                #Los campos de la tabla de BD
                values=(pelicula[1], pelicula[2], pelicula[3])) # pelicula[4], pelicula[5], pelicula[6]))
        

        self.frame_compra = tk.Frame(self, background='gray17')
        self.frame_compra.pack()
        
        ############################################################################################
        ############################################################################################
        #Para evitar que el administrador pueda comprar boletos y solo vea las peliculas disponibles
        if not admin('admin2590'):
            self.frame_uno()
            self.frame_dos()
            self.frame_tres()
            self.frame_cuatro()
            self.frame_botones()

            self.tabla.bind('<ButtonRelease-1>', self.seleccion)
        ############################################################################################
        ############################################################################################


    def seleccion(self, event):
        item = self.tabla.identify('item', event.x, event.y) #Obtengo un valor hexadecimal de la fila/registro
        
        if self.tabla.item(item, 'text') != '':#Si se hace click en la cabecera item es igual a '' (vacio)
            self.tabla.config(height=5)
            self.frame_1.pack(side=tk.LEFT, padx=15)
            self.frame_2.pack(side=tk.LEFT, padx=30)
            self.frame_3.pack(side=tk.LEFT, padx=30)
            self.frame_4.pack(side=tk.LEFT, padx=15)
            
            self.lbl_pelicula.config(text=self.tabla.item(item, 'values')[0])#Obtengo los valores de una fila y columna
            id_peli = int(self.tabla.item(item, 'text'))
            
           # nom_peli = self.tabla.item(item, 'values')[0]
            #print (id_peli)
            self.lbl_genero.config(text=self.tabla.item(item, 'values')[2])

            self.lbl_duracion.config(text=self.tabla.item(item, 'values')[3])

            self.lbl_sala.config(text=self.tabla.item(item, 'values')[1])
            self.lbl_precio.config(text='$ 250')

            self.lbl_subtotal.config(text='$ 570')
            self.lbl_descuento.config(text='$ 70')
            self.lbl_total.config(text='$ 500')

            self.frame_boton.pack(pady=30)
    
    
    def frame_uno(self):
        self.frame_1 = tk.Frame(self.frame_compra, background='gray17')
        
        tk.Label(self.frame_1,
            text='Pelicula',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack()
        self.lbl_pelicula = tk.Label(self.frame_1,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_pelicula.pack()
        

        tk.Label(self.frame_1,
            text='Género',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(20, 0))
        self.lbl_genero = tk.Label(self.frame_1,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_genero.pack()
        

        tk.Label(self.frame_1,
            text='Duración',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(20, 0))
        self.lbl_duracion = tk.Label(self.frame_1,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_duracion.pack()
    
    def frame_dos(self):
        self.frame_2 = tk.Frame(self.frame_compra, background='gray17')
        
        tk.Label(self.frame_2,
            text='Sala',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack()
        self.lbl_sala = tk.Label(self.frame_2,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_sala.pack()


        tk.Label(self.frame_2,
            text='Butacas',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(20, 0))
        self.var_butaca = tk.StringVar()
        lista_butacas = ['1', '2', '3', '4']
        cbbx_butaca = ttk.Combobox(self.frame_2, 
            textvariable = self.var_butaca,
            state='readonly',
            width=10,
            values=lista_butacas)
        cbbx_butaca.set(lista_butacas[0]) #Muestro el primer valor de la lista
        cbbx_butaca.pack()

        tk.Label(self.frame_2,
            text='Precio',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(20, 0))
        self.lbl_precio = tk.Label(self.frame_2,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_precio.pack()

    def frame_tres(self):
        self.frame_3 = tk.Frame(self.frame_compra, background='gray17')

        tk.Label(self.frame_3,
            text='Fecha',
            bg='gray17',
            fg='white',
            font=('Tahoma', 16, 'bold')).pack()

        tk.Label(self.frame_3,
            text='Día',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(15, 0))
        self.var_dia = tk.StringVar()
        cbbx_dia = ttk.Combobox(self.frame_3, 
            textvariable = self.var_dia,
            state='readonly',
            width=15,
            values=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
        cbbx_dia.set(cbbx_dia['values'][0]) #Muestro el primer valor por defecto
        cbbx_dia.pack()

        tk.Label(self.frame_3,
            text='Hora',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack(pady=(15, 0))
        self.var_hora = tk.StringVar()
        cbbx_hora = ttk.Combobox(self.frame_3,
            textvariable=self.var_hora,
            state='readonly',
            width=15,
            values=['08:30', '11:20', '14:30', '17:00', '20:00', '22:20'])
        cbbx_hora.set(cbbx_hora['values'][0]) #Muestro el primer valor del combobox
        cbbx_hora.pack()
    
    def frame_cuatro(self):
        self.frame_4 = tk.Frame(self.frame_compra, background='gray17')

        tk.Label(self.frame_4,
            text='Compra de Entrada',
            bg='gray17',
            fg='white',
            font=('Tahoma', 18, 'bold')).pack()
        tk.Label(self.frame_4,
            text='Subtotal',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack()
        self.lbl_subtotal = tk.Label(self.frame_4,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_subtotal.pack()
        tk.Label(self.frame_4,
            text='Descuento',
            bg='gray17',
            fg='white',
            font=('Tahoma', 12, 'bold')).pack()
        self.lbl_descuento = tk.Label(self.frame_4,
            bg='gray17',
            fg='white',
            font=('Tahoma', 8, 'bold'))
        self.lbl_descuento.pack()
        tk.Label(self.frame_4,
            text='Total',
            bg='gray17',
            fg='white',
            font=('Tahoma', 16, 'bold')).pack()
        self.lbl_total = tk.Label(self.frame_4,
            bg='gray17',
            fg='white',
            font=('Tahoma', 20, 'bold'))
        self.lbl_total.pack()
    

    def frame_botones(self):
        self.frame_boton = tk.Frame(self, background='gray17')
        
        tk.Button(self.frame_boton, 
            text='Comprar',
            command=self.comprar,
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=0, column=0, padx=10, pady=10)
        
        tk.Button(self.frame_boton, 
            text='Cancelar',
            command=lambda: self.root.mostrar_frame(Pelicula_Cliente),
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#f2104d",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white").grid(row=0, column=1, padx=10, pady=10)
    
    def comprar(self):
        if estado_sesion():#El cliente ya inicio sesion
            pass
        else:
            from login.Login import Login
            self.root.mostrar_frame(Login)
