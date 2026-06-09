from collections import defaultdict

def Markov1(tokens):
    frecuencias = defaultdict(lambda: defaultdict(int))
    for i in range (len(tokens)-1):
        actual = tokens[i]
        siguiente = tokens[i+1]
        frecuencias[actual][siguiente] += 1
    probabilidades = {}
    for palabra, transiciones in frecuencias.items():
        total = sum(transiciones.values())
        probabilidades[palabra] = {
            sig: freq/total
            for sig, freq in transiciones.items()
        }
    return probabilidades

def Markov2(tokens):
    frecuencias = defaultdict(lambda: defaultdict(int))
    for i in range(len(tokens)-2):
        contexto = (tokens[i], tokens [i+1])
        siguiente = tokens[i+2]
        frecuencias[contexto][siguiente] += 1
    probabilidades = {}
    
    for contexto, transiciones in frecuencias.items():
        total = sum(transiciones.values())
        probabilidades[contexto] = {
            sig: freq/total
            for sig, freq in transiciones.items()
        }
    return probabilidades