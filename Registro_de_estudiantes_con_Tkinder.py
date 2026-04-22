"""
    Ingieneria de Sistemas | 3 Semestre | 2 Corte
    Cristian David Jacanamijoy Narvaez
    
    ¡5.0!!✅👽
"""
import tkinter as tk

class Estudiante:
    #Inicio con el constructor recibiendo los datos: nombre, edad 
    def __init__(self, Nombre, Edad):
    # declaro con el constructor dnd se van a guardar los datos ingresados
        self.nombre = Nombre;
        self.edad = Edad;
    
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
            # esta condicion compara el atributo nombre del constructor con el atributo nombre de cada indice de la lista
            if self.listaEstudiantes[i].nombre == Estudiante.nombre:
                return False;
            
        self.listaEstudiantes.append(Estudiante);
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
    # strip() elimina espacios al inicio y final
    if nombre_E.strip() == "" or edad_E.strip() == "":
        resultado.config(text="Error: No se permiten campos vacíos")
        nombre.delete(0, tk.END)
        edad.delete(0, tk.END)
        return
    # Valido que edad sea un numero.
    # atrapo el error
    try:
        edad_E = int(edad_E)  # Aqui convierto el dato a entero, en caso de error es pq no es un numero y sale
        #verifico que no sea negativa la edad
        if edad_E < 0:
            resultado.config(text="Error: La edad no puede ser negativa")
            return
    except ValueError:
        resultado.config(text="Error: La edad debe ser un numero válido")
        return
    # verifico que los valores no esten vacios, en caso de estar vacios muestra el mensaje
    nuevo_estudiante = Estudiante(nombre_E, edad_E)

    if lista.agregarEstudiante(nuevo_estudiante):
        resultado.config(text=f"¡Se ha registrado un nuevo estudiante {nombre_E}!")
    else:
        resultado.config(text=f"Error: estudiante {nombre_E} ya existe.")

    nombre.delete(0,tk.END)
    edad.delete(0,tk.END)

def listaEstudiante():
    resultado2.config(text=f"Lista Estudiantes: \n{lista.mostrarEstudiantes()}")
#ventana principal

try:
    ventana = tk.Tk()
    ventana.title("Sistema Registro de Estudiantes")
    ventana.geometry("450x450");
    # titulo
    titulo = tk.Label(ventana, text="Registro de Estudiantes.", bg="#17C225", font=(500))
    titulo.pack()

    txt_nombre = tk.Label(ventana, text="Nombre:")
    txt_nombre.pack()
    nombre = tk.Entry(ventana)
    nombre.pack()
    txt_edad = tk.Label(ventana, text="Edad:")
    txt_edad.pack()
    edad = tk.Entry(ventana)
    edad.pack()

    boton = tk.Button(ventana, text="Registrar", command=registro)
    boton.pack(pady=10)

    resultado = tk.Label(ventana, text="")
    resultado.pack()

    boton_lista = tk.Button(ventana, text="Lista Estudiantes", command=listaEstudiante)
    boton_lista.pack(pady=10)

    resultado2 = tk.Label(ventana, text="")
    resultado2.pack()

    ventana.mainloop()
except ValueError:
    resultado.config(text="Error: Entrada Invalida")
    