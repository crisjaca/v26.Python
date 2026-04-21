"""
INGIENERIA DE SISTEMAS | APLICATIVO SISTEMA ESCOLAR    
"""

class Estudiante:
    def __init__(self, Nombre, edad):
        self.nombre = Nombre
        self.edad = edad # atributo privado
        self.__notas = []
        
    def agregar_nota(self, nueva_nota):
        cantidad = len(self.__notas)
        self.__notas[cantidad] = nueva_nota
        return True;
    
    def calcular_Promedio(self):
        promedio = sum(self.__notas) / len(self.__notas)    
        return promedio;
    
    def estado(self):
        if len(self.__notas)==0:
            menssage = "No hay notas registradas!!"
            return menssage;
        elif self.calcular_Promedio()>=60:
            return True;
        else:
            return False;
        
    def mostrarInfo(self):
        lista = ""
        for i in range(len(self.__notas)):
            lista += self.__notas[i]
        
        message = "Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nNota : ",lista
        return message;
    
class sistema_Escolar:
    def __init__(self):
        self.lista_Estudiantes = []
            
    
    
