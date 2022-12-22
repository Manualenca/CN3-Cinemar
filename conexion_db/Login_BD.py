from tkinter import messagebox
from conexion_db.Conexion_BD import Conexion_BD

RUTA_DB = 'database/Cinemar.db' #Ruta de la base de datos
ADMINISTRADOR = 'admin2590'

#Variables auxiliarres
sesion = False #Variable global para saber si un cliente o el administrador ha iniciado sesion
nombre_cliente = None #Variable auxiliar para saber quien ha iniciado sesion


def guardar_datos(cliente):#Le paso una lista con los valores
    conexion = Conexion_BD(RUTA_DB)
    global sesion

    sql = f'''
        INSERT INTO Login (nombre, apellido, nombre_usuario, contrasenia, email, estado)
        VALUES(?,?,?,?,?,?)
    '''

    try:
        conexion.cursor.execute(sql, cliente)
        conexion.commit()
        conexion.cerrar()
        sesion = True #Para que cuando se registre se cambie el menu
    except:
        messagebox.showerror('Guardar Datos', 'No se ha podido guardar los datos.')


def lista_datos():
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = 'SELECT * FROM Login'

    try:
        conexion.consulta(sql) #Recuperamos toda la informacion de la tabla
        lista = conexion.cursor.fetchall()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registros', 'No se ha podido obtener los registros.')
    
    return lista #Devuelve todos los registros


def verificar(nombre_usuario, email):
    conexion = Conexion_BD(RUTA_DB)
    lista = []

    sql = f'SELECT * FROM Login'

    try:
        conexion.consulta(sql)
        lista = conexion.cursor.fetchall()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registro', 'No se ha podido obtener los registros.')
    
    for i in range(len(lista)):
        if nombre_usuario in lista[i] and email not in lista[i]:
            return (True, False)  #Ya existe otro usuario con ese nombre  
        
        if nombre_usuario not in lista[i] and email in lista[i]:
            return (False, True)  #Ya hay un correo igual al ingresado 
        
        if nombre_usuario in lista[i] and email in lista[i]:
            return (True, True)  #Ya esta registrado 
    
    return (False, False) #Registro correcto


def iniciar_sesion(nombre_usuario, contrasenia):
    conexion = Conexion_BD(RUTA_DB)
    lista = []
    global nombre_cliente 
    global sesion #Pongo la palabra clave global para poder cambiar el valor de su contenido
    nombre_cliente = nombre_usuario
 #   global id_usuario 
    sql = f'SELECT * FROM Login'

    try:
        conexion.consulta(sql)
        lista = conexion.cursor.fetchall()
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener Registro', 'No se ha obtener los registros.')
    
    if nombre_usuario==ADMINISTRADOR and contrasenia==ADMINISTRADOR:
        actualizar_estado(nombre_usuario, 1)        
        return (True, True) #Es el administrador
    
    else:
        for i in range(len(lista)):
            
            if nombre_usuario in lista[i] and contrasenia in lista[i]:
                actualizar_estado(nombre_usuario, 1)                
                sesion = True
                return (True, False) #Es un usuario
    
    return (False, False) #No esta registrado

#Actualiza el campo estado de un usuario que inicio sesion
def actualizar_estado(nombre_usuario, estado):
    conexion = Conexion_BD(RUTA_DB)

    sql = f"UPDATE Login SET estado={estado} WHERE nombre_usuario='{nombre_usuario}'"

    try:
        conexion.consulta(sql)
        conexion.commit()
        conexion.cerrar()
    except:
        pass

#Esta funcion me sirve para saber si un cliente inicio sesion, 
# si es asi le aparece el Menu_Usuario cambia
#Esta funcion es llamada por App
def estado_sesion():
    return sesion

#Para saber si el administrador ha iniciado sesion, si es asi el menu cambia
#Esta funcion es llamada por la clase App para cambiar el menu
def admin(administrador):
    conexion = Conexion_BD(RUTA_DB)

    sql = f"SELECT estado FROM Login WHERE nombre_usuario='{administrador}'"
    resultado = (0,0)
    try:
        conexion.consulta(sql)
        resultado = conexion.cursor.fetchone()#Vevuelve el estado, es una tupla
        conexion.commit()
        conexion.cerrar()
    except:
        messagebox.showerror('Error', 'Nombre de usuario incorrecto.')
    
    return True if resultado[0]==1 else False

#Cuando se ejecuta el programa todos los estado se setean a cero
def estado_inicial():
    conexion = Conexion_BD(RUTA_DB)

    sql = 'SELECT nombre_usuario FROM Login'
    nombres = []

    try:
        conexion.consulta(sql)
        nombres = conexion.cursor.fetchall() #Obtengo todos los nombres, es una tupla
        conexion.commit()
        conexion.cerrar()
    except:
        pass
    
    for i in range(len(nombres)):
        actualizar_estado(nombres[i][0], 0)
        

def cerrar_sesion():
    global sesion
    sesion = False #Si es un cliente
    actualizar_estado(nombre_cliente, 0) #Si es el administrador o un cliente