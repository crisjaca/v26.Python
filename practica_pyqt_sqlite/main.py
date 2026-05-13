import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel

)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.crear_base_datos()
        self.setWindowTitle("Registro de Usuarios")  #Define el título de la ventana
        self.setGeometry(100, 100, 300, 150)         #Define la posición (x, y) y el tamaño (ancho, alto) de la ventana
        layout = QVBoxLayout() 
        self.input_nombre = QLineEdit() 
        self.input_nombre.setPlaceholderText("Ingrese el nombre") 
        self.input_email = QLineEdit() 
        self.input_email.setPlaceholderText("Ingrese el email") 
        self.boton_guardar = QPushButton("Guardar usuario") 
        self.label_mensaje = QLabel("") 
        layout.addWidget(self.input_nombre) 
        layout.addWidget(self.input_email) 
        layout.addWidget(self.boton_guardar) 
        layout.addWidget(self.label_mensaje)
        self.setLayout(layout)

        self.boton_guardar.clicked.connect(self.guardar_usuario)#Conecta el evento de clic del botón a la función guardar_usuario
        

    def guardar_usuario(self):
        nombre = self.input_nombre.text()
        email = self.input_email.text()

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios(nombre, email) VALUES (?, ?)", (nombre, email))    #Ejecuta una consulta SQL para insertar un nuevo usuario en la tabla "usuarios" con los valores proporcionados.
        conexion.commit()
        conexion.close()
        self.label_mensaje.setText("Usuario guardado correctamente")    #Actualiza el texto de la etiqueta para mostrar un mensaje de éxito.
        self.input_nombre.clear()
        self.input_email.clear()

    def crear_base_datos(self):
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS usuarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       email TEXT NOT NULL )
                       """)
        conexion.commit()
        conexion.close()
app = QApplication(sys.argv)

window = MainWindow()                             #Crea una ventana básica.
window.show()                                     #Muestra la ventana en la pantalla

sys.exit(app.exec())                            #Inicia el bucle de eventos de la aplicación.





