Implementar un juego interactivo donde los jugadores deben encadenar palabras basándose en la última letra de la palabra anterior. Se utiliza una lista predefinida de palabras de la cual se selecciona aleatoriamente la primera palabra para comenzar el juego. Los jugadores alternan turnos, eligiendo palabras que cumplan con la regla de encadenamiento. Se manejan casos de palabras no válidas o duplicadas. Los jugadores tienen la opción de salir cuando lo deseen.

Instrucciones:

Al inicio, el programa dará la bienvenida y explicará las reglas del juego.
Se seleccionará aleatoriamente la primera palabra de la lista predefinida para iniciar el juego.
Los jugadores se turnarán para ingresar palabras que comiencen con la última letra de la palabra previa.
Se verificará si la palabra es válida (existente en la lista predefinida, no duplicada y cumple con la regla de encadenamiento).
Se mostrará el estado del juego después de cada turno, incluyendo la palabra actual y la última letra.
Los jugadores pueden salir del juego en cualquier momento al ingresar un comando especial, como "salir".
Se manejarán casos de entrada no válida, como palabras no existentes o comandos inválidos.

import string
import random

def mostrar_menu():
    print ("Bienvenido al juego de palabras ")
    print ("Reglas")
    print ("* Se encadenaran palabras una detras de la otra con su  ")
    print ("")
    print ("")
