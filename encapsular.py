"""
     encapsulammiento 

"""

class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        #defino que es privado .__ defino que no se pueda usar en ninguna otra parte.
        self.__saldo += cantidad;

    def retirar(self, cantidad):
        if( cantidad <= self.__saldo):
            self.__saldo -= cantidad;
        else:
            print("¡¡Fondos insuficientes!!")
    def mostrar_saldo(Self):
        print("saldo: ",Self.__saldo)

cuenta = Cuenta(1000);

cuenta.depositar(500);

cuenta.retirar(200);

cuenta.mostrar_saldo();
# print(cuenta.__saldo)


"""
    EJERCICIO EN CLASE:

    
"""