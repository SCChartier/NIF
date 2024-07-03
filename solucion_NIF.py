#### import
import csv

#### FUNCIONES
def menu():
    print("### MENU PRINCIPAL ###")
    print("1. Grabar.")
    print("2. Buscar.")
    print("3. Guardar archivos.")
    print("4. Salir.")

def verificar_nif(nif):
    if nif[-4] != "-":
        return False
    else:
        p1, p2 = nif.split("-")
        if len(p1) != 8:
            return False
        else:
            try:
                int(p1)
                return True 
            except:
                return False

def verificar_full_name(nombre_completo):
    lista = nombre_completo.split(" ")
    if len(lista) != 2:
        return False
    else:
        nombre = lista[0]
        apellido = lista[1]
        if len(nombre) >= 8 and len(apellido) >= 8:
            return True
        else:
            return False

def buscar_nif(nif):
    if nif in d:
        print(d[nif])
    else:
        print("NIF no encontrado.")

def guardar_archivo(a, b):
    L = []
    for nif, datos in d.items():
        nombre = datos[0]
        edad = datos[1]
        if edad >= a and edad <= b:
            L.append([nombre, nif, edad])
    L.sort()
    ### escribir archivo
    name_arch = "edades_entre_" + str(a) + "_y_" + str(b) + ".csv"
    with open(name_arch, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(L)

#### MAIN
d = {}
while True:
    menu()
    op = input("Seleccione una opcion: ")
    if op == "1":
        print("Ingresando a opción 1.")
        nif = input("Ingrese NIF: ")
        resp_nif = verificar_nif(nif)
        if resp_nif == False:
            print("NIF invalido")
        else:
            print("NIF es valido")
            full_name = input("Ingrese nombre y apellido: ")
            resp_name = verificar_full_name(full_name)
            if resp_name == False:
                print("Nombre invalido")
            else:
                print("Nombre es valido")
                edad = int(input("Ingrese edad: "))
                if edad >= 15:
                    print("Edad valida")
                    d[nif] = [full_name, edad]
                    print("Datos ingresados exitosamente.")
                else:
                    print("Edad invalida")
    elif op == "2":
        print("Ingresando a opción 2.")
        nif_buscar = input("Ingrese NIF a buscar: ")
        buscar_nif(nif_buscar)
    elif op == "3":
        print("Ingresando a opción 3.")
        edad1 = int(input("Ingrese edad minima: "))
        edad2 = int(input("Ingrese edad maxima: "))
        guardar_archivo(edad1, edad2)
    elif op == "4":
        print("Saliendo del programa...")
        print("Sergio Campos\nVersión 1.0")
        break  
    else:
        print("Ingrese una opcion correcta (1, 2, 3 o 4)")