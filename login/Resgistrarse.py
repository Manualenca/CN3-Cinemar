import tkinter as tk
from tkinter import messagebox
from cartelera.Cartelera import Cartelera

from conexion_db.Login_BD import verificar, guardar_datos

class Registrarse(tk.Frame):
    def __init__(self,root, contenedor):
        super().__init__(contenedor)
        self.root = root

        self.config(background='gray17')
        self.widgets_frame()
    

    def widgets_frame(self):
        # _____________________________ Etiquetas _______________________________________
        tk.Label(self,
            text='Registrarse',
            font=('Tahoma', 26, 'bold'),
            bg='gray17',
            fg='white').pack(pady=(20, 30))



        frame_1 = tk.Frame(self, background='gray17')
        frame_1.pack(pady=20)

        tk.Label(frame_1,
            text='Nombre',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Apellido',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=1, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Nombre de Usuario',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=2, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Contraseña',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=3, column=0, padx=10, pady=10)

        tk.Label(frame_1,
            text='Email',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=4, column=0, padx=10, pady=10)
        
        # __________________ Campos de texto _______________________________
        self.var_nombre = tk.StringVar()
        self.txt_nombre = tk.Entry(frame_1,
            textvariable=self.var_nombre,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30)
        self.txt_nombre.focus() #Pone el cursor en la primera caja de texto
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        self.var_apellido = tk.StringVar()
        tk.Entry(frame_1,
            textvariable=self.var_apellido,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30).grid(row=1, column=1, padx=10, pady=10)
        
        self.var_nombre_usuario = tk.StringVar()
        tk.Entry(frame_1,
            textvariable=self.var_nombre_usuario,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30).grid(row=2, column=1, padx=10, pady=10)
        
        self.var_contrasenia = tk.StringVar()
        self.contrasenia = tk.Entry(frame_1,
            textvariable=self.var_contrasenia,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            #show='#', #Para que no se vea la contrasenia solo '#'
            width=30).grid(row=3, column=1, padx=10, pady=10)
        
        self.var_email = tk.StringVar()
        tk.Entry(frame_1,
            textvariable=self.var_email,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30).grid(row=4, column=1, padx=10, pady=10)
        


        frame_2 = tk.Frame(self, background='gray17')
        frame_2.pack(pady=20)
        #_________________________________ Botones ________________________________________
        tk.Button(frame_2, 
            text="Registrarse",
            command=self.registrarse,
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white"
        ).grid(row=0, column=0, padx=10, pady=(30, 10))

        tk.Button(frame_2, 
            text="Cancelar",
            command=self.cancelar,
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#f2104d",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white"
        ).grid(row=0, column=1, padx=10, pady=(30, 10))
    

    
    def registrarse(self):
        if self.verifica_campos():
            verif = verificar(self.var_nombre_usuario.get(), self.var_email.get())
            if not verif[0] and not verif[1]: #Recorrio los registros y no encontro coincidencias
                guardar_datos( [#Envio una lista
                    self.var_nombre.get(), #Obtengo los valores de los campos de texto
                    self.var_apellido.get(),
                    self.var_nombre_usuario.get(),
                    self.var_contrasenia.get(),
                    self.var_email.get(),
                    1] ) #Como se registro sin problema su estado es acitivo, puede comprar y ver sus reservas
                messagebox.showinfo('Registrarse', 'Se ha registrado correctamente.')
                self.root.mostrar_frame(Cartelera)
            elif verif[0] and not verif[1]:
                messagebox.showerror('Error al Registrarse', 'Ya hay un correo igual al ingresado.')
            elif not verif[0] and verif[1]:
                messagebox.showerror('Error al Registrarse', 'Ya hay un usuario con ese nombre.')
            else:
                from login.Login import Login #Lo pongo aqui para evitar problemas
                messagebox.showerror('Error al Registrarse', 'Usted ya esta registrado')
                self.root.mostrar_frame(Login) #Muestra la clase Login para iniciar sesion
        else:
            messagebox.showerror('Error al Registrarse', 'Debe llenar todos los campos.')
    
    def verifica_campos(self): #Ningun campo debe estar vacio
        if self.var_nombre.get()=='' or self.var_apellido.get()=='' or self.var_nombre_usuario.get()=='' or self.var_contrasenia.get()=='' or self.var_email.get()=='':
            return False
        return True
    


    def cancelar(self):#Obtengo los valores de los campos y los seteo a vacio
        self.var_nombre.set('')
        self.var_apellido.set('')
        self.var_nombre_usuario.set('')
        self.var_contrasenia.set('')
        self.var_email.set('')

        self.txt_nombre.focus()
    
    