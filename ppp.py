def mostrar_bienvenida():
    print("¡Bienvenido al generador interactivo de la Secuencia de Fibonacci!")
    print("La Secuencia de Fibonacci comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")
    print("Puedes ingresar el valor de 'n' para generar la secuencia hasta el enésimo término.")

def obtener_valor_n():
    while True:
        try:
            n = int(input("\nIngresa un valor entero para 'n' (o ingresa 0 para salir): "))
            if n < 0:
                print("Por favor, ingresa un valor entero no negativo.")
            else:
                return n
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un valor entero.")
             

def generar_fibonacci(n):
    secuencia = []
    a, b = 0, 1
    while len(secuencia) < n:
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

def mostrar_secuencia(secuencia):
    print("Secuencia de Fibonacci hasta el término {}:".format(len(secuencia)))
    print(secuencia)

def main():
    mostrar_bienvenida()
    while True:
        n = obtener_valor_n()
        if n == 0:
            print("Gracias por usar el generador de la Secuencia de Fibonacci. ¡Adiós!")
            break
        secuencia = generar_fibonacci(n)
        mostrar_secuencia(secuencia)

if __name__ == "__main__":
    main()
