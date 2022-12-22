import tkinter as tk
from PIL import ImageTk, Image
from cartelera.Cartelera import Cartelera


class Main(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.config(background='gray17')

        tk.Label(self, 
            text='CINEMAR', 
            font=('Cooper Black', 50, 'bold', 'underline'),
            bg='gray17',
            fg='white').pack(pady=20)
        
        
        imagen = Image.open('image/cinemar.png')
        # Reduciendo el tamaño de la imagen principal
        imagen = imagen.resize((280, 280), Image.ANTIALIAS)# Reduce al tamaño dado y mantiene la calidad de imagen

        self.nueva_imagen = ImageTk.PhotoImage(imagen)
        tk.Label(self, 
            image=self.nueva_imagen, 
            background='gray17').pack()


        tk.Button(self, 
            text='ENTRAR', 
            font=('Cooper Black', 20, 'bold'), 
            fg='white', 
            bg='green',
            cursor="hand2", #Para que el cursor cambie de flecha a manito
            activebackground="lightgreen", #Para que cambie el color de fondo al hacer click
            activeforeground='white', #Para que cambie el color de fuente al hacer click
            command=lambda: root.mostrar_frame(Cartelera)).pack(pady=20) #root es la clase App que hereda de Tk()
        

