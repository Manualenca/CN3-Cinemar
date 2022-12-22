import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexion_db.Login_BD import cerrar_sesion

from login.Resgistrarse import Registrarse
from login.Login import Login
from cartelera.Cartelera import Cartelera
from pelicula.Pelicula_Cliente import Pelicula_Cliente
from reserva.Reserva_Cliente import Reserva_Cliente

class Menu_Usuario:
    def __init__(self, root):
        self.root = root
        self.barra_menu = tk.Menu(root)
        self.root.config(menu=self.barra_menu)
        
    def sesion_cerrada(self):
        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        menu_login = tk.Menu(self.barra_menu, 
            tearoff=0,
            background='#e74166',
            foreground='white',
            activebackground='white', # Color de fondo al pasar el cursor
            activeforeground='#e74166',  # Color de fuente al pasa el cursor
            font=('Tahoma', 9, 'bold'))
        # Agrego menu_inicio a la barra de menu (self.barra_menu)
        self.barra_menu.add_cascade(label="Login", menu=menu_login)

        #Agrego submenus a menu_inicio
        menu_login.add_cascade(label="Iniciar Sesión", command=lambda: self.root.mostrar_frame(Login))
        menu_login.add_cascade(label="Registrarse", command=lambda: self.root.mostrar_frame(Registrarse))
        menu_login.add_separator()
        menu_login.add_cascade(label="Salir", command=self.root.destroy)

        
        # Agrego menues a la barra de menu
        self.barra_menu.add_cascade(label="Cartelera", command=lambda: self.root.mostrar_frame(Cartelera))
        self.barra_menu.add_cascade(label="Peliculas", command=lambda: self.root.mostrar_frame(Pelicula_Cliente))
        self.barra_menu.add_cascade(label="Acerca de", command=self.acerca_de)
    
    
    def sesion_abierta(self):
        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        #Agrego items al menu principal
        self.barra_menu.add_cascade(label="Cartelera", command=lambda: self.root.mostrar_frame(Cartelera))
        self.barra_menu.add_cascade(label="Peliculas", command=lambda: self.root.mostrar_frame(Pelicula_Cliente))
        self.barra_menu.add_cascade(label="Mis Reservas", command=lambda: self.root.mostrar_frame(Reserva_Cliente))
        self.barra_menu.add_cascade(label="Cerrar Sesión", command=self.cerrar_sesion)
        self.barra_menu.add_cascade(label="Acerca de", command=self.acerca_de)
        self.barra_menu.add_cascade(label='Salir', command=self.root.destroy)
    
    
    def acerca_de(self):
        return messagebox.showinfo('Acerca de', 'Cinemar Version 1.1 \n\n \u00A9 2022 Cinemar Inc.')
    

    def cerrar_sesion(self):
        cerrar_sesion() #Actualizo el estado del cliente o el administrador
        self.root.mostrar_frame(Cartelera)
    

    