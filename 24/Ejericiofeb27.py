# Declaramos el diccionario 'inventario' con modelos de autos, cantidad disponible y precio por día
inventario = {
    'Sedan': {'cantidad': 5, 'precio_por_dia': 50},
    'SUV': {'cantidad': 3, 'precio_por_dia': 75},
    'Convertible': {'cantidad': 2, 'precio_por_dia': 100}
}

# Declaramos el diccionario 'clientes' donde cada cliente registrado almacenará autos alquilados, cantidad de días y costo total
clientes = {}

# Función para mostrar los vehículos disponibles
def mostrar_autos():
    print("Vehículos disponibles:")
    for modelo, datos in inventario.items():
        print(f"{modelo}: {datos['cantidad']} disponibles a ${datos['precio_por_dia']} por día")

# Función para alquilar un auto
def alquilar_auto():
    nombre_cliente = input("Ingrese su nombre: ")
    mostrar_autos()
    modelo_auto = input("Ingrese el modelo del auto que desea alquilar: ")

    if modelo_auto in inventario and inventario[modelo_auto]['cantidad'] > 0:
        dias = int(input("Ingrese la cantidad de días que desea alquilar el auto: "))
        costo_total = dias * inventario[modelo_auto]['precio_por_dia']
        
        inventario[modelo_auto]['cantidad'] -= 1
        
        if nombre_cliente in clientes:
            clientes[nombre_cliente].append({'modelo': modelo_auto, 'dias': dias, 'costo_total': costo_total})
        else:
            clientes[nombre_cliente] = [{'modelo': modelo_auto, 'dias': dias, 'costo_total': costo_total}]
        
        print(f"{nombre_cliente}, has alquilado un {modelo_auto} por {dias} días. Costo total: ${costo_total}")
    else:
        print("Lo siento, ese modelo no está disponible.")

# Función para devolver un auto
def devolver_auto():
    nombre_cliente = input("Ingrese su nombre: ")
    
    if nombre_cliente in clientes:
        print("Autos alquilados:")
        for idx, alquiler in enumerate(clientes[nombre_cliente]):
            print(f"{idx + 1}. Modelo: {alquiler['modelo']}, Días: {alquiler['dias']}, Costo total: ${alquiler['costo_total']}")
        
        idx_auto = int(input("Ingrese el número del auto que desea devolver: ")) - 1
        modelo_auto = clientes[nombre_cliente][idx_auto]['modelo']
        
        inventario[modelo_auto]['cantidad'] += 1
        
        clientes[nombre_cliente].pop(idx_auto)
        if not clientes[nombre_cliente]:
            del clientes[nombre_cliente]
        
        print(f"Has devuelto un {modelo_auto}.")
    else:
        print("No tienes autos alquilados.")

# Ejemplo de uso del programa
while True:
    print("\nGestión de alquiler de autos")
    print("1. Mostrar vehículos disponibles")
    print("2. Alquilar un auto")
    print("3. Devolver un auto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mostrar_autos()
    elif opcion == '2':
        alquilar_auto()
    elif opcion == '3':
        devolver_auto()
    elif opcion == '4':
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
