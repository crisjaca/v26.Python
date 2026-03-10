
# class Estudiante:

#     def __init__(self, nombre,edad):
#         self.nombre = nombre;
#         self.edad = edad;

#     def mostrar (self):
#         print(self.nombre,"\nedad: ",self.edad);


# est1 = Estudiante("Ana",20)

# est1.mostrar()

class Carro:

    def __init__(self, marca,modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar (self):
        print("Marca: ",self.marca,"\nmodelo: ",self.modelo,"\ncolor: ",self.color);
        print("---------------------")


auto1 = Carro("Tesla",2025,"Gris platino")
auto2 = Carro("BMW", 2024, "Negro mate")
auto3 = Carro("Mercedes-Benz", 2023, "Blanco perla")
auto4 = Carro("Audi", 2022, "Rojo escarlata")
auto5 = Carro("Porsche", 2025, "Azul eléctrico")
auto6 = Carro("Ferrari", 2021, "Rojo clásico")
auto7 = Carro("Lamborghini", 2024, "Amarillo intenso")
auto8 = Carro("Toyota", 2023, "Verde oliva")
auto9 = Carro("Ford", 2022, "Plateado metálico")
auto10 = Carro("Chevrolet", 2025, "Azul marino")

auto1.mostrar();
auto2.mostrar();
auto3.mostrar();
auto4.mostrar();
auto5.mostrar();
auto6.mostrar();
auto7.mostrar();
auto8.mostrar();
auto9.mostrar();
auto10.mostrar();