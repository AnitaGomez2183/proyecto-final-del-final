import json
from servicio import *
from ingrediente import *
from receta import *

class Recetario:
    
    nombre_archivo = "recetasDB.json"

    def __init__(self):
        self.recetarioService = FileManager(Recetario.nombre_archivo)
    
    def crearDB(self):
       try: 
           self.recetarioService.create({"guiso": {
               "ingredientes": [{
                    "nombre" : "papa",
                    "cantidad" : "1",
                    "unidad_de_medida" : "kg"
               },
               {
                    "nombre" : "carne",
                    "cantidad" : "0.5",
                    "unidad_de_medida" : "kg"
               }
               ],
               "preparacion": ["picar papa","picar carne"],
               "imagenes": ["ruta imagen 1","ruta imagen 2"],
               "duracion": "30 min",
               "coccion": "60 min",
               "fecha": "03/03/2023",
               "etiquetas": ["guiso", "carne","caliente"],
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
       
    def addOne(self, nombre, receta):
        try:
            res = self.recetarioService.addOne(nombre, receta)
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
        
    def delOne(self, nombre):
        try:
            res = self.recetarioService.deleteOne(nombre)
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
    
    def getAll(self):
        try:
            data = self.recetarioService.getAll()            
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

        
    
