from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Clientes.db'


def guardar_datos(cliente):
    conexion = Conexion_BD(RUTA_DB)

    sql = f'''
        INSERT INTO Clientes (nombre, apellido, nombre_usuario, contrasenia, email)
        VALUES('{cliente.nombre}', '{cliente.apellido}', '{cliente.nombre_usuario}', {cliente.contrasenia}', {cliente.email}')
    '''

    try:
        conexion.consulta(sql)
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Guardar Datos', 'No se ha creado ninguna tabla.')


def lista_datos():
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = 'SELECT * FROM Clientes'

    try:
        conexion.consulta(sql) #Recuperamos toda la informacion de la tabla
        lista = conexion.get_registros()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registros', 'No se ha creado ninguna tabla.')
    
    return lista


def eliminar_sala(id_cliente):
    conexion = Conexion_BD(RUTA_DB)

    sql = f'DELETE FROM Clientes WHERE id_cliente = {id_cliente}'

    try:
        conexion.consulta(sql)
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Eliminar Cliente', 'No se pudo eliminar el cliente.')