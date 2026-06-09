import numpy as np
import random
from Temperatura import temperatura

def muestrear(distribucion, T=1.0):
    palabras, probs = temperatura(
        distribucion,
        T
    )
    return np.random.choice(
        palabras,
        p=probs
    )

def generarO1(
        modelo,
        longitud=50,
        T = 1.0):
    palabra = random.choice(
        list(modelo.keys())
    )
    resultado = [palabra]
    for _ in range(longitud -1):
        if palabra not in modelo:
            break
        palabra = muestrear(
            modelo[palabra],
            T
        )
        resultado.append(palabra)
    return " ".join(resultado)

def generarO2(
        modelo,
        longitud = 50,
        T=1.0):
    contexto = random.choice(
        list(modelo.keys())
    )

    resultado = [
        contexto[0],
        contexto[1]
    ]
    for _ in range(longitud-2):
        if contexto not in modelo:
            break
        siguiente = muestrear(
            modelo[contexto],
            T
        )
        resultado.append(siguiente)
        contexto = (
            contexto[1],
            siguiente
        )
    return " ".join(resultado)