"""
INGIENERIA DE SISTEMAS | APLICATIVO SISTEMA ESCOLAR    
"""
import tkinter as tk

class Estudiante():
    def __init__(self, Nombre, edad, nota):
        self.nombre = Nombre
        self.edad = edad # atributo privado
        self.__notas = [nota]
        
    def agregar_nota(self, nueva_nota):
        
        self.__notas.append(int(nueva_nota))
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
            lista += str(self.__notas[i])+", "
        
        message = f"Nombre: {self.nombre}\nEdad: {self.edad}\nNota : {lista}\n"
        return message;
    
class sistema_Escolar:
    def __init__(self):
        self.lista_Estudiantes = []
            
    def agregar_Estudiantes(self, nuevo_estudiante):
        
        self.lista_Estudiantes.append(nuevo_estudiante)
        return True
    
    def buscar_Estudiantes(self, nombre):
        for i in range(len(self.lista_Estudiantes)):
            if self.lista_Estudiantes[i].nombre == nombre:
                return self.lista_Estudiantes[i]
            

    def mostrar_Lista_Estudiante(self):
        lista = f""

        for indice in range(len(self.lista_Estudiantes)):
            lista += self.lista_Estudiantes[indice].mostrarInfo()
        
        return lista
lista = sistema_Escolar()

def registro():
    nombre_E = nombre.get()
    edad_E = edad.get()
    nota_E = nota.get()
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
        nota_E = int(nota_E)

    except ValueError:
        resultado.config(text="Error: Entrada inválida")
        return
    if nombre_E and edad_E and nota_E >0 and nota_E < 100:
        nuevo_estudiante = Estudiante(nombre_E, edad_E, nota_E)
        if lista.agregar_Estudiantes(nuevo_estudiante):
            resultado.config(text=f"¡Se ha registrado un nuevo estudiante {nombre_E}!")
        else:
            resultado.config(text=f"Error: estudiante {nombre_E} ya existe.")
    else:
        resultado.config(text="Por favor ingrese nombre y edad.")

    nombre.delete(0,tk.END)
    edad.delete(0,tk.END)
    nota.delete(0,tk.END)

def lst_estudiantes():
    resultado2.config(text=f"Lista Estudiantes: \n{lista.mostrar_Lista_Estudiante()}")
def agregar_Nota():
    nombre2 = nombre.get()
    nota2 = nota.get()
    if lista.buscar_Estudiantes(nombre2):
        resultado.config(text="Busqueda exitosa!!")
        if lista.buscar_Estudiantes(nombre2).agregar_nota(nota2):
            resultado2.config(text="Se guardo la nueva nota con extito!!")
            nombre.delete(0,tk.END)
            nota.delete(0,tk.END)
            return
    else:
        resultado2.config(text="Error: Entrada Invalida")
        return
    if nota2 == "":
        resultado.config(text="Error: La nota no puede estar vacía")
        return
    

def buscar_E():
    nombre2 = nombre.get()

    if lista.buscar_Estudiantes(nombre2):
        resultado.config(text="Busqueda exitosa!!")
        resultado2.config(text=f"Resultado: \n {lista.buscar_Estudiantes(nombre2).mostrarInfo()}")
        nombre.delete(0,tk.END)
        return
    else:
        resultado2.config(text="Error: Usuario no encontrado")
        return

# def promedio():
#     nombre2 =n

try:
    ventana = tk.Tk()
    ventana.title("Sistema Registro de Estudiantes")
    ventana.geometry("500x500");
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

    # ==================================================
    txt_nota = tk.Label(ventana, text="Ingresa la nota:").pack()
    nota = tk.Entry(ventana)
    nota.pack()

    boton = tk.Button(ventana, text="Registrar", command=registro)
    boton.pack(pady=10)
    # ========================================================
    btn_agregar_nota = tk.Button(ventana, text="Agregar nota", command=agregar_Nota)
    btn_agregar_nota.pack()
    # ========================================================
    btn_buscar_estudiante = tk.Button(ventana,text="Buscar Estudiante", command=buscar_E)
    btn_buscar_estudiante.pack()
    # ========================================================
    # btn_promedio = tk.Button(ventana, text="Mostrar promedio", command=promedio)
    # btn_promedio.pack(pady=20)
    # ========================================================

    resultado = tk.Label(ventana, text="")
    resultado.pack()

    boton_lista = tk.Button(ventana, text="Lista Estudiantes", command=lst_estudiantes)
    boton_lista.pack(pady=20)

   

    resultado2 = tk.Label(ventana, text="")
    resultado2.pack()

    ventana.mainloop()
except Exception as e:
    raise e