"""
    Sistema de Registro de Mascotas
    Ingienería de Sistemas
    Cristian David Jacanamijoy Narvaez
    
"""

import sys
import sqlite3

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel
)
class MainWindow (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Registro de Mascotas")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.label_titulo = QLabel("Registro de Mascotas")

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre de la mascota")

        self.input_tipo = QLineEdit()
        self.input_tipo.setPlaceholderText("Tipo de mascota")

        self.input_duenio = QLineEdit()
        self.input_duenio.setPlaceholderText("Nombre del dueño")

        self.input_edad = QLineEdit()
        self.input_edad.setPlaceholderText("Edad de la mascota")

        self.input_raza = QLineEdit()
        self.input_raza.setPlaceholderText("Raza de la mascota")

        self.btn_guardar = QPushButton("Guardar Registro")
        # -------------------------------------------------
        self.btn_mostrar = QPushButton("Mostrar Registros")
        # -------------------------------------------------
        self.btn_limpiar = QPushButton("Limpiar")
        
        self.label_mensaje = QLabel("")

        layout.addWidget(self.label_titulo)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.input_tipo)
        layout.addWidget(self.input_duenio)
        layout.addWidget(self.input_edad)
        layout.addWidget(self.input_raza)
        layout.addWidget(self.btn_guardar)
        layout.addWidget(self.btn_mostrar)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.label_mensaje)

        self.setLayout(layout)
        self.btn_guardar.clicked.connect(self.guardar_mascota)
        self.btn_mostrar.clicked.connect(self.mostrar_mascotas)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.crear_base_datos()
    
    def guardar_mascota(self):
        nombre = self.input_nombre.text()
        tipo = self.input_tipo.text()
        duenio = self.input_duenio.text()
        edad = self.input_edad.text()
        raza = self.input_raza.text()

        if nombre == "" or tipo == "" or duenio == "" or edad == "" or raza == "":
            self.label_mensaje.setText("Error, los campos no pueden estar vacios.")
            return
        
        conexion = sqlite3.connect("veterinaria.db")
        cursor = conexion.cursor()
        # -------------------------------------------------
        # Inserto el registo en la tabla "registro_mascotas" con los valores de entrada.
        cursor.execute(
            "INSERT INTO registro_mascotas(nombre, tipo, dueño, edad, raza) VALUES (?, ?, ?, ?, ?)",
            (nombre, tipo, duenio, edad, raza)
        )
        conexion.commit()
        conexion.close()

        self.label_mensaje.setText("Mascota guardada correctamente")

    
    def crear_base_datos(self):
        # Creo la base de datos "veterinaria.db" y la tabla "registro_mascotas" si no existe.
        conexion = sqlite3.connect("veterinaria.db")
        cursor = conexion.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS registro_mascotas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       tipo TEXT NOT NULL,
                       dueño TEXT NOT NULL,
                       edad INTEGER,
                       raza TEXT
                       )
                       """)
        conexion.commit()
        conexion.close()

    def mostrar_mascotas(self):
        # Conecto a la base de datos y obtengo todos los registros de la tabla "registro_mascotas".
        conexion = sqlite3.connect("veterinaria.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registro_mascotas")
        registros = cursor.fetchall()
        
        # -------------------------------------------------
        # Estoy cocatenando los registros en un mensaje para mostrarlo todo junto en mensaje.
        mensaje = "Registros de Mascotas:\n"
        # Recorro cada registro obtenido de la base de datos y lo agrego al mensaje.
        for registro in registros:
            # Cada registro tiene unos campos de la tabla por lo que accedo a cada campo por su índice.
            mensaje += f"ID: {registro[0]}\nNombre: {registro[1]}\nTipo: {registro[2]}\nDueño: {registro[3]}\nEdad: {registro[4]}\nRaza: {registro[5]}\n____________________________\n"
        # cierro la conexion despues de tener los registros.
        conexion.close()
        self.label_mensaje.setText(mensaje)

    def limpiar_campos(self):
        self.input_nombre.clear()
        self.input_tipo.clear()
        self.input_duenio.clear()
        self.input_edad.clear()
        self.input_raza.clear()
        self.label_mensaje.setText("Campos limpiados")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())