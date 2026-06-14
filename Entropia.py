import numpy as np
from Temperatura import temperatura
#====================================
#Entropía
#====================================
def entropia(probs):
    probs = np.array(probs)
    probs = probs[probs > 0]
    return -np.sum(
        probs * np.log2(probs)
    )

#====================================
#Comparación de temperaturas
#====================================
def analizarTemperaturas(distribucion):
    resultados = {}
    for T in [0.5, 1.0, 2.0]:
        palabras, probs = temperatura(
            distribucion,
            T
        )

        resultados[T] = entropia(probs)
    return resultados