# # Interface de usuario
# # Importamos la libreria para Interfaces de escritorio

import tkinter as tk
# # Creamos e inicializamos la ventana principal de la aplicación
# ventana = tk.Tk();
# # Defie el texto que aparece en la barra de titulo de la ventana
# ventana.title("Mi primera app");
# # mantienen la app activa y ala espera de eventos del usuario
# ventana.mainloop();

# # widgets: es cualquier elemento visual de la Interfax.
# # label --> Muestra texto estatico en pantalla.
# # Button --> Ejecuta una funcion al hacer clic.
# # Entry --> Permite al usuario ingresar datos.

# #   MOSTRAR TEXTO:

# label = tk.Label(ventana,text= "Hola mundo")
# label.pack();

# # CAPTURAR DATOS

# entrada = tk.Entry(ventana)
# entrada.pack();

# # EJECUTAR ACCIONES
# boton = tk.Button(ventana,text="Presionar", command=accion)
# boton.pack()


def saludar():
    nombre = entrada.get()
    resultado.config(text=f"¡Hola {nombre}!")

ventana = tk.Tk()
ventana.title("Saludo Personalizado")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="SALUDAR",command=saludar)
boton.pack()

resultado = tk.Label(ventana,text="")
resultado.pack()

ventana.mainloop()