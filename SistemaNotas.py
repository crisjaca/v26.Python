"""
Ejercicio 1
"""

class Estudiante:
    def __init__(self, Nombre, Nota_final):
        self.nombre = Nombre;
        self.__nota_final = Nota_final; # atributo privado

    def asignarNota(self, nota):
        if nota >= 0 and nota <= 100:
            self.__nota_final = nota
            print("Se actualizo la nota del estudiante: ",self.nombre," a: ",self.__nota_final)
        else:
            print("Entrada Invalida");

    def mostrarInfo(self):
        print("El estudiante: ",self.nombre,"\n Nota final: ",self.__nota_final);

    def aprobo(sefl):
        if sefl.__nota_final >= 60:
            print("El estudiante APROBO.")
        else:
            print("El estudiante reprobo.")

nota1 = Estudiante("CAMILO",20);
nota1.asignarNota(50);
#print(nota1.__nota_final)
nota1.mostrarInfo();
nota1.aprobo();
