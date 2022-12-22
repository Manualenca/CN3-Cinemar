from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Cinemar.db'


def guardar_datos(reserva): #Seria una lista
    conexion = Conexion_BD(RUTA_DB)

    sql = f'''
        INSERT INTO Reservas_Cliente (pelicula, nro_sala, butacas, fecha, genero, duracion)
        VALUES(?,?,?,?,?,?)
    '''

    try:
        conexion.cursor.execute(sql, reserva)
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Guardar Datos', 'No se ha podido guardar los datos.')


def lista_datos():
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = 'SELECT * FROM Reservas_Cliente'#Lista de Películas

    try:
        conexion.consulta(sql) 
        lista = conexion.cursor.fetchall()#Recuperamos toda la informacion de la tabla
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registros', 'No se ha obtener los registros.')
    
    return lista #Devuelve todos los registros de la tabla

def lista_datos1():
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = 'SELECT P.id_Peli, P.Nom_Peli, C.Nombre_Categoria, P.Duracion FROM Pelicula as P left join Categoria as C using (id_Categoria)'#Lista de Películas

    try:
        conexion.consulta(sql) 
        lista = conexion.cursor.fetchall()#Recuperamos toda la informacion de la tabla
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registros', 'No se ha obtener los registros.')
    
    return lista #Devuelve todos los registros de la tabla
