def recolectar_datos():
    usuario = {}
    usuario['nombre'] = input("¿Cuál es tu nombre? ")
    usuario['edad'] = input("¿Cuántos años tienes? ")
    usuario['direccion'] = input("¿Cuál es tu dirección? ")
    usuario['telefono'] = input("¿Cuál es tu número de teléfono? ")
    return usuario
def mostrar_datos(usuario):
    mensaje = f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}."
    print(mensaje)
def programa_principal():
    usuario = recolectar_datos()
    mostrar_datos(usuario)

if __name__ == "__main__":
    programa_principal()
