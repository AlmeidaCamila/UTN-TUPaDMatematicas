# Version Gemini
import random
# ESTRUCTURA SECUENCIAL: Inicialización de variables
puntuacion = 0
ronda_actual = 0
tipo_pregunta = 0 # Usaremos 0 para Binario a Decimal, 1 para Decimal a Binario
min_numero = 4
max_numero = 31

print("🐍 ¡Bienvenido al Juego de Adivinanza en Binario! 🧠")
print("-----------------------------------------------------")

# ESTRUCTURA SECUENCIAL: Pedir el número de rondas
while True:
    try:
        entrada = input("¿Cuántas rondas quieres jugar? ")
        cantidad_rondas = int(entrada)
        # ESTRUCTURA CONDICIONAL: Verificar que sea un número positivo
        if cantidad_rondas > 0:
            break
        else:
            print("Por favor, ingresa un número de rondas positivo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

# LISTA: Para llevar un registro de los resultados
resultados_rondas = []

# ESTRUCTURA REPETITIVA (Bucle principal del juego)
while ronda_actual < cantidad_rondas:
    ronda_actual = ronda_actual + 1 # Estructura secuencial (incremento)
    print(f"\n--- RONDA {ronda_actual} de {cantidad_rondas} ---")
    
    # ESTRUCTURA SECUENCIAL/LOGICA: Determinar el tipo de pregunta (alternando)
    tipo_pregunta = ronda_actual % 2 # Álgebra de Boole/Lógica (resto 0 o 1)

    # Generar un número decimal aleatorio para la ronda
    numero_decimal = random.randint(min_numero, max_numero)
    
    # --- CONVERSIÓN DE DECIMAL A BINARIO (Manual para no usar bin() o funciones) ---
    temporal = numero_decimal
    binario_lista = [] # LISTA para almacenar los bits
    
    # ESTRUCTURA REPETITIVA: Algoritmo de división por 2
    while temporal > 0:
        # LOGICA/ALGEBRA DE BOOLE: Determinar el bit (resto de la división por 2)
        bit = temporal % 2
        # LISTA: Insertar el bit al inicio para que quede en el orden correcto
        binario_lista.insert(0, str(bit)) 
        temporal = temporal // 2 # División entera
        
    # ESTRUCTURA SECUENCIAL: Convertir la lista de bits en una cadena binaria
    numero_binario_str = ""
    for bit_str in binario_lista: # Recorrer la lista
        numero_binario_str = numero_binario_str + bit_str
    
    # Ajuste de longitud si es necesario (e.g., para mostrar 0001)
    # Aunque no es estrictamente necesario, asegura que sean al menos 4 bits
    if len(numero_binario_str) < 4:
        zeros_a_agregar = 4 - len(numero_binario_str)
        ceros = ""
        while zeros_a_agregar > 0:
            ceros = ceros + "0"
            zeros_a_agregar = zeros_a_agregar - 1
        numero_binario_str = ceros + numero_binario_str


    # ESTRUCTURA CONDICIONAL: Tipo de pregunta 1 (Binario a Decimal)
    if tipo_pregunta == 0:
        print(f"Pregunta: ¿Cuál es el equivalente **decimal** del binario **{numero_binario_str}**?")
        respuesta_correcta = numero_decimal
        
        # ESTRUCTURA REPETITIVA (Validación de entrada)
        while True:
            try:
                respuesta_usuario = int(input("Tu respuesta (decimal): "))
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero.")

    # ESTRUCTURA CONDICIONAL: Tipo de pregunta 2 (Decimal a Binario)
    else: # tipo_pregunta == 1
        print(f"Pregunta: ¿Cuál es el equivalente **binario** del decimal **{numero_decimal}**?")
        respuesta_correcta = numero_binario_str
        respuesta_usuario = input("Tu respuesta (binario, solo 0s y 1s): ")
        
        # LOGICA/ALGEBRA DE BOOLE: Asegurar que la respuesta binaria no tenga espacios al inicio/fin
        respuesta_usuario = respuesta_usuario.strip()

    # ESTRUCTURA CONDICIONAL: Verificar la respuesta
    es_correcto = False
    
    if tipo_pregunta == 0: # Binario a Decimal
        # LOGICA: Comparación de enteros
        if respuesta_usuario == respuesta_correcta:
            es_correcto = True
    else: # Decimal a Binario
        # LOGICA: Comparación de cadenas de texto
        if respuesta_usuario == respuesta_correcta:
            es_correcto = True

    # ESTRUCTURA CONDICIONAL: Mostrar resultado de la ronda
    if es_correcto:
        print("✅ ¡Correcto! Ganaste 1 punto.")
        puntuacion = puntuacion + 1 # Estructura secuencial (incremento)
        resultados_rondas.append(True) # LISTA: Agregar resultado
    else:
        print(f"❌ Incorrecto. La respuesta correcta es: **{respuesta_correcta}**.")
        resultados_rondas.append(False) # LISTA: Agregar resultado

    print(f"Puntuación actual: {puntuacion}")

# --- FIN DEL JUEGO ---
print("\n=====================================================")
print("             🎉 ¡JUEGO TERMINADO! 🎉")
print(f"Rondas jugadas: {cantidad_rondas}")
print(f"Puntuación final: {puntuacion} puntos.")

# ESTRUCTURA SECUENCIAL: Cálculo de porcentaje (aunque incluye operadores, usa secuenciales)
porcentaje_aciertos = (puntuacion / cantidad_rondas) * 100

# ESTRUCTURA CONDICIONAL: Mensaje final según el rendimiento
if porcentaje_aciertos >= 80:
    print("¡Excelente! ¡Dominas el sistema binario!")
elif porcentaje_aciertos >= 50:
    print("¡Bien hecho! Sigue practicando las conversiones.")
else:
    print("No te rindas, repasa la lógica del sistema binario.")
    
# LISTA: Mostrar el historial de resultados
print("\nHistorial de resultados (True = Acierto):")
print(resultados_rondas)
print("=====================================================")