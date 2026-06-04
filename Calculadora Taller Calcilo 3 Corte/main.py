import sys
import math
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QSpinBox,
                             QPushButton, QTextEdit, QGroupBox, QRadioButton)
from PyQt6.QtCore import Qt

class VentanaCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora: cos(√x) por serie de Maclaurin")  #Titulo de la Ventana
        self.setGeometry(100, 100, 700, 500)    #Tamaño de la ventana

        # Widget central
        central_widget = QWidget()      #En la Intefaz visual esta generando un contenedor vacio para colocar los elementos de la interfaz
        self.setCentralWidget(central_widget) #Es necesario para que el contenedor se muestre en la ventana principal
        layout_principal = QVBoxLayout(central_widget)  #Organiza los elementos dentro del contenedor central

        # --- ENTRADAS ---
        layout_entradas = QHBoxLayout()     #Organiza los elementos de entrada en una fila horizontal
        self.input_x = QLineEdit("1.0")     #Campo de texto para ingresar el valor de x, con un valor inicial de 1.0
        self.input_x.setPlaceholderText("x (real)") #Texto de fondo que se muestra cuando el campo está vacío, indica que se espera un numero real para x
        self.spin_terminos = QSpinBox() #Este campo espara seleccionar el número de términos de la serie, con botones para aumentar o disminuir el valor
        self.spin_terminos.setRange(1, 100)     #Limita el rango entre 1 y 100 terminos esto evita calculos excesivamente largos o sin sentido.
        self.spin_terminos.setValue(10)         #Se declara un valor inicial de 10 terminos
        self.spin_terminos.setSuffix(" términos")   #Se agrego el sufijo para aclarar representa el número de términos de la serie

        layout_entradas.addWidget(QLabel("x ="))    #Etiqueta para indicar que el campo de texto es para ingresar el valor de x
        layout_entradas.addWidget(self.input_x)     #Agrega el campo de texto al layout de entradas, para que se muestre en la interfaz
        layout_entradas.addWidget(QLabel("N ="))    #Etiqueta que indica el campo de selección es para ingresar el número de términos de la serie
        layout_entradas.addWidget(self.spin_terminos)#Agrega el campo de selección al layout de entradas, para que se muestre en la interfaz
        layout_principal.addLayout(layout_entradas) #Agrega el layout de entradas al layout principal, para que se muestre en la interfaz

        # --- BOTON PARACALCULAR ---
        self.btn_calcular = QPushButton("Calcular")         #Boton que inicia la aproximacion de cos(√x) por la serie de Maclaurin
        self.btn_calcular.clicked.connect(self.calcular)    #Conecta el evento de clic del botón a la función calcular, para que se ejecute cuando el usuario haga clic en el botón
        layout_principal.addWidget(self.btn_calcular)       #Agrega el botón al layout principal, para que se muestre en la interfaz

        # --- ÁREA DE SALIDA (Muestra todos los símbolos) ---
        self.output = QTextEdit()       #Area para mostrar los resultados, permite mostrar texto
        self.output.setReadOnly(True)   #Hace que el area de texto sea de solo lectura, para que no se pueda modificar el resultado
        self.output.setFontFamily("Consolas")  #Fuente de texto monoespaciada para alinear mejor los resultados
        self.output.setFontPointSize(11)        #Tamaño de fuente para mejorar la lectura del resultado
        layout_principal.addWidget(self.output) #Agrego el area de salida al layout principal, para que se muestre en la interfaz

        # --- ENCABEZADO INICIAL ---
        self.mostrar_encabezado()   #Encabezado con la formula que se muestra al iniciar la aplicacion.

    def mostrar_encabezado(self):
        self.output.setPlainText(   
            "PROGRAMA PARA cos(√x) MEDIANTE SERIE DE MACLAURIN\n"
            "Serie: cos(√x) = Σ_{n=0}^∞ (-1)^n x^n / (2n)!\n"
            "Radio de convergencia: R = ∞ (converge para todo x real)\n"
            + "=" * 60 + "\n"
        )#Agrega un texto plano al area de salida.

    # ---------------- FUNCIONES DE CÁLCULO ----------------
    def cos_sqrt_series(self, x, n_terminos): 
        """Calcula la aproximación por la serie usando los coeficientes."""
        termino = 1.0
        aprox = termino
        for n in range(1, n_terminos): #Va desde 1 hasta el número de terminos seleccionado por el usuario, para calcular cada termino de la serie y sumarlo a la aproximación total.
            termino *= -x / ((2*n - 1) * (2*n))
            aprox += termino
        return aprox    #Devuelve la aproximación calculada por la serie de Maclaurin para cos(√x) con el número de términos especificado.

    def calcular(self):
        """Ejecuta el cálculo y muestra los resultados."""
        try:
            x = float(self.input_x.text())
            N = self.spin_terminos.value() #Se uso N para representar el número de terminos de la serie, es más claro que usar un nombre genérico como n_terminos en esta función.
        except ValueError:
            self.output.append("\n⚠️ ERROR: Ingresa un número válido para x.")#Dado si el texto no se puede convertir a numero, muestra el mensaje de arror.
            return

        # Limpia y muestra el encabezado antes de mostrar resultados.
        self.mostrar_encabezado() 

        # 1. Valor exacto (manejando x negativo) 
        if x < 0:   #si x es negativo, se calcula el valor exacto usando la función hiperbólica cosh, ya que cos(√x) para x < 0 se relaciona con cosh(√(-x)).
            exacto = math.cosh(math.sqrt(-x))
            self.output.append(f"\n📌 Nota: x = {x} < 0 → cos(√{x}) = cosh(√{-x})") 
        else:   #si x es positivo o cero, se calcula el valor exacto usando la función cos normal, ya que cos(√x) para x >= 0 se calcula directamente con cos.
            exacto = math.cos(math.sqrt(x))

        # 2. Aproximación por serie
        aprox = self.cos_sqrt_series(x, N) #Calcula la aproximacion de la serrie usando los coeficientes.

        # 3. Error
        error = abs(aprox - exacto) #Dado el valor exacto y la aproximación, se calcula el error absoluto como la diferencia entre ambos valores.
                                    #para medir la precisión de la aproximación obtenida por la serie de Maclaurin.

        # 4. Mostrar resultados
        self.output.append("\n📊 RESULTADOS:")
        self.output.append(f"   x = {x}")
        self.output.append(f"   N = {N} términos")
        self.output.append(f"   Aproximación por serie: {aprox:.10f}")
        self.output.append(f"   Valor exacto:           {exacto:.10f}")
        self.output.append(f"   Error absoluto:         {error:.6e}")

        # 5. Mostrar la serie paso a paso (para entender la convergencia)
        self.output.append("\n📈 EVOLUCIÓN DE LA APROXIMACIÓN (primeros 5 términos):")
        termino = 1.0
        suma = termino
        self.output.append(f"   n=0 → {suma:.8f}")
        for n in range(1, min(5, N)):
            termino *= -x / ((2*n - 1) * (2*n))
            suma += termino
            self.output.append(f"   n={n} → {suma:.8f}")

        # 6. Demostración del radio de convergencia
        self.output.append("\n📐 CÁLCULO DEL RADIO DE CONVERGENCIA:")
        self.output.append("   Coeficiente general: c_n = (-1)^n / (2n)!")
        self.output.append("   Criterio del cociente: |c_{n+1} / c_n| = 1 / [(2n+2)(2n+1)] → 0 cuando n → ∞")
        self.output.append("   Por lo tanto, R = ∞. La serie converge para todo x real.")

if __name__ == "__main__":  #Punto de entrada del programa, se ejecuta cuando se inicia la aplicación.
    app = QApplication(sys.argv)    #Crea una instancia de la aplicacion, para gestionar la interfaz grafica y las acciones del usuario.
    ventana = VentanaCalculadora()  
    ventana.show()              #Muestra la ventana de la calculadora en la pantalla, para que el usuario pueda interactuar con ella.
    sys.exit(app.exec())        #Inicia el bucle de eventos de la aplicación, que mantiene la interfaz responsive y 
                                # permite que el usuario interactúe con ella. El programa se cerrará cuando el usuario cierre la ventana.