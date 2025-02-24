import string
import random 

def generar_contraseñas_numerica():
    return "" .join(random.choices(string.digits,k=6))
def generar_contraseñas_numerica():
    return "" .join(random.choices(string.ascii_letters + string.digits,k=8))
def generar_contraseñas_numerica():
    return "" .join(random.choices(string.caracteres , k=10))

def mostrar_menu():
    print ("(Elija la contraseña que desea generar digitando los numeros)")
    print ("1.Generar contraseña numérica (6 dígitos)")
    print ("2.Generar contraseña alfanumérica (8 caracteres)")
    print ("3.Generar contraseña con caracteres especiales (10 caracteres)")
    print ("4.salir")

while True:
    mostrar_menu()
    opcion = input("Introduce una opción: ")

    if opcion == '1':
        print("Contraseña numérica generada:", generar_contraseña_numerica ())
    elif opcion == '2':
        print("Contraseña alfanumérica generada:", generar_contraseña_alfanumerica())
    elif opcion == '3':
        print("Contraseña con caracteres especiales generada:", generar_contraseña_caracteres_especiales())
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
