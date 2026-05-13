import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuarios")  #Define el título de la ventana
        self.setGeometry(100, 100, 300, 150)         #Define la posición (x, y) y el tamaño (ancho, alto) de la ventana


app = QApplication(sys.argv)

window = MainWindow()                             #Crea una ventana básica.
window.show()                                  #Muestra la ventana en la pantalla

sys.exit(app.exec())                            #Inicia el bucle de eventos de la aplicación.




