"""
    Ingieneria de Sistemas | 3 Semestre

"""
import tkinter as tk


class Estudiante:
    #Inicio con el constructor recibiendo los datos: nombre, edad, notas.
    def __init__(self, Nombre, Edad):
        self.nombre = Nombre;
        self.edad = Edad;

        # declaro con el constructor dnd se van a guardar los datos ingresados
    
    def mostrarInfo(self):
        mensaje1 =f"***************************************\nNombre: {self.nombre}\nEdad: {self.edad}\n"
        return mensaje1;

class Sistema:
    def __init__(self):
        self.listaEstudiantes = [];
    
    def agregarEstudiante(self, Estudiante):
        # Uso for para recorrer la listaEstudiantes
        for i in range(len(self.listaEstudiantes)):
            # En cada iteracion, 'i' toma el valor del índice (0, 1, 2, ..., n)
            # con self.listaEstudiantes[i] se usa acceder al elemento en esa posicion
            if self.listaEstudiantes[i].nombre == Estudiante.nombre:
                print(f"Error: Ya existe un estudiante con el mismo nombre {Estudiante.nombre}")
                return False;
    
        self.listaEstudiantes.append(Estudiante);
        print(f"El estudiante {Estudiante.nombre} se agrego exitosamente")
        return True;

    def mostrarEstudiantes(self):
        mensaje_lista=""
        # Verifico si la lista esta vacia
        if self.listaEstudiantes:
            
            # Recorre la lista con for
            for i in range(len(self.listaEstudiantes)):
                # Llama al método mostrarInfo de cada estudiante en segun la posicion en la lista
                mensaje_lista += self.listaEstudiantes[i].mostrarInfo()
        else:
            mensaje_lista = "No hay estudiantes registrados."
        
        return mensaje_lista;


lista = Sistema()

def registro():
    nombre_E = nombre.get()
    edad_E = edad.get()
    if nombre_E and edad_E:
        nuevo_estudiante = Estudiante(nombre_E, edad_E)
        if lista.agregarEstudiante(nuevo_estudiante):
            resultado.config(text=f"¡Se ha registrado un nuevo estudiante {nombre_E}!")
        else:
            resultado.config(text=f"Error: estudiante {nombre_E} ya existe.")
    else:
        resultado.config(text="Por favor ingrese nombre y edad.")

def listaEstudiante():
    resultado2.config(text=f"Lista Estudiantes: \n{lista.mostrarEstudiantes()}")
#ventana principal

ventana = tk.Tk()
ventana.title("Sistema Registro de Estudiantes")

nombre = tk.Entry(ventana)
nombre.pack()
edad = tk.Entry(ventana)
edad.pack()

boton = tk.Button(ventana, text="Registrar", command=registro)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

boton_lista = tk.Button(ventana, text="Lista Estudiantes", command=listaEstudiante)
boton_lista.pack()

resultado2 = tk.Label(ventana, text="")
resultado2.pack()

ventana.mainloop()
# try:
#     pass
# except ValueError:
#     print("Error: Entrada Invalida")
        