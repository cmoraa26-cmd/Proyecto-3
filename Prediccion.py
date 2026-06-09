def predecir(modelo, palabra):
    if palabra not in modelo:
        return {}
    return modelo[palabra]

def predecir2(modelo, palabra1, palabra2):
    contexto = (palabra1, palabra2)
    
    if contexto not in modelo:
        return {}
    return modelo[contexto]