import numpy as np

def temperatura(distribucion, T=1.0):
    palabras = list(distribucion.keys())
    probs = np.array(list(distribucion.values()))
    probs = probs ** (1/T)
    probs = probs / probs.sum()
    
    return palabras, probs
