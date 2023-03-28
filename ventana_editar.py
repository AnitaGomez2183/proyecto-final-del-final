import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from manager import *
from tkinter import font
import tkinter.messagebox as messagebox

""" 
Importamos tkinter para crear la ventana
Importamos todos los metodos y clases del recetario
"""

class VentanaEditar(ttk.Frame):
    """
    En esta clase manejamos el frontend de una ventana de edicion
    """

    def __init__(self, nombre_receta = "pollo", master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Editar Receta")
        self.master.configure(bg="#F58182") # Configura el color de fondo en celeste
        

        """instanciamos la clase controlador de Receta"""
        self.recetas_service = Manager("recetario.json")

        self.receta_name = nombre_receta

        """
        Tomamos la data utilizando el metodo correspondiente.
        """
        res = self.recetas_service.find_one(nombre_receta)
        if(res['status']== "Success"):
            self.receta = res['data'][nombre_receta]       
            self.createView()   
        else:
            self.receta = {}
            
        
        
        

    def actualizar_diccionario(self, *args):
        self.receta["duracion"] = self.duracion.get()
        self.receta["coccion"] = self.coccion.get()
        self.receta["fecha"] = self.fecha.get()

            

    def guardar_receta(self):
        self.receta["duracion"] = self.duracion.get()    
        self.receta["coccion"] = self.coccion.get()
        self.receta["fecha"] = self.fecha.get()       
        res = self.recetas_service.update_one(self.receta_name,self.receta)
        if res["status"] == True:
            messagebox.showinfo("Éxito", res["message"])
        else:
            messagebox.showerror("Error", res["message"])    

        
    
    def createView(self):
        fuente_mediana = font.Font(family="Arial", size=20, weight="bold")
        fuente_titulo = font.Font(family="Impact", size=30)

        """
        Enlaza los campos del dictionary self.receta a variables de control tkinter
        """
        duracion_var = tk.StringVar()
        duracion_var.set(self.receta["duracion"])
        #duracion_var.trace("w", self.actualizar_diccionario)

        coccion_var = tk.StringVar()
        coccion_var.set(self.receta["coccion"])
        #coccion_var.trace("w", self.actualizar_diccionario)

        fecha_var = tk.StringVar()
        fecha_var.set(self.receta["fecha"])
        #fecha_var.trace("w", self.actualizar_diccionario)

        



        """
        Creacion de los widgets y entrys
        """
        # valor_name = tk.StringVar(value=self.receta_name)        
        # tk.Label(self, text=f"Nombre de Receta: ").grid(row=0, column=0, padx=10, pady=10)
        # self.nombre_receta = tk.Entry(self, textvariable=valor_name, font=fuente_mediana)        
        # self.nombre_receta.configure(state='normal')                
        # self.nombre_receta.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self, text=self.receta_name, background="#F6B54F", font=fuente_titulo).grid(row=0, column=0, padx=10, pady=10)
        #self.nombre_receta = tk.Entry(self, font=fuente_mediana)
        
        #self.nombre_receta.configure(state='disabled')

        tk.Label(self, text="Duración de preparación: ").grid(row=1, column=0,padx=10, pady=10)
        self.duracion = tk.Entry(self, textvariable=duracion_var)
        self.duracion.grid(row=1, column=1)

        tk.Label(self, text="Tiempo de cocción: ").grid(row=2, column=0, padx=10, pady=10)
        self.coccion = tk.Entry(self, textvariable=coccion_var)
        self.coccion.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Fecha: ").grid(row=3, column=0, padx=10, pady=10)
        self.fecha = tk.Entry(self, textvariable=fecha_var)
        self.fecha.grid(row=3, column=1, padx=10, pady=10)

        self.treeview = ttk.Treeview(self, columns=("nombre", "cantidad", "unidad_de_medida"), show="headings")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("cantidad", text="Cantidad")
        self.treeview.heading("unidad_de_medida", text="Unidad de medida")

        for i, ingrediente in enumerate(self.receta['ingredientes']):
            self.treeview.insert("", tk.END, values=(ingrediente['nombre'], ingrediente['cantidad'], ingrediente['unidad_de_medida']))

        self.treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        #self.treeview.column("nombre", editable="yes")


        ttk.Button(self, text="Guardar", command=self.guardar_receta).grid(row=10, column=1)

        self.grid()  
    

 
    
    
if __name__ == "__main__":
    #root = tk.Tk()
    root = ThemedTk(theme="ubuntu")
    window = VentanaEditar(master=root)    
    window.mainloop()
    
    
