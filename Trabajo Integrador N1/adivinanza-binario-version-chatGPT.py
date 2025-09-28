# Version ChatGPT

import random

# Lista para registrar los puntajes
puntajes = []

# Variable de control para repetir el juego
seguir = True

print("=== JUEGO DE ADIVINANZA BINARIO ===")

while seguir:
    # Generar un número aleatorio entre 1 y 31
    numero = random.randint(1, 31)

    # Decidir lógicamente si mostrar en binario o decimal
    mostrar_binario = random.choice([True, False])

    if mostrar_binario:
        # Mostrar el número en binario
        print("\nEl número en BINARIO es:", bin(numero)[2:])
        respuesta = int(input("¿Cuál es su equivalente DECIMAL?: "))
        
        if respuesta == numero:
            print("¡Correcto!")
            puntajes.append(1)   # Lista usada para acumular aciertos
        else:
            print("Incorrecto. Era", numero)
            puntajes.append(0)

    else:
        # Mostrar el número en decimal
        print("\nEl número en DECIMAL es:", numero)
        respuesta = input("¿Cuál es su equivalente BINARIO?: ")
        
        if respuesta == bin(numero)[2:]:
            print("¡Correcto!")
            puntajes.append(1)
        else:
            print("Incorrecto. Era", bin(numero)[2:])
            puntajes.append(0)

    # Uso de lógica booleana para continuar o salir
    opcion = input("¿Querés jugar otra ronda? (s/n): ")
    seguir = (opcion.lower() == "s") and not (opcion.lower() == "n")

# Mostrar resultados finales
print("\n=== RESULTADOS ===")
print("Respuestas:", puntajes)
print("Aciertos:", sum(puntajes), "de", len(puntajes))
