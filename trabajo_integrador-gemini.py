

# 1. Importación permitida
import random

# 2. Solicitar y validar N
texto_n = input("Ingrese el número de bits (N ≥ 1): ")

es_n_valido = True
if len(texto_n) == 0:
    es_n_valido = False
else:
    for caracter in texto_n:
        if caracter not in "0123456789":
            es_n_valido = False
            break

# 3. Iniciar el juego solo si N es válido
if es_n_valido and int(texto_n) >= 1:
    N = int(texto_n)
    
    # --- Proceso Interno: Generación y Conversión (más compacto) ---
    
    # Calcular límite y generar número secreto en menos pasos
    limite = 1
    for i in range(N):
        limite = limite * 2
    secreto = int(random.random() * limite) # El rango es de 0 a limite-1

    # Conversión binaria manual optimizada
    # Este método también maneja el caso 'secreto = 0' eficientemente
    binario = ""
    if secreto == 0:
        binario = "0"
    else:
        n_temp = secreto
        while n_temp > 0:
            binario = str(n_temp % 2) + binario
            n_temp = n_temp // 2
    
    # --- Interacción con el usuario (Bucle de juego principal) ---
    
    print(f"\n--- Adivina el Número Binario ---")
    print(f"Binario: {binario}")
    print(f"Rango decimal: 0 a {limite - 1}")
    
    intentos = 0
    while True: # Bucle infinito que se rompe al acertar
        texto_intento = input("Tu adivinanza: ")
        
        # Validación numérica manual (obligatoria por las reglas)
        es_valido = True
        if len(texto_intento) == 0:
            es_valido = False
        else:
            for caracter in texto_intento:
                if caracter not in "0123456789":
                    es_valido = False
                    break
        
        if es_valido:
            intentos = intentos + 1
            intento = int(texto_intento)
            
            if intento < secreto:
                print("Incorrecto. Es MAYOR.")
            elif intento > secreto:
                print("Incorrecto. Es MENOR.")
            else:
                print(f"¡CORRECTO! El número era {secreto}. Lo lograste en {intentos} intentos.")
                break # Única salida del bucle
        else:
            print("Entrada no válida. Intenta de nuevo.")
            
else:
    print("Error: La entrada para N debe ser un número entero mayor o igual a 1.")