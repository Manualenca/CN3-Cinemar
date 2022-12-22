from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Cinemar.db' #Ruta de la base de datos


def guardar_sala(sala):#Le paso una lista con los valores
    conexion = Conexion_BD(RUTA_DB)
    
    sql = f'''
        INSERT INTO Sala (Id_Sala, Pelicula, Nro_Sala, Fecha, Capacidad)
        VALUES(null,?,?,?,?)
    '''
    try:
        conexion.cursor.execute(sql, sala)
        conexion.commit()
        conexion.cerrar()
        messagebox.showinfo('Crear Sala', 'Se creó la sala correctamente.')
    except:
        messagebox.showerror('Crear Sala', 'No se ha podido crear la sala.')



def get_salas():############### ESTA FUNCION NO ES LLAMADA POR NADIE ######################33
    conexion = Conexion_BD(RUTA_DB)
    lista_salas = []

    sql = 'SELECT * FROM Sala'

    try:
        conexion.consulta(sql)
        lista_salas = conexion.cursor.fetchall()#Obtengo todos los registros
        
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Salas', 'No se pudo obtener la lista de Salas.')
    
    return lista_salas #Retorna todas las salas

