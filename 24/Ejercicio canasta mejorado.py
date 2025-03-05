# Productos disponibles en la tienda
productos = {
    "Menta": 300,
    "Chocorramo": 1000,
    "lapicero": 2700,
    "Chocolatina": 2500
}

# Carrito de compras inicial
cesta = {}

def mostrar_carrito(cesta):
    print("****Su carrito tiene***")
    for llave, valor in cesta.items():
        print(valor, " - ", llave)
    print("***Fin del carrito***")

def agregar_al_carrito(productos, cesta):
    print("****Agregar al carrito***")
    while True:
        print("Los productos disponibles son: ")
        for i in productos:
            print("- ", i)
        producto = input("Ingrese el producto que desea comprar o 0 para salir: ")
        if producto in productos:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            cesta[producto] = cantidad
        elif producto == "0":
            print("***Fin******")
            break
        else:
            print("El producto no existe")

def vaciar_carrito(cesta):
    cesta.clear()
    print("Vuelve pronto.... :(")

def calcular_total(cesta, productos):
    print("***Sus productos son***")
    total = 0
    for llave, valor in cesta.items():
        print(llave, " - cantidad: ", valor, " - precio: ", productos.get(llave))
        total += valor * productos.get(llave)
    print("El total a pagar es: ", total)

def tienda():
    while True:
        print("*****Bienvenido a la tienda de Karol*****")
        print("Ingrese\n1. Para ver el carrito\n2. Para añadir producto al carrito\n3. Para vaciar carrito\n4. Para calcular el total a pagar\n5. Para salir")
        opc = input("Ingrese la opción requerida: ")
        if opc == "1":
            mostrar_carrito(cesta)
        elif opc == "2":
            agregar_al_carrito(productos, cesta)
        elif opc == "3":
            vaciar_carrito(cesta)
        elif opc == "4":
            calcular_total(cesta, productos)
        elif opc == "5":
            print("Saliendo...")
            break
        else:
            print("Lea bien...")

# Inicia la tienda
tienda()
