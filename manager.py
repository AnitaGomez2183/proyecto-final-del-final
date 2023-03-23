import json
class Manager:
    ruta = 'archivos/'        

    def __init__(self, archivo: str):  #constructor init
        self.__archivo = archivo        
    

    def creator(self, info:dict):  # crea el archivo
        try:
            with open(Manager.ruta + self.__archivo, "w") as wfile:
                json.dump(info, wfile, indent=4)  # lo abre para escribirlo
                wfile.close()
        except Exception as e:    #manejo de errores
            return {
                "status": "Failed",
                "message": str(e)
            }
        

    def get_info(self):  # método que obtiene todas las recetas (lista)
        try: 
            with open(Manager.ruta+self.__archivo, "r") as usefile: #abre archivo y guarda los datos en dict
                data = json.load(usefile) 
        except Exception as e:  
            return {
                "status": "Failed",
                "message": str(e)
            }
        else:
            return {
                "status": "Success",
                "info": data
            }
        
    def find_one(self, key: str) -> dict:  #método que busca una receta por el nombre (key) y la devuelve
        try:            
            data = self.get_info()  #trae las recetas a data
            data = data["info"]
            if(key not in data): # en el caso que no existe la info
                return {
                    "status": "Failed",
                    "message": "Recipe not found"
                }                
            obj = data[key]  
            # return obj
        except Exception as e:  
            return {
                "status": "Failed",
                "message": str(e)
            }
        else:
            return {
                "status": "Success",
                "data": {      #
                    key: obj
                }
            }

    
    def sum_one(self, clave: str, valor) -> str:   #metodo que crea una receta - recibe clave (nombre) -valor (contenido de la receta)
        try:
            data = self.get_info() #metodo que trae la info
            data = data["info"]  
            if(clave in  data):   # comprueba si la receta existe o no
                return {
                    "status": "Failed",
                    "message": "Recipe already exists" # me avisa que ya existe
                }
            else:    #Si no existe la receta, la escribe
                data[clave] = valor  #tomo el valor y lo agrego en clave
            
                with open(Manager.ruta+self.__archivo,"w") as writable_file: # abre el archivo  json y lo sobreescribe
                    json.dump(data, writable_file)                
        except Exception as e:
            return {
                "status": "Failed",
                "message": str(e)
            }
        else:
            return {
                "status": "Success",
                "message": "Recipe has been added"
            }
    
    def erase_one(self, llave: str)->str:  #borra la receta seleccionada, usando como parametro el nombre
        try:
            res = self.get_info()  # recibo una respuesta 
            recetas = res["info"]  # listado de receta y la guarda en res
            if(llave in recetas):
                del recetas[llave]
                self.creator(recetas)                
            else: 
                return {
                    "status": "unexistent",
                    "message": f"Recipe {llave}  doesn't exist "
                }                
        
        except Exception as e:
            return {
                "status": "Failed",
                "message": str(e)
            }
        else:
            return {
                    "status": "Success",
                    "message": f"El objeto con clave {llave} ha sido eliminado exitosamente"
                }            
        
    def update_one(self, key, value) -> str:  # recibe una key (nombre) y escribe la nueva informacion
        try:
            data = self.get_info() # trae status yla info de la receta 
            data = data["info"]   # solo deja la lista de la receta
            if(key not in data):  #Si la llave no esta en data
                return {
                    "status": "Failed",
                    "message": f"Recipe {key} doesn't exist"
                }                
            else:  #Actualiza la receta elegida
                data[key]=value  #le asigna un nuevo valor al objeto 
                self.creator(data)   #sobreescribe el archivo             
        
        except Exception as e:
            return {
                "status": "Failed",
                "message": str(e)
            }
        else:
            return {
                    "status": "Success",
                    "message": f"Recipe {key} has been updated"
                }                
    def recetaDelDia(self):   # elige al azar una receta del listado 
            from random import choice
            try:
                res = self.get_info()
                claves = list(res['info'].keys()) #crea una lista con los nombres de la receta 
                selected = choice(claves)   # elige la receta al azar y la devuelve            
            except Exception as e:
                return {
                    "status": "Failed",
                    "message": str(e)
                }
            else:
                return {
                    "status": "Success",
                    "deldia": selected
                }            
            
        
