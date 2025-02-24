import random

# Lista predefinida de palabras
palabras = ["manzana", "elefante", "mesa", "silla", "amarillo", "oso", "uña", "árbol", "luz", "zapato"]

def es_palabra_valida(palabra, ultima_letra, usadas):
    return palabra in palabras and palabra not in usadas and palabra[0] == ultima_letra

def mostrar_estado_juego(palabra_actual):
    print(f"\nPalabra actual: {palabra_actual}")
    print(f"Última letra: {palabra_actual[-1]}")

def juego_encadenar_palabras():
    print("¡Bienvenidos al juego de encadenar palabras!")
    print("Reglas del juego:")
    print("- Cada jugador debe ingresar una palabra que comience con la última letra de la palabra anterior.")
    print("- La palabra debe existir en la lista predefinida y no puede ser duplicada.")
    print("- Escribe 'salir' para terminar el juego en cualquier momento.\n")
    
    palabra_actual = random.choice(palabras)
    usadas = [palabra_actual]
    mostrar_estado_juego(palabra_actual)

    while True:
        palabra = input("Ingresa una palabra: ").lower()
        
        if palabra == "salir":
            print("¡Gracias por jugar!")
            break

        if es_palabra_valida(palabra, palabra_actual[-1], usadas):
            usadas.append(palabra)
            palabra_actual = palabra
            mostrar_estado_juego(palabra_actual)
        else:
            print("Palabra no válida. Intenta de nuevo.")
            
juego_encadenar_palabras()
