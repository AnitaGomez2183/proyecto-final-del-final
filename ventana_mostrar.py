import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as messagebox
from manager import *
from PIL import Image, ImageTk

""" 
Importamos tkinter para poder crear la ventana
Tambien importamos todos los metodos y clases de recetario que nos permite utlizarlas en lo que necesitemos
"""

class VentanaMostrar(ttk.Frame):
    
    """
    En esta clase creamos la ventana que permite mostar una receta buscada por el usuario
    """

    def __init__(self, nombre_receta ="Pizza de anana" , master=None):
        super().__init__(master)
        self.master = master
        self.master.title(f"Receta de {nombre_receta} ")
        self.master.geometry("1400x700")
        self.master.configure(bg="#F58182") 

        """
        instanciamos la clase controlador de Receta
        """
        self.recetas_service = Manager("recetario.json")

        res= self.recetas_service.find_one(nombre_receta)
        if res["status"] == "Success":
            self.data = res["data"][nombre_receta]
        
        else:
            self.data = {}

        """
        Creamos los label necesarios y las list box para mostrar los datos 
        """
        
        tk.Label(self, text="Ingredientes ").grid(row=0, column=0)
        listbox = tk.Listbox(self, height=len(self.data["ingredientes"]))
        row_count = 0
        for item in self.data["ingredientes"]:
            ingres = (f"{item['nombre']}  -  {item['cantidad']} {item['unidad_de_medida']}")
            listbox.insert(tk.END, ingres)
            row_count += 1
        listbox.grid(column=0, row=1, padx=(0, 10), pady=15, sticky='w')

        tk.Label(self, text="Pasos de preparación").grid(row=0, column=1)
        listbox = tk.Listbox(self, height=len(self.data["preparacion"]))
        row_count2 = 0
        for item in self.data["preparacion"]: 
            listbox.insert(tk.END, item)
            row_count2 += 1
        listbox.grid(column=1, row=1, padx=(0, 10), pady=15, sticky='w')


        tk.Label(self, text="Duración de la preparación: ").grid(row=0, column=4)
        tk.Label(self, text=self.data["duracion"]).grid(row=0, column=5)

        tk.Label(self, text="Tiempo de cocción: ").grid(row=1, column=4)
        tk.Label(self, text=self.data["coccion"]).grid(row=1, column=5)

        tk.Label(self, text="Fecha de creación de la receta: ").grid(row=2, column=4)
        tk.Label(self, text=self.data["fecha"]).grid(row=2, column=5)


        tk.Label(self, text="Etiquetas").grid(row=0, column=3)
        listbox = tk.Listbox(self, height=len(self.data["etiquetas"]))
        row_count3 = 0
        for item in self.data["etiquetas"]: 
            listbox.insert(tk.END, item)
            row_count3 += 1
        listbox.grid(column=3, row=1, padx=(0, 10), pady=15, sticky='w')

        tk.Label(self, text="Es favorita: ").grid(row=4, column=4)
        if self.data.get("favorita", True):
            esfavorita = "Sí"
        else:
            esfavorita = "No"
        tk.Label(self, text=esfavorita).grid(row=4, column=5)


        """ 
        Creamos el Frame para la imagen
        """
        self.imagen_frame = ttk.Frame(self)
        self.imagen_frame.grid(row=30, column=6, padx=25, pady=25, sticky='w')        
        
        imagen = Image.open(f"pictures/{self.data['imagenes'][0]}")
        imagen = imagen.resize((400, 400), Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.label_img = tk.Label(self.imagen_frame)

        #self.label_img.configure(image=imagen_tk)
        self.label_img.image = imagen_tk
        self.label_img.pack()

        self.grid()    

if __name__ == "__main__":
    root = ThemedTk(theme="adapta", background="black")
    # root = tk.Tk()
    # root.configure(background="#FFFFFF")
    vent=VentanaMostrar(master=root)
    vent.mainloop()
    
    