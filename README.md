# 🎮 Juego de Adivinanza en Binario  

## 📌 Enunciado  
**Juego de Adivinanza en Binario:**  
El programa debe mostrar un número en **binario** y desafiar al usuario a adivinar su equivalente **decimal**, o viceversa.  
El objetivo es **reforzar la conversión entre ambos sistemas numéricos**, practicando tanto la lógica de la conversión como el razonamiento algorítmico.  

--

## 📖 Descripción del trabajo  
En este proyecto se desarrollaron **tres versiones diferentes** del mismo juego en Python, cada una con un enfoque distinto:  

1. **Versión Deepseek:**  
   - Implementa todas las conversiones de forma **manual** (sin funciones predefinidas como `bin()` o `int()`).
   - Uso explícito de estructuras **secuenciales, condicionales, repetitivas y listas**.
   - Muy detallada y extensa, pensada como práctica fuerte de algoritmos.  

2. **Versión Gemini:**  
   - Alterna automáticamente entre preguntas **Binario→Decimal** y **Decimal→Binario**.  
   - Incluye **validación de entradas** con `try/except`.  
   - Buen equilibrio entre complejidad y claridad.  

3. **Versión ChatGPT:**  
   - Código más **simple y directo**, usando funciones de Python como `bin()` e `int()`.  
   - Menor validación y menos rigor didáctico, pero más accesible y fácil de leer.  

---

## 📊 Comparación de las versiones  

| Aspecto              | Versión Deepseek | Versión Gemini | Versión ChatGPT |
|----------------------|------------------|----------------|-----------------|
| **Complejidad**      | Muy detallada, evita funciones predefinidas (`bin()`, `int()`). Convierte manualmente con bucles y multiplicaciones. | Intermedia: convierte decimal→binario manualmente, pero usa estructuras más claras. | Simple: usa directamente `bin()` y conversión con `int()`. |
| **Estructuras usadas** | Secuenciales, condicionales, repetitivas y listas, explícitamente en todo el código. | Usa las mismas estructuras, pero combina más validación de entrada y alterna tipo de pregunta. | Usa condicionales y bucles, pero se apoya en funciones de Python (menos manual). |
| **Modo de juego**    | El usuario elige: Binario→Decimal o Decimal→Binario. Se puede repetir indefinidamente hasta salir. | Define cantidad de rondas al inicio y alterna automáticamente entre los dos tipos de preguntas. | El modo es aleatorio: a veces muestra binario y pide decimal, o viceversa. |
| **Validación**       | Muy estricta: verifica carácter por carácter si la entrada es válida (numérica o binaria). | Valida entrada con `try/except`, evita errores de tipeo. | Validación mínima, depende de que el usuario escriba bien. |
| **Historial / resultados** | Guarda cada intento en una lista detallada (aciertos y errores). Muestra estadísticas finales con % de aciertos. | Guarda lista de aciertos (`True/False`). Muestra porcentaje final y un mensaje motivacional. | Guarda lista de puntajes (1 o 0). Al final suma y muestra aciertos. |
| **Dificultad para el usuario** | Más “serio” y extenso, pensado como práctica de conversión manual. | Equilibrado, mantiene dinámica por rondas y alternancia. | Más corto y amigable, pero menos riguroso en aprendizaje. |
| **Ventaja principal** | Refuerza fuerte los conceptos matemáticos detrás de la conversión binaria. | Balance entre didáctico y práctico, buen manejo de errores. | Código corto, fácil de entender y mantener. |
| **Desventaja principal** | Muy largo y repetitivo (difícil de mantener). | Más largo que lo necesario por validaciones y lógica extra. | Didácticamente pobre: el alumno no practica conversión manual. |

---

## 🎯 Conclusión  
La comparación de las tres versiones permite identificar fortalezas y debilidades:  
- **Deepseek**: refuerza la lógica algorítmica al máximo, pero es demasiado extenso.  
- **Gemini**: balancea práctica y simplicidad con validaciones útiles.  
- **ChatGPT**: ofrece un código sencillo y claro, pero menos educativo.  

La **versión final ideal** debería **combinar lo mejor de las tres**:  
- Claridad y simpleza en el código (ChatGPT).  
- Validaciones y manejo de rondas (Gemini).  
- Explicación del cálculo manual para reforzar conceptos (Deepseek).  

---

