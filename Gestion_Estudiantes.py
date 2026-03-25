"""
    Ingieneria de sistemas || Tercer Semestre P002
    
    Sistema de Gestion de Estudiantes y Notas
    Cristian Jacanamijoy Narvaez
"""

class Estudiante:
    #Inicio con el constructor recibiendo los datos: nombre, edad, notas.
    def __init__(self, Nombre, Edad):
        self.nombre = Nombre;
        self.edad = Edad;
        self.__notas = [];#el estudiante va ha tener varias notas para luego poder sacar un promedio de ellas

        # declaro con el constructor dnd se van a guardar los datos ingresados
    
    def mostrarInfo(self):
        print(f"***************************************\nNombre: {self.nombre}\nEdad: {self.edad}\nNotas: {self.__notas}")
        print(f"***************************************\n")

    def agregarNota(self, Nota):
        cantidadNotas = len(self.__notas)
        self.__notas.append(Nota);
        print("Se guardo la nota: ",cantidadNotas+1)

    def promedio(self):
        # promedio  de las notas del estudiante
        # verifico si no hay elemntos en la lista __notas
        if len(self.__notas) == 0:
            return 0
        # retorno el promedio usando los metodos sum() y len() para contar los elementos de una lista
        return sum(self.__notas) / len(self.__notas)

    def estado(self):
        #verifico si hay registro en __notas[]
        if len(self.__notas) == 0:
            return "Sin notas registradas"
        #como condicion puse para aprovar el promedio debe ser mayor o igual a 3.0
        elif self.promedio() >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"

class Sistema:
    def __init__(self):
        self.listaEstudiantes = [];
    
    def agregarEstudiante(self, Estudiante):
        # Uso for para recorrer la listaEstudiantes
        for i in range(len(self.listaEstudiantes)):
            print("entro al ciclo")
            # En cada iteracion, 'i' toma el valor del índice (0, 1, 2, ..., n)
            # con self.listaEstudiantes[i] se usa acceder al elemento en esa posicion
            if self.listaEstudiantes[i].nombre == Estudiante.nombre:
                print(f"Error: Ya existe un estudiante con el mismo nombre {Estudiante.nombre}")
                return False;
        # Si no se encontro ningun notas igual, procede a guardar.add(elemento)
        print("Va ah guardar")

        self.listaEstudiantes.append(Estudiante);
        print(f"El estudiante {Estudiante.nombre} se agrego exitosamente")

    def mostrarEstudiantes(self):
        # Verifico si la lista esta vacia
        print(f"\n========== Lista Estudiantes: ==========")
        # Recorre la lista con for
        for i in range(len(self.listaEstudiantes)):
            # Llama al método mostrarInfo de cada estudiante en segun la posicion en la lista
            self.listaEstudiantes[i].mostrarInfo()
        
    
    def buscarEstudiante(self, Buscar):
        # Busca un estudiante por su notas
        for i in range(len(self.listaEstudiantes)):
            # Compara el notas del estudiante en la posicion actual con el notas buscado
            if self.listaEstudiantes[i].nombre == Buscar:
                # Si lo encuentra, retorna el estudiante completo
                return self.listaEstudiantes[i]
        return
    
    def agregarNotaEstudiante(self, Buscar, nota):
        estudiante = self.buscarEstudiante(Buscar);
        # valido si estudiante tiene un valor con la condicion
        if estudiante:
            estudiante.agregarNota(nota)
            return estudiante
        else:
            print("Estudiante no encontrado")
            return

lista = Sistema()
while True:
    try:
        print("\n=== BIENVENIDO AL SISTEMA DE GESTIÓN DE ESTUDIANTES Y NOTAS. ===")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Agregar Nota")
        print("4. Ver promedio")
        print("5. Ver estado")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del Estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            #Creo un nuevo objeto estudiante
            nuevo_estudiante = Estudiante(nombre,edad)
            #lo agrego a la lista
            lista.agregarEstudiante(nuevo_estudiante);
            print(f"Nuevo Estudiante '{nombre}' se creo exitosamente!")

        elif opcion == 2:
            #muestro todos los estudiantes
            lista.mostrarEstudiantes();
        elif opcion == 3:
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nueva nota: "))
            #Con estas dos variables voy a filtrar en el buscador por el nombre y agrego la nota
            lista.agregarNotaEstudiante(nombre, nota)
        
        elif opcion == 4:
            nombre = input("Ingrese el nombre del estudiante: ")
            #busca por el atributo nombre de cada elemento de la lista
            estudiante = lista.buscarEstudiante(nombre)
            if estudiante:
                #despues de encontrar el estudiante aplico funciones sobre el elemento
                print(f"Promedio de {nombre} : {estudiante.promedio()}")
            else:
                print("Estudiante no encontrado")
        
        elif opcion == 5:
            nombre = input("Ingrese el nombre del estudiante: ")
            estudiante = lista.buscarEstudiante(nombre)
            if estudiante:
                print(f"Estado de {nombre} : {estudiante.estado()}")
            else:
                print("Estudiante no encontrado")
        elif opcion == 6:
            print("¡Gracias por usar el sistema gestion de estudiantes!!")
            #Salimos del ciclo while con un salto
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    except ValueError:
        print("Error: Entrada invalida")

"""
PREGUNTAS DE REFLEXIÓN
1 ¿Por qué las notas están encapsuladas?
R//  Por que notas se guardan en el atributo self.__notas que es un atributo privado, para proteger la informacion
2 ¿Cómo se calcula el promedio?
R// Con el metodo promedio, sum(se suman todas las notas) y len(se cuenta cuantas notas hay en el vector)
3 ¿Qué hace buscar_estudiante?
R// Recorre la listaEstudiantes y compara el nombre de cada objeto con el de Buscar, si lo ubica lo devuelde si no encuentra nada no devuelve nada.
"""