import tkinter as tk
from tkinter import messagebox
from cartelera.Cartelera import Cartelera

from conexion_db.Login_BD import iniciar_sesion
#from login.Resgistrarse import Registrarse

class Login(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.root = root
        self.config(background='gray17')
        self.widgets_frame()
    

    def widgets_frame(self):
        # _____________________________ Etiquetas _______________________________________
        tk.Label(self,
            text='Iniciar Sesión',
            font=('Tahoma', 26, 'bold'),
            bg='gray17',
            fg='white').pack(pady=(20, 30))


        frame_login = tk.Frame(self, background='gray17')
        frame_login.pack(pady=30)

        tk.Label(frame_login,
            text='Nombre de Usuario',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_login,
            text='Contraseña',
            font=('Tahoma', 14, 'bold'),
            bg='gray17',
            fg='white').grid(row=1, column=0, padx=10, pady=10)
        # __________________ Campos de texto _______________________________
        self.var_nombre_usuario = tk.StringVar()
        self.txt_nombre_usuario = tk.Entry(frame_login,
            textvariable=self.var_nombre_usuario,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30)
        self.txt_nombre_usuario.focus() #Pone el cursor en la primera caja de texto
        self.txt_nombre_usuario.grid(row=0, column=1, padx=10, pady=10)
        
        
        self.var_contrasenia = tk.StringVar()
        tk.Entry(frame_login,
            textvariable=self.var_contrasenia,
            fg='gray',
            font=('Verdana', 9, 'bold'),
            width=30,show='*').grid(row=1, column=1, padx=10, pady=10)



        frame_login_2 = tk.Frame(self, background='gray17')
        frame_login_2.pack(pady=30)

      #  tk.Label(frame_login_2,
      #      text='¿Olvidó su contraseña?',
      #      cursor='hand2',
      #      font=('Tahoma', 11, 'italic', 'underline'),
      #      bg='gray17',
      #      fg='#2e3ae4').grid(row=0, column=0, padx=10, pady=(0, 10))

        lbl_registrarse = tk.Label(frame_login_2,
            text='Registrarse',
            font=('Arial Black', 12, 'bold'),
            bg='gray17',
            fg='white',
            cursor='hand2',
            relief='groove',
            borderwidth=6)
        lbl_registrarse.grid(row=1, column=0, padx=10, pady=15, ipadx=10, ipady=10)
        
        lbl_registrarse.bind('<Button-1>', self.registrarse)



        frame_boton = tk.Frame(self, background='gray17')
        frame_boton.pack(pady=10)
        #_________________________________ Botones ________________________________________
        tk.Button(frame_boton, 
            text="Iniciar Sesión",
            command=self.iniciar_sesion,
            width=20, 
            font=("Arial", 12, "bold"), 
            fg="white",
            bg="#2d45e6",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#a3b8d9", #Para que cambie el color de fondo al hacer click
            activeforeground="white" #Para que cambie el color de fuente al hacer click
        ).grid(row=0, column=0, padx=10, pady=(20, 10))

        tk.Button(frame_boton, 
            text="Cancelar",
            command=self.cancelar,
            width=20, 
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#d23952",
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="#eb8f95", #Para que cambie el color de fondo al hacer click
            activeforeground="white" #Para que cambie el color de fuente al hacer click
        ).grid(row=0, column=1, padx=20, pady=(20, 10))
    
    def iniciar_sesion(self):
        if self.var_nombre_usuario.get()!='' and self.var_contrasenia.get()!='':
            sesion = iniciar_sesion(self.var_nombre_usuario.get(), self.var_contrasenia.get())

            if sesion[0] and not sesion[1]:#Es un usuario
                messagebox.showinfo('Iniciar Sesión', 'Ha iniciado sesión correctamente')

                self.root.mostrar_frame(Cartelera)

            elif sesion[0] and sesion[1]:#Es el administrador
                messagebox.showinfo('Administrador', 'BIENVENIDO ADMINISTRADOR.')
                self.root.mostrar_frame(Cartelera)

            elif not sesion[0] and not sesion[1]:
                messagebox.showerror('Error Iniciar Sesión', 'Usted no esta registrado.')
        
        else:
            messagebox.showerror('Error Iniciar Sesión', 'Debe llenar todos los campos.')


    def cancelar(self):
        self.var_nombre_usuario.set('')
        self.var_contrasenia.set('')
        self.txt_nombre_usuario.focus()
    

    def registrarse(self, event):
        from login.Resgistrarse import Registrarse #Lo pongo aqui para evitar problemas
        self.root.mostrar_frame(Registrarse)
    
    
