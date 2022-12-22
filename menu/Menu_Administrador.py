import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from cartelera.Cartelera import Cartelera
from conexion_db.Login_BD import cerrar_sesion
from pelicula.Pelicula_Administrador import Pelicula_Administrador
from pelicula.Pelicula_Cliente import Pelicula_Cliente
from sala.Sala_Administrador import Sala_Administrador
from reserva.Reserva_Administrador import Reserva_Administrador

class Menu_Administrador:
    def __init__(self, root):
        self.root = root
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # Agrego menues a la barra de menu
        barra_menu.add_cascade(label="Cartelera", command=lambda: self.root.mostrar_frame(Cartelera))
        barra_menu.add_cascade(label="Peliculas Disponibles", command=lambda: self.root.mostrar_frame(Pelicula_Cliente))
        barra_menu.add_cascade(label="Cargar Pelicula", command=lambda: self.root.mostrar_frame(Pelicula_Administrador))
        barra_menu.add_cascade(label="Crear Sala", command=lambda: self.root.mostrar_frame(Sala_Administrador))
        barra_menu.add_cascade(label="Reservas", command=lambda: self.root.mostrar_frame(Reserva_Administrador))
        barra_menu.add_cascade(label="Cerrar Sesión", command=self.cerrar_sesion)
        barra_menu.add_cascade(label="Acerca de", command=self.acerca_de)
        barra_menu.add_cascade(label="Salir", command=self.root.destroy)
    
    
    def acerca_de(self):
        return messagebox.showinfo('Acerca de', 'Cinemar Version 1.1 \n\n \u00A9 2022 Cinemar Inc.')
    

    def cerrar_sesion(self):
        cerrar_sesion() #Actualizo el estado del cliente o administrador
        self.root.mostrar_frame(Cartelera)
    
    