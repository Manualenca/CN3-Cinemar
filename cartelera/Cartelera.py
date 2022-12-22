import tkinter as tk
from PIL import ImageTk, Image

from pelicula.Pelicula_Cliente import Pelicula_Cliente


class Cartelera(tk.Frame):
    def __init__(self, root, contenedor):
        super().__init__(contenedor)
        self.config(background='gray17')
        self.titulo = tk.Label(self, 
            text='Cartelera', 
            font=('Verdana', 26, 'bold'),
            fg='white',
            bg='gray17'
            ).pack(pady=(20, 30))
        
        self.lista_nueva = []
        self.root = root # root es la clase App que hereda de Tk()

        # Frame peliculas
        self.frame_1 = tk.Frame(self, background='gray17')
        self.frame_1.pack()
        self.frame_2 = tk.Frame(self, background='gray17')
        self.frame_2.pack(pady=(20, 0))

        self.tamanio_imagen()
        for i in range(len(self.lista_nueva)):
            self.frame_imagen(self.lista_nueva[i], self.frame_1) #Cartelera superior
            self.frame_imagen(self.lista_nueva[i], self.frame_2) #Cartelera inferior

    #Cambiar el tamaño de una imagen
    def tamanio_imagen(self):
        self.lista = [
            Image.open('image/black_adam.jpg'), 
            Image.open('image/avatar-el_camino_del_agua.jpg'),
            Image.open('image/aftersun.jpg'),
            Image.open('image/creed_iii.jpg'),
            Image.open('image/super_mario-la_pelicula.jpg'),
            Image.open('image/shazam-la_furia_de_los_dioses.jpg')
        ]

        for i in range(len(self.lista)):
            self.lista[i] = self.lista[i].resize((100, 150), Image.ANTIALIAS)# Reduce al tamaño dado y mantiene la calidad de imagen
            self.lista_nueva.append(ImageTk.PhotoImage(self.lista[i]))


    def frame_imagen(self, imagen, master):
        frame = tk.Frame(master, relief='sunken', borderwidth=4)# Padre del frame, relieve y ancho del relieve
        frame.pack(side=tk.LEFT, expand=True, padx=15)

        tk.Label(frame, text='Pelicula').pack()
        lbl = tk.Label(frame, image=imagen, cursor='hand2')
        lbl.pack() #Esto va por separado si muetra error al usar bind
        lbl.bind('<Button-1>', self.ver_pelicula) #Evento 'Click boton izquierdo de mouse' y funcion
        
        tk.Label(frame, text='Fecha').pack()
        return frame
    

    def ver_pelicula(self, event):#Se debe para un parametro al usar bind por mas que no se use
        self.root.mostrar_frame(Pelicula_Cliente)

    
       




