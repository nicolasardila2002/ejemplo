import json

def bienvenida():
    print("Bienvenido a datos poblacionales globales")

def menu_principal():
    print("\nPresiona la letra para acceder a los archivos:")
    print("A. Ingresar datos")
    print("B. Informes")
    print("C. Reportes")
    print("D. Salir")

def seleccionar_pais():
    paises = [
        "Estados Unidos (USA)", "China", "Colombia", "India", "Brasil", "México", "Canadá", "Rusia", "Japón", "Alemania",
        "Francia", "Reino Unido", "Italia", "España", "Australia", "Argentina", "Nigeria", "Sudáfrica", "Egipto", "Turquía",
        "Indonesia", "Arabia Saudita", "Corea del Sur", "Sudán", "Kenia", "Marruecos", "Tailandia", "Polonia", "Pakistán",
        "Vietnam", "Filipinas", "Irán", "Venezuela", "Chile", "Perú", "Ecuador", "Bolivia", "Paraguay", "Uruguay",
        "Guatemala", "Honduras", "El Salvador", "Costa Rica", "Panamá", "Portugal", "Grecia", "Ucrania", "Suecia",
        "Noruega", "Nueva Zelanda"
    ]
    for i, pais in enumerate(paises, 1):
        print(f"{i}. {pais}")
    pais_seleccionado = int(input("Seleccionar país eligiendo número de país: "))
    return paises[pais_seleccionado - 1]

def ingresar_datos():
    pais = seleccionar_pais()
    ano = input("Año: ")
    poblacion = input("Población: ")
    return {"ano": ano, "pais": pais, "poblacion": poblacion}

def informes():
    print("\n1. Población por año")
    print("2. Crecimiento poblacional")
    print("3. Regresar")
    opcion = input("Selecciona una opción: ")
    return opcion

def reportes():
    print("\nA. India")
    print("B. Países")
    print("C. Población total de los países")
    print("D. Países con crecimiento del 2%")
    print("E. Regresar")
    opcion = input("Selecciona una opción: ")
    return opcion

def sub_menu_reportes(opcion):
    if opcion == "A":
        print("\n1. Datos de 2000 a 2023")
        print("2. Datos de cuenta atrás a partir de 2023")
        print("3. Datos anteriores al 2000")
        sub_opcion = input("Selecciona una opción: ")
        return sub_opcion
    elif opcion == "C":
        print("\nA. Datos totales de la población antes del año 2000")
        print("B. Datos totales de la población después del año 2010")
        sub_opcion = input("Selecciona una opción: ")
        return sub_opcion
    elif opcion == "D":
        print("\nA. Países con crecimiento del 2%")
        sub_opcion = input("Selecciona una opción: ")
        return sub_opcion
    else:
        return None

def main():
    bienvenida()
    datos = []

    while True:
        menu_principal()
        opcion = input("Selecciona una opción: ").upper()

        if opcion == "A":
            datos.append(ingresar_datos())
        elif opcion == "B":
            opcion_b = informes()
            if opcion_b == "1":
                pais = seleccionar_pais()
                ano = input("Digite año: ")
                if int(ano) > 2023:
                    print("Error: digite año menor o igual a 2023")
                else:
                    for dato in datos:
                        if dato["pais"] == pais and dato["ano"] == ano:
                            print(json.dumps(dato, indent=4))
            elif opcion_b == "2":
                pais = seleccionar_pais()
                ano1 = input("Digite año 1: ")
                ano2 = input("Digite año 2: ")
                poblacion1 = poblacion2 = 0
                for dato in datos:
                    if dato["pais"] == pais:
                        if dato["ano"] == ano1:
                            poblacion1 = int(dato["poblacion"])
                        elif dato["ano"] == ano2:
                            poblacion2 = int(dato["poblacion"])
                crecimiento = poblacion2 - poblacion1
                print(f"El crecimiento en este periodo fue de: {crecimiento}")
            elif opcion_b == "3":
                continue
        elif opcion == "C":
            opcion_c = reportes()
            sub_opcion_c = sub_menu_reportes(opcion_c.upper())
            # Implementación de cada subopción aquí según las instrucciones dadas
            # ...
        elif opcion == "D":
            break

if __name__ == "__main__":
    main()

