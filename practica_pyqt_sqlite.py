import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QMessageBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario Inicial")
        self.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe tu nombre")
        
        self.button = QPushButton("Saludar")
        self.label = QLabel("")
        
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        self.button.clicked.connect(self.saludar)
        
    def saludar(self):
        nombre = self.input.text()
        self.label.setText(f"¡Hola, {nombre}!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())

# app.exec()                 
    
     
# label = QLabel("Formulario")
# label.show()
# app.exec()


# python -m pip install PyQt6
#         pip show PyQt6                                                                            