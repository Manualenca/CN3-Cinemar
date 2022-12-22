import sqlite3


class Conexion_BD:
    def __init__(self,bd):#bd es el nombre de la base de datos
        self.conexion = sqlite3.connect(bd)
        self.cursor = self.conexion.cursor()
    
    def consulta(self, consulta):
        self.cursor.execute(consulta)
    
    def consultas(self, consulta, args):#Para cargar varios registros
        self.cursor.executemany(consulta, args)
    
    def commit(self):
        self.conexion.commit()
    
    def get_registro(self):#Para ver un registro
        return self.cursor.fetchone()
    
    def get_registros(self):#Para ver todos los registros
        return self.cursor.fetchall()
    
    def cerrar(self):
        self.conexion.close()
