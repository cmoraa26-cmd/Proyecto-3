from collections import defaultdict, Counter
def top1 (tokens, top_n=10):
    conteos = defaultdict(int)
    for i in range(len(tokens)-1):

        transicion = (
            tokens[i],
            tokens[i+1]
        )
        conteos[transicion] += 1
    return sorted(
        conteos.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

def top2 (tokens, top_n=10):
    conteos = defaultdict(int)
    for i in range(len(tokens)-2):
        transicion = (
            tokens[i],
            tokens[i+1],
            tokens[i+2]
        )
        conteos[transicion] += 1
    return sorted(
        conteos.items(),
        key=lambda x: x[1],
        reverse = True
    )[:top_n]

def palabraTop(tokens):
    conteo = Counter(tokens)
    palabra, frecuencia = conteo.most_common(1)[0]
    return palabra, frecuencia