#### FUNCIONES
def menu():
    print("### MENU PRINCIPAL ###")
    print("1. Grabar.")
    print("2. Buscar.")
    print("3. Guardar archivos.")
    print("4. Salir.")

#### MAIN
while True:
    menu()
    op = input("Seleccione una opcion: ")
    if op == "1":
        print("Ingresando a opción 1.")
    elif op == "2":
        print("Ingresando a opción 2.")
    elif op == "3":
        print("Ingresando a opción 3.")
    elif op == "4":
        print("Saliendo del programa...")
        print("Sergio Campos\nVersión 1.0")
        break  
    else:
        print("Ingrese una opcion correcta (1, 2, 3 o 4)")