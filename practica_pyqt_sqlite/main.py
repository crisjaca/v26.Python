import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget
)

app = QApplication(sys.argv)

ventana = QWidget()                             #Crea una ventana básica.
ventana.setWindowTitle("Registro de Usuarios")  #Define el título de la ventana
ventana.setGeometry(100, 100, 300, 150)         #Define la posición (x, y) y el tamaño (ancho, alto) de la ventana
ventana.show()                                  #Muestra la ventana en la pantalla

sys.exit(app.exec())                            #Inicia el bucle de eventos de la aplicación.




