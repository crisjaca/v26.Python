

class Libro:

    def __init__(self, titulo,autor, año, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = disponibilidad;

    def mostrar(self):
        print("Libro: ",self.titulo,"\nAutor: ",self.autor,"\naño: ",self.año,"\nDisponible? ",self.disponibilidad)

    # Método para prestar libro
    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    # Método para devolver libro
    def devolver(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    
valor = True;

biblioteca = {}
try:
    while valor:
        print("Biblioteca..\n1) Agregar libro.\n2) Mostrar libro.\n3) Prestrar libro.\n4) Devolver libro\n5) Salir");
        opc = int(input("Selecciona un opcion: "));

        if opc == 1:

            libro1 = input("Titulo del libro: ");
            autor1 = input("Ingresa el autor: ")
            año1 = int(input("Ingresa el año: "));
            disp1 = True;
            libro = Libro(libro1,autor1,año1,disp1)
            biblioteca.append(libro)
            print("Libro agregado!!");
        elif opc == 2:
            for libro in biblioteca:
                libro.mostrar()
        elif opc == 3:
            titulo = input("Título del libro a prestar: ")
            for libro in biblioteca:
                if libro.titulo == titulo:
                    libro.prestar()

        elif opc == 4:
            titulo = input("Título del libro a devolver: ")
            for libro in biblioteca:
                if libro.titulo == titulo:
                    libro.devolver()
        elif opc == 5: 
            break;
except ValueError:
    print("Error: Ingreso invalido")