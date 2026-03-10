
""""


"""

# registro = {
#     "nombre": "anabel",
#     "edad": 24,
#     "carrera":"Historia",
#     "lugar":"Kihoto"
# }

# for clave,valor in registro.items():
#     print(clave,": ",valor);

#declado el arreglo
registros={}

while True:
    print("=====    SISTEMA DE ESTUDIANTES   =====\n1) Agregar estudiante.\n2) Ver estudiante.\n3) Buscar estudiante\n4) Salir");

    opcion = input("Seleccione una opcion:")
    if opcion == "1":
        nombre = input("Nombre: ");
        edad = input("Edad: ")
        ciudad = input("Ciudad: ");
        
        registros[nombre] = {
        "edad": edad,
        "ciudad": ciudad,
    }
        print(registros)
    elif opcion =="2": 
        for nombre, datos in registros.items():
            print(nombre,": ",datos)
    elif opcion == "3":
        buscar = input("====    Busqueda estudiante    ===\nDigite el nombre:\n")
        if buscar in registros:
            print("Edad: ",registros[buscar]["edad"],"\nciudad: ",registros[buscar]["ciudad"])
            pass
        else:
            print("Error: Registro no existe")
    else:
        print("bye");break;
        

