from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Cinemar.db' #Ruta de la base de datos


def guardar_pelis(lista1):#Le paso una lista con los valores
    conexion = Conexion_BD(RUTA_DB)
    no_Cat = buscar_categoria(lista1[1])
    lista=(lista1[0],no_Cat[0],lista1[2])
    
    sql = f'''
        INSERT INTO Pelicula (Id_Peli, Nom_Peli, Id_Categoria, Duracion)
        VALUES(null,?,?,?)
    '''
    #messagebox.showinfo('Cosas', sql)
    try:
        conexion.cursor.execute(sql, lista)
        conexion.commit()
        conexion.cerrar()
        messagebox.showinfo('Guardar Peliculas', 'Se cargó bien la Película')
    except:
        messagebox.showerror('Guardar Peliculas', 'No se ha cargado la Pelicula')

def buscar_categoria(nom_cat):
    conexion = Conexion_BD(RUTA_DB)
    sql = f'''
        SELECT Id_Categoria FROM Categoria where Nombre_Categoria ="{nom_cat}"
    '''

    try:
        conexion.cursor.execute(sql)
        resultado = conexion.cursor.fetchall() #Devuelve los registros en una tupla
        
        
        #rdo = resultado[0]
        conexion.commit()
        conexion.cerrar()
        #messagebox.showinfo('Iniciar Sesión', resultado[0])
    except:
        messagebox.showerror('Guardar Datos', 'No se pudo cargar la Categoria')
    
    return resultado[0] #Devuelve el ID


def get_nombres():
    conexion = Conexion_BD(RUTA_DB)
    lista_nombres = []

    sql = 'SELECT Nom_peli FROM Pelicula'

    try:
        conexion.consulta(sql)
        lista = conexion.cursor.fetchall()#Retorna [('nombre1',), ('nombre2',), ...]
        
        for i in range(len(lista)):
            lista_nombres.append(lista[i][0])#Solo obtengo el nombre
        
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener lista nombres', 'No se pudo obtener la lista de nombres.')
    
    return lista_nombres #Retorno lista de nombres ['nombre1', 'nombre2', ...]