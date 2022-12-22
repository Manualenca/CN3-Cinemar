from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Cinemar.db'


def lista_datos():
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = 'SELECT * FROM Reservas_Administrador'

    try:
        conexion.consulta(sql) #Recuperamos toda la informacion de la tabla
        lista = conexion.cursor.fetchall()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registros', 'No se ha podido obtener los registros.')
    
    return lista #Devuelve todos los registros


def buscar(cliente):
    conexion = Conexion_BD(RUTA_DB)
    lista = []
    reservas = []

    sql = f'SELECT * FROM Reservas_Administrador WHERE cliente = {cliente}'

    try:
        conexion.consulta(sql)
        lista = conexion.cursor.fetchall()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registro', 'Cliente no encontrado.')
    
    #Recorro a lista y comparo
    for i in range(len(lista)):
        if cliente in lista[i]:
            reservas.append(lista[i])
    
    return reservas #Un cliente puede tener 0, 1 o muchas reservas

