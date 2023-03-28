import json
from manager import *
from ingredientes import *
from recetario import *

class Recetario:
    
    nombre_archivo = "recetario.json"

    def __init__(self):
        self.recetarioService = Manager(Recetario.nombre_archivo)
    
    def creator(self):
       """ Funcion que crea los archivos json(recetas)
       """
       try: 
           self.recetarioService.creator({"pollo al horno": {
               "ingredientes": [{
                    "nombre" : "pollo",
                    "cantidad" : "1",
                    "unidad_de_medida" : "u"
               },
               {
                    "nombre" : "aceite",
                    "cantidad" : "1",
                    "unidad_de_medida" : "cda"
               }
               ],
               "preparacion": ["poner aceite al pollo","poner al horno y cocinar"],
               "imagenes": ["ruta imagen 1","ruta imagen 2"],
               "duracion": "15 min",
               "coccion": "60 min",
               "fecha": "03/03/2023",
               "etiquetas": ["pollo", "horno","caliente"],
               "favorita": True}
               })
       except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
       else:
           return {
                "status": True,
                "message": "El archivo recetario ha sido creado con Exito"
            }
       
    def sum_one(self, nombre, receta):
        try:
            res = self.recetarioService.sum_one(nombre, receta)
            if(res["status"] == False):
                return {
                "status": False,
                "message": f"La receta {nombre} ya existe"
            }
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "message": f"La receta {nombre} ha sido agregada con Exito"
            }
        
    def erase_one(self, nombre):
        try:
            res = self.recetarioService.erase_one(nombre)
            if(res["status"] == False):
                return {
                "status": False,
                "message": res['message']
            }
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "message": res['message']
            }
    
    def get_info(self):
        try:
            data = self.recetarioService.get_info()            
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "recetas": data
            }
        
    def updateOne(self, nombre, newInfo):
        try:
            res = self.recetarioService.updateOne(nombre, newInfo)
            if(res["status"] == False):
                return {
                "status": False,
                "message": f"la receta {nombre} no Existe"
            }   
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "message": f"la receta {nombre} ha sido Actualizada"
            }
        
    def getOne(self, nombre):
        try:
            res = self.recetarioService.getOne(nombre)
            if(res["status"] == False):
             return {
                "status": False,
                "message": f"la receta {nombre} no Existe"
            }   
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "receta": res['data']
            }
        
    def filterByLabel(self, etiqueta):
        try:
            res = self.recetarioService.getAll()
            if(len(res) == 0):
                return {
                    "status": True,
                    "data": []
                }
            filtradas = []
            for nombre, datos in res.items():
                if(etiqueta in datos['etiquetas']):
                    obj = {nombre: datos}
                    filtradas.append(obj)            
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "recetas": filtradas
            }
        
    def recetaDelDia(self):
        from random import choice
        try:
            res = self.recetarioService.getAll()
            keys = list(res.keys())
            elegida = choice(keys)                
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
           return {
                "status": True,
                "r_del_dia": elegida
            }

        
    
