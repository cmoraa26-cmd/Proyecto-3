import re
def limpiartexto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\sáéíóúüñ]',' ',texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto.split()