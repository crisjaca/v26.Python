"""
Martes 03 de Marzo del 2026

Litar un arrreglo

"""

# frutas = ["manzanas","banana","pera"];
# frutas.append("fresa");

# frutas.remove("pera");

# for i in range(len(frutas)):
#     print(frutas[i])


# ListaNum = [];

# for i in range(5):
    
#     num= int(input(f"Digita el {i+1} valor"));
#     ListaNum.append(num);
#     pass

# print("LISTA: ",ListaNum);
# print("Mayor: ",max(ListaNum));
# print("Menor: ",min(ListaNum));
# print("Promedio: ",sum(ListaNum)/len(ListaNum));

def menu():
    print("\n--- Lista de Tareas ---\n1. Ver tareas\n2. Agregar tarea\n3. Eliminar tarea\n4. Salir");
    return;
    
def lista():
    if tareas:
        mensaje = print(tareas);
    else:
        mensaje = print("no hay datos");
    return mensaje;

def eliminar():

    posicion = int(input("ELIMINAR TAREA: "));

    print(f"vas a eliminar ",posicion," = ")
    if posicion !=0:
        tareas.pop(posicion);
    else:
        print("no hay nada");
    return tareas;

def promedio():

    if tareas:
        prom = sum(tareas)/len(tareas);
        print(" .. "+prom)
    else:
        print("no hay datos");
    return
tareas = []

valida = True;
posicion = 0;
while valida:
    try:
        menu();
        opc = int(input("Selecciona una opcion:"));

        if opc == 1:
            lista();
        elif opc ==2:
            nota = float(input("Ingresa la nota: "));
            tareas.append(nota);
        elif opc == 3:
            eliminar()
        elif opc == 4:
            valida=False;
        elif opc == 5:
            promedio();
        else:
            print("_________________")
    except ValueError:
        print("Error: Entrada Invalida")

