import json

# Lista de países
paises = [
    "Estados Unidos (USA)", "China", "Colombia", "India", "Brasil", "México",
    "Canadá", "Rusia", "Japón", "Alemania", "Francia", "Reino Unido", "Italia",
    "España", "Australia", "Argentina", "Nigeria", "Sudáfrica", "Egipto",
    "Turquía", "Indonesia", "Arabia Saudita", "Corea del Sur", "Sudán", "Kenia",
    "Marruecos", "Tailandia", "Polonia", "Pakistán", "Vietnam", "Filipinas",
    "Irán", "Venezuela", "Chile", "Perú", "Ecuador", "Bolivia", "Paraguay",
    "Uruguay", "Guatemala", "Honduras", "El Salvador", "Costa Rica", "Panamá",
    "Portugal", "Grecia", "Ucrania", "Suecia", "Noruega", "Nueva Zelanda"
]

# Funciones para manejar datos
def cargar_datos():
    try:
        with open("poblacion.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_datos(datos):
    with open("poblacion.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Menús
def mostrar_menu_principal():
    print("Bienvenido a datos poblacionales globales")
    print("Presiona la letra para acceder a los archivos:")
    print("A. Ingresar datos")
    print("B. Informes")
    print("C. Reportes")
    print("D. Salir")

def mostrar_menu_ingresar_datos():
    print("\nSelecciona una opción:")
    print("A. Seleccionar un país existente")
    print("B. Ingresar un nuevo país")

def mostrar_menu_paises():
    print("\nLista de países:")
    for i, pais in enumerate(paises, start=1):
        print(f"{i}. {pais}")

def menu_informes():
    while True:
        print("\n1. Población por año")
        print("2. Crecimiento poblacional")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_paises()
            seleccion = int(input("Seleccione un país por su número: "))
            if seleccion > 0 and seleccion <= len(paises):
                pais = paises[seleccion - 1]
                año = int(input("Digite el año (<= 2023): "))
                if año > 2023:
                    print("Error: El año debe ser menor o igual a 2023.")
                else:
                    mostrar_datos_poblacion(pais, año)
            else:
                print("Selección no válida.")
        elif opcion == "2":
            mostrar_menu_paises()
            seleccion = int(input("Seleccione un país por su número: "))
            if seleccion > 0 and seleccion <= len(paises):
                pais = paises[seleccion - 1]
                año1 = int(input("Ingrese el año inicial: "))
                año2 = int(input("Ingrese el año final: "))
                calcular_crecimiento(pais, año1, año2)
            else:
                print("Selección no válida.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")

def menu_reportes():
    while True:
        print("\nA. Países")
        print("B. Población total de los países")
        print("C. Países con crecimiento del 2%")
        print("D. Regresar")
        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            mostrar_menu_paises()
            # Aquí puedes implementar las opciones avanzadas del menú "A".
        elif opcion == "B":
            print("Función para mostrar población total en desarrollo.")
        elif opcion == "C":
            print("Función para mostrar países con crecimiento del 2% en desarrollo.")
        elif opcion == "D":
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")

# Funciones de manejo de datos
def mostrar_datos_poblacion(pais, año):
    datos = cargar_datos()
    if pais in datos and str(año) in datos[pais]:
        print(json.dumps(datos[pais][str(año)], indent=4))
    else:
        print("Datos no disponibles para este país y año.")

def calcular_crecimiento(pais, año1, año2):
    datos = cargar_datos()
    if pais in datos and str(año1) in datos[pais] and str(año2) in datos[pais]:
        poblacion1 = datos[pais][str(año1)]["valor"]
        poblacion2 = datos[pais][str(año2)]["valor"]
        crecimiento = poblacion2 - poblacion1
        print(f"El crecimiento en este periodo fue de: {crecimiento} personas.")
    else:
        print("Datos insuficientes para realizar el cálculo.")

# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ").upper()

        if opcion_principal == "A":
            mostrar_menu_ingresar_datos()
            # Implementar ingreso de datos.
        elif opcion_principal == "B":
            menu_informes()
        elif opcion_principal == "C":
            menu_reportes()
        elif opcion_principal == "D":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
import json

# Lista de países
paises = [
    "Estados Unidos (USA)", "China", "Colombia", "India", "Brasil", "México",
    "Canadá", "Rusia", "Japón", "Alemania", "Francia", "Reino Unido", "Italia",
    "España", "Australia", "Argentina", "Nigeria", "Sudáfrica", "Egipto",
    "Turquía", "Indonesia", "Arabia Saudita", "Corea del Sur", "Sudán", "Kenia",
    "Marruecos", "Tailandia", "Polonia", "Pakistán", "Vietnam", "Filipinas",
    "Irán", "Venezuela", "Chile", "Perú", "Ecuador", "Bolivia", "Paraguay",
    "Uruguay", "Guatemala", "Honduras", "El Salvador", "Costa Rica", "Panamá",
    "Portugal", "Grecia", "Ucrania", "Suecia", "Noruega", "Nueva Zelanda"
]

# Funciones para manejar datos
def cargar_datos():
    try:
        with open("poblacion.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_datos(datos):
    with open("poblacion.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Menús
def mostrar_menu_principal():
    print("Bienvenido a datos poblacionales globales")
    print("Presiona la letra para acceder a los archivos:")
    print("A. Ingresar datos")
    print("B. Informes")
    print("C. Reportes")
    print("D. Salir")

def mostrar_menu_ingresar_datos():
    print("\nSelecciona una opción:")
    print("A. Seleccionar un país existente")
    print("B. Ingresar un nuevo país")

def mostrar_menu_paises():
    print("\nLista de países:")
    for i, pais in enumerate(paises, start=1):
        print(f"{i}. {pais}")

def menu_informes():
    while True:
        print("\n1. Población por año")
        print("2. Crecimiento poblacional")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_paises()
            seleccion = int(input("Seleccione un país por su número: "))
            if seleccion > 0 and seleccion <= len(paises):
                pais = paises[seleccion - 1]
                año = int(input("Digite el año (<= 2023): "))
                if año > 2023:
                    print("Error: El año debe ser menor o igual a 2023.")
                else:
                    mostrar_datos_poblacion(pais, año)
            else:
                print("Selección no válida.")
        elif opcion == "2":
            mostrar_menu_paises()
            seleccion = int(input("Seleccione un país por su número: "))
            if seleccion > 0 and seleccion <= len(paises):
                pais = paises[seleccion - 1]
                año1 = int(input("Ingrese el año inicial: "))
                año2 = int(input("Ingrese el año final: "))
                calcular_crecimiento(pais, año1, año2)
            else:
                print("Selección no válida.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")

def menu_reportes():
    while True:
        print("\nA. Países")
        print("B. Población total de los países")
        print("C. Países con crecimiento del 2%")
        print("D. Regresar")
        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            mostrar_menu_paises()
            # Aquí puedes implementar las opciones avanzadas del menú "A".
        elif opcion == "B":
            print("Función para mostrar población total en desarrollo.")
        elif opcion == "C":
            print("Función para mostrar países con crecimiento del 2% en desarrollo.")
        elif opcion == "D":
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")

# Funciones de manejo de datos
def mostrar_datos_poblacion(pais, año):
    datos = cargar_datos()
    if pais in datos and str(año) in datos[pais]:
        print(json.dumps(datos[pais][str(año)], indent=4))
    else:
        print("Datos no disponibles para este país y año.")

def calcular_crecimiento(pais, año1, año2):
    datos = cargar_datos()
    if pais in datos and str(año1) in datos[pais] and str(año2) in datos[pais]:
        poblacion1 = datos[pais][str(año1)]["valor"]
        poblacion2 = datos[pais][str(año2)]["valor"]
        crecimiento = poblacion2 - poblacion1
        print(f"El crecimiento en este periodo fue de: {crecimiento} personas.")
    else:
        print("Datos insuficientes para realizar el cálculo.")

# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ").upper()

        if opcion_principal == "A":
            mostrar_menu_ingresar_datos()
            # Implementar ingreso de datos.
        elif opcion_principal == "B":
            menu_informes()
        elif opcion_principal == "C":
            menu_reportes()
        elif opcion_principal == "D":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
