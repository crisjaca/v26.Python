

# def sumar(a,b):
#     return a+b;

# resultado =sumar(5,3);
# print(resultado);



# def numpar(num):
#     return num%2==0;
    
# try:
#     numero = int(input("Digite un numero: "));
#     if numpar(numero):
#         print("Es par")
#     else:
#         print("Es impar")
# except Exception as e:
#     print("Error: ")
#     raise e


def suma(a,b):
    return a+b;
def resta(a,b):
    return a-b;
def dividir(a,b):
    return a/b;
def multiplicar(a,b):
    return a*b;
def menu():
    menu = print("***************************************\nCalculadora basica\n1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n5. Salir\n Selecciona una opcion:")
    return menu;

validar = True;
while validar:
    try:
        menu()
        opc = int(input());
        if opc != 0 and opc!=5:
            num2 = int(input("Ingrese el segundo numero: "));
            num1 = int(input("Ingrese el primer numero: "));
            if opc ==1 :
                resultado = suma(num1,num2);
            elif opc ==2 :
                resultado = resta(num1,num2);
            elif opc == 3:
                resultado = multiplicar(num1,num2);
            elif opc == 4:
                if num1 != 0 and num2!= 0:
                    resultado = dividir(num1,num2);
                else: 
                    print("No se puede dividir por 0")
                    break;
            print("El resultado es: ",resultado)
        elif opc == 5:
            print("Adios");
            validar= False;
        else:
            print("Ingresa un valor")
    except ValueError:
        print("Error");



