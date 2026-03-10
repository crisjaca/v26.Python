

class Libro:

    def __init__(self, titulo,autor, año, disponibilidad):
        libros = {}

    def mostrar(self):
        print("Libro: ",self.titulo,"\nAutor: ",self.autor,"\naño: ",self.año,"\nDisponible? ",self.disponibilidad)

    def crear(self, titulo,autor, año, disponibilidad ):
        self.libros.append({titulo,autor,año,disponibilidad})
        print(f"El libro { titulo } se agrego..")
    
    def prestar(self)
valor = True;


try:
    while valor:
        print("Biblioteca..\n1) Agregar libro.\n2) Mostrar libro.\n3) Prestrar libro.\n4) Devolver libro\n5) Salir");
        opc = int(input("Selecciona un opcion: "));

        if opc == 1:

            libro1 = input("Titulo del libro: ");
            autor1 = input("Ingresa el autor: ")
            año1 = int(input("Ingresa el año: "));
            disp1 = True;
            obj1 = Libro(libro1,autor1,año1,disp1)
            #libros.append(libro1,autor1,año1,disp1)
            print("Libro agregado!!");
        elif opc == 2:
            Libro.mostrar();
        elif opc == 5: 
            break;
except ValueError:
    print("Error: Ingreso invalido")