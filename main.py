from Preprocesamiento import limpiartexto
from Modelos import Markov1, Markov2
from Prediccion import predecir, predecir2
from generacion import generarO1, generarO2
from analisis import top1, top2

# =====================================================
# CARGA DE TEXTOS
# =====================================================

with open("Texto1.txt", "r", encoding="utf-8") as f:
    texto1 = f.read()

with open("Texto2.txt", "r", encoding="utf-8") as f:
    texto2 = f.read()

# =====================================================
# PREPROCESAMIENTO
# =====================================================

Tokens1 = limpiartexto(texto1)
Tokens2 = limpiartexto(texto2)

print("=" * 60)
print("ESTADÍSTICAS DEL CORPUS")
print("=" * 60)

print(f"Texto 1: {len(Tokens1)} palabras")
print(f"Texto 2: {len(Tokens2)} palabras")

# =====================================================
# MODELOS
# =====================================================

Modelo11 = Markov1(Tokens1)
Modelo12 = Markov2(Tokens1)

Modelo21 = Markov1(Tokens2)
Modelo22 = Markov2(Tokens2)

# =====================================================
# PREDICCIONES TEXTO 1
# =====================================================

print("\n" + "=" * 60)
print("PREDICCIONES - TEXTO 1")
print("=" * 60)

# Orden 1
print("\nPredicción Orden 1")

prueba = Tokens1[0]

print(f"Contexto: '{prueba}'")

pred1 = predecir(
    Modelo11,
    prueba
)

for palabra, prob in sorted(
    pred1.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]:

    print(f"{palabra:<20} {prob:.4f}")

# Orden 2
print("\nPredicción Orden 2")

contexto1 = Tokens1[0]
contexto2 = Tokens1[1]

print(f"Contexto: ('{contexto1}', '{contexto2}')")

pred2 = predecir2(
    Modelo12,
    contexto1,
    contexto2
)

for palabra, prob in sorted(
    pred2.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]:

    print(f"{palabra:<20} {prob:.4f}")

# =====================================================
# PREDICCIONES TEXTO 2
# =====================================================

print("\n" + "=" * 60)
print("PREDICCIONES - TEXTO 2")
print("=" * 60)

# Orden 1
print("\nPredicción Orden 1")

prueba = Tokens2[0]

print(f"Contexto: '{prueba}'")

pred1 = predecir(
    Modelo21,
    prueba
)

for palabra, prob in sorted(
    pred1.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]:

    print(f"{palabra:<20} {prob:.4f}")

# Orden 2
print("\nPredicción Orden 2")

contexto1 = Tokens2[0]
contexto2 = Tokens2[1]

print(f"Contexto: ('{contexto1}', '{contexto2}')")

pred2 = predecir2(
    Modelo22,
    contexto1,
    contexto2
)

for palabra, prob in sorted(
    pred2.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]:

    print(f"{palabra:<20} {prob:.4f}")

# =====================================================
# GENERACIÓN TEXTO 1
# =====================================================

print("\n" + "=" * 60)
print("GENERACIÓN DE TEXTO - TEXTO 1 - ORDEN 1")
print("=" * 60)

for T in [0.5, 1.0, 2.0]:

    print(f"\nTemperatura = {T}")

    textoGenerado = generarO1(
        Modelo11,
        longitud=50,
        T=T
    )

    print(textoGenerado)

print("\n" + "=" * 60)
print("GENERACIÓN DE TEXTO - TEXTO 1 - ORDEN 2")
print("=" * 60)

for T in [0.5, 1.0, 2.0]:

    print(f"\nTemperatura = {T}")

    textoGenerado = generarO2(
        Modelo12,
        longitud=50,
        T=T
    )

    print(textoGenerado)

# =====================================================
# GENERACIÓN TEXTO 2
# =====================================================

print("\n" + "=" * 60)
print("GENERACIÓN DE TEXTO - TEXTO 2 - ORDEN 1")
print("=" * 60)

for T in [0.5, 1.0, 2.0]:

    print(f"\nTemperatura = {T}")

    textoGenerado = generarO1(
        Modelo21,
        longitud=50,
        T=T
    )

    print(textoGenerado)

print("\n" + "=" * 60)
print("GENERACIÓN DE TEXTO - TEXTO 2 - ORDEN 2")
print("=" * 60)

for T in [0.5, 1.0, 2.0]:

    print(f"\nTemperatura = {T}")

    textoGenerado = generarO2(
        Modelo22,
        longitud=50,
        T=T
    )

    print(textoGenerado)

# =====================================================
# ANÁLISIS TEXTO 1
# =====================================================

print("\n" + "=" * 60)
print("TOP 10 TRANSICIONES - TEXTO 1 - ORDEN 1")
print("=" * 60)

top_1 = top1(Tokens1)

for (a, b), frecuencia in top_1:

    print(f"{a} -> {b} : {frecuencia}")

print("\n" + "=" * 60)
print("TOP 10 TRANSICIONES - TEXTO 1 - ORDEN 2")
print("=" * 60)

top_2 = top2(Tokens1)

for (a, b, c), frecuencia in top_2:

    print(f"({a}, {b}) -> {c} : {frecuencia}")

# =====================================================
# ANÁLISIS TEXTO 2
# =====================================================

print("\n" + "=" * 60)
print("TOP 10 TRANSICIONES - TEXTO 2 - ORDEN 1")
print("=" * 60)

top_1_libro2 = top1(Tokens2)

for (a, b), frecuencia in top_1_libro2:

    print(f"{a} -> {b} : {frecuencia}")

print("\n" + "=" * 60)
print("TOP 10 TRANSICIONES - TEXTO 2 - ORDEN 2")
print("=" * 60)

top_2_libro2 = top2(Tokens2)

for (a, b, c), frecuencia in top_2_libro2:

    print(f"({a}, {b}) -> {c} : {frecuencia}")

# =====================================================
# COMPARACIÓN DIRECTA
# =====================================================

print("\n" + "=" * 60)
print("COMPARACIÓN ENTRE CORPUS")
print("=" * 60)

print("\nTexto 1 - Orden 2")
print(
    generarO2(
        Modelo12,
        longitud=50,
        T=1.0
    )
)

print("\nTexto 2 - Orden 2")
print(
    generarO2(
        Modelo22,
        longitud=50,
        T=1.0
    )
)

# =====================================================
# RESUMEN FINAL
# =====================================================

print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)

print(f"Palabras Texto 1: {len(Tokens1)}")
print(f"Palabras Texto 2: {len(Tokens2)}")

print(f"Estados Orden 1 Texto 1: {len(Modelo11)}")
print(f"Estados Orden 1 Texto 2: {len(Modelo21)}")

print(f"Estados Orden 2 Texto 1: {len(Modelo12)}")
print(f"Estados Orden 2 Texto 2: {len(Modelo22)}")