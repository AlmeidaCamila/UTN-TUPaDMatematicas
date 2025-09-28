# Version Deepseek
# Juego de Adivinanza en Binario
# Usando solo: secuenciales, condicionales, repetitivas y listas

import random

# Inicio del programa - Estructuras secuenciales
print("Bienvenido al Juego de Adivinanza Binario!")
print("=" * 50)

# Variables iniciales
puntuacion = 0
intentos = 0
historial = []  # Lista para guardar resultados
continuar_jugando = True

# Estructura repetitiva principal (while)
while continuar_jugando:
    # Menú de selección
    print("\nSelecciona el modo de juego:")
    print("1. Binario → Decimal")
    print("2. Decimal → Binario")
    
    opcion = input("Ingresa 1 o 2: ")
    
    # Estructuras condicionales para el modo de juego
    if opcion == '1':
        modo = "binario_decimal"
        # Generar número binario aleatorio (4-8 bits)
        bits = random.randint(4, 8)
        binario = ''
        
        # Estructura repetitiva para generar binario
        i = 0
        while i < bits:
            binario = binario + random.choice(['0', '1'])
            i = i + 1
        
        # Eliminar ceros a la izquierda
        while len(binario) > 1 and binario[0] == '0':
            binario = binario[1:]
        
        # Convertir binario a decimal (sin función)
        decimal_correcto = 0
        potencia = len(binario) - 1
        j = 0
        
        # Estructura repetitiva para conversión binario-decimal
        while j < len(binario):
            bit = binario[j]
            if bit == '1':
                # Calcular 2^potencia
                resultado_potencia = 1
                k = 0
                while k < potencia:
                    resultado_potencia = resultado_potencia * 2
                    k = k + 1
                decimal_correcto = decimal_correcto + resultado_potencia
            potencia = potencia - 1
            j = j + 1
        
        print(f"\n¿Cuál es el equivalente decimal de: {binario} ?")
        
    elif opcion == '2':
        modo = "decimal_binario"
        # Generar número decimal aleatorio (1-255)
        decimal_correcto = random.randint(1, 255)
        
        # Convertir decimal a binario (sin función)
        binario_correcto = ''
        numero = decimal_correcto
        
        if numero == 0:
            binario_correcto = '0'
        else:
            # Estructura repetitiva para conversión decimal-binario
            while numero > 0:
                resto = numero % 2
                binario_correcto = str(resto) + binario_correcto
                numero = numero // 2
        
        print(f"\n¿Cuál es el equivalente binario de: {decimal_correcto} ?")
        
    else:
        print("Opción inválida. Usando modo Binario→Decimal por defecto.")
        modo = "binario_decimal"
        # Generar número binario aleatorio
        bits = random.randint(4, 8)
        binario = ''
        i = 0
        while i < bits:
            binario = binario + random.choice(['0', '1'])
            i = i + 1
        
        while len(binario) > 1 and binario[0] == '0':
            binario = binario[1:]
        
        # Convertir binario a decimal
        decimal_correcto = 0
        potencia = len(binario) - 1
        j = 0
        while j < len(binario):
            bit = binario[j]
            if bit == '1':
                resultado_potencia = 1
                k = 0
                while k < potencia:
                    resultado_potencia = resultado_potencia * 2
                    k = k + 1
                decimal_correcto = decimal_correcto + resultado_potencia
            potencia = potencia - 1
            j = j + 1
        
        print(f"\n¿Cuál es el equivalente decimal de: {binario} ?")
    
    # Capturar respuesta del usuario
    respuesta_usuario = input("Tu respuesta: ")
    intentos = intentos + 1
    es_correcta = False
    
    # Validar respuesta según el modo
    if modo == "binario_decimal":
        # Verificar si la respuesta es numérica
        es_numerica = True
        m = 0
        while m < len(respuesta_usuario):
            caracter = respuesta_usuario[m]
            if caracter not in "0123456789":
                es_numerica = False
                break
            m = m + 1
        
        if es_numerica and respuesta_usuario != "":
            # Convertir string a número
            respuesta_numero = 0
            n = 0
            while n < len(respuesta_usuario):
                digito = int(respuesta_usuario[n])
                respuesta_numero = respuesta_numero * 10 + digito
                n = n + 1
            
            if respuesta_numero == decimal_correcto:
                es_correcta = True
                
    else:  # modo decimal_binario
        # Verificar formato binario
        formato_valido = True
        p = 0
        while p < len(respuesta_usuario):
            caracter = respuesta_usuario[p]
            if caracter not in "01":
                formato_valido = False
                break
            p = p + 1
        
        if formato_valido and respuesta_usuario != "":
            # Convertir binario usuario a decimal
            decimal_usuario = 0
            potencia_usuario = len(respuesta_usuario) - 1
            q = 0
            while q < len(respuesta_usuario):
                bit = respuesta_usuario[q]
                if bit == '1':
                    resultado_potencia_usuario = 1
                    r = 0
                    while r < potencia_usuario:
                        resultado_potencia_usuario = resultado_potencia_usuario * 2
                        r = r + 1
                    decimal_usuario = decimal_usuario + resultado_potencia_usuario
                potencia_usuario = potencia_usuario - 1
                q = q + 1
            
            if decimal_usuario == decimal_correcto:
                es_correcta = True
    
    # Actualizar puntuación y mostrar resultado
    if es_correcta:
        puntuacion = puntuacion + 10
        print("✅ ¡Correcto! +10 puntos")
    else:
        print("❌ Incorrecto")
    
    # Mostrar respuesta correcta y guardar en historial
    if modo == "binario_decimal":
        print(f"La respuesta correcta era: {decimal_correcto}")
        # Agregar a la lista de historial
        if es_correcta:
            historial.append(f"Binario: {binario} → Decimal: {decimal_correcto} - ✓")
        else:
            historial.append(f"Binario: {binario} → Decimal: {decimal_correcto} - ✗")
    else:
        print(f"La respuesta correcta era: {binario_correcto}")
        if es_correcta:
            historial.append(f"Decimal: {decimal_correcto} → Binario: {binario_correcto} - ✓")
        else:
            historial.append(f"Decimal: {decimal_correcto} → Binario: {binario_correcto} - ✗")
    
    # Preguntar si quiere continuar
    print("\n¿Quieres jugar otra ronda?")
    continuar = input("Escribe 's' para sí, cualquier otra tecla para no: ")
    
    # Estructura condicional para determinar si continuar
    if continuar == 's' or continuar == 'S' or continuar == 'si' or continuar == 'SI':
        continuar_jugando = True
    else:
        continuar_jugando = False

# Mostrar estadísticas finales (fuera del while principal)
print("\n" + "=" * 50)
print("RESULTADOS FINALES")
print("=" * 50)
print(f"Puntuación total: {puntuacion} puntos")
print(f"Intentos realizados: {intentos}")

# Calcular porcentaje de aciertos
if intentos > 0:
    porcentaje = (puntuacion / (intentos * 10)) * 100
    print(f"Porcentaje de aciertos: {porcentaje:.1f}%")

# Mostrar historial usando lista
print("\nHISTORIAL DE JUEGO:")
if len(historial) > 0:
    s = 0
    while s < len(historial):
        print(f"{s + 1}. {historial[s]}")
        s = s + 1
else:
    print("No se jugaron rondas")

# Evaluación final
if puntuacion >= 30:
    print("\n🎉 ¡Excelente! Eres un experto en binario")
elif puntuacion >= 20:
    print("\n👍 ¡Buen trabajo! Sigues mejorando")
else:
    print("\n💪 Sigue practicando, ¡lo lograrás!")

print("\n¡Gracias por jugar!")