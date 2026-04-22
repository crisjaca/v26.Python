"""
    Ingieneria de Sistemas | 3 Semestre | 2 Corte
    Cristian David Jacanamijoy Narvaez
    
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

    def bucarEstudiante(self, nombreE):
        for i in range(len(self.listaEstudiantes)):
            if self.listaEstudiantes[i].nombre == nombreE:
                return self.listaEstudiantes[i].mostrarInfo()

    def eliminar(self, nombreE):
        for i in range(len(self.listaEstudiantes)):
            if self.listaEstudiantes[i].nombre == nombreE:
                self.listaEstudiantes.pop(i)
                return True

    def conteo(self):
        return len(self.listaEstudiantes)

lista = Sistema()

def registro():
    nombre_E = nombre.get()
    edad_E = edad.get()
    if nombre_E == "":
        resultado.config(text="Error: El nombre no puede estar vacío")
        return
    
    if edad_E == "":
        resultado.config(text="Error: La edad no puede estar vacía")
        return
    
    # valida que edad sea numérica
    try:
        edad_E = int(edad_E)  # la convierto a entero en caso de error es pq no es un numero
        if edad_E < 0:
            resultado.config(text="Error: La edad no puede ser negativa")
            return
    except ValueError:
        resultado.config(text="Error: La edad debe ser un numero válido")
        return
    
    if nombre_E and edad_E:
        nuevo_estudiante = Estudiante(nombre_E, edad_E)
        if lista.agregarEstudiante(nuevo_estudiante):
            resultado.config(text=f"¡Se ha registrado un nuevo estudiante {nombre_E}!")
        else:
            resultado.config(text=f"Error: estudiante {nombre_E} ya existe.")
    else:
        resultado.config(text="Por favor ingrese nombre y edad.")

    nombre.delete(0,tk.END)
    edad.delete(0,tk.END)

def listaEstudiante():
    resultado2.config(text=f"Lista Estudiantes: \n{lista.mostrarEstudiantes()}")
#ventana principal
def buscar_estudiante():
    nombre_buscar = txt_buscar.get()
    txt = lista.bucarEstudiante(nombre_buscar)
    if txt:
        resultado.config(text="Se encontro el registro.")
        resultado2.config(text=txt)
    else:
        resultado2.config(text="El estudiante no existe.")
    txt_buscar.delete(0,tk.END)

def eliminar_estudiante():
    eliminar = txt_buscar.get()

    if lista.eliminar(eliminar):
        resultado2.config(text="Se borro el registro.")
    else:
        resultado2.config(text="no se encontro el registro")
    txt_buscar.delete(0,tk.END)
def conteo_estudiantes():
    ct = lista.conteo()
    if ct:
        resultado2.config(text=f"la candidad de estudiantes es:{ct}")
    else:
        resultado2.config(text=f"no hay registros")

try:
    ventana = tk.Tk()
    ventana.title("Sistema Registro de Estudiantes")
    ventana.geometry("450x450");
    # titulo
    titulo = tk.Label(ventana, text="Sistema Registro de Estudiantes.", bg="#17C225", font=(500))
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


    buscar = tk.Label(ventana, text="Buscar Estudiante por nombre.").pack()
    txt_buscar = tk.Entry(ventana)
    txt_buscar.pack()
    bnt_buscar = tk.Button(ventana,text="Buscar",command=buscar_estudiante).pack()
    btn_eliminar = tk.Button(ventana,text="Eliminar",command=eliminar_estudiante).pack()
    btn_cantidad =  tk.Button(ventana,text="cantidad estudiantes",command=conteo_estudiantes).pack()
    ventana.mainloop()
except ValueError:
    resultado.config(text="Error: Entrada Invalida")
