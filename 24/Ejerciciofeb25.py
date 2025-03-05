tienda={
    "menta":300
    "Chocoramo":1000
    "Esfero":2700
    "Chocolatina":2500
}
print("Los productos disponibles son: ")
for i in productos:
    print("-",i)
producto = input ("ingrese el producto deseado")
if producto in productos:
    cantidad = int(inpt("ingrese la cantidad del producto"))
    total = productos.get(producto) * cantidad
    print("El total a pagar es ", total, "pesos")
else:
    print("lea bien")
