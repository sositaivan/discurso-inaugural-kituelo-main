import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#Parte I
def obtener_palabras(filename:str)->list[str]:
    with open(filename, 'r', encoding="utf8") as file:
        data = file.read()
        palabras = data.split()
    return palabras

def top_n_palabras(conteo_palabras:dict[str, int], n:int)->list[tuple[str, int]]:
    return sorted(conteo_palabras.items(), key=lambda x: x[1], reverse=True)[:n]

#Parte II
def limpiar_palabras(palabras:list[str])->list[str]:
    palabras_limpias = []
    for palabra in palabras:
        palabra = palabra.lower()
        palabra = palabra.replace('.', '')
        palabra = palabra.replace(',', '')
        palabra = palabra.replace(';', '')
        palabra = palabra.replace(':', '')
        palabra = palabra.replace('?', '')
        palabra = palabra.replace('¿', '')
        palabra = palabra.replace('!', '')
        palabra = palabra.replace('¡', '')
        palabras_limpias.append(palabra)
    return palabras_limpias

def sacar_conectores(palabras:list[str])->list[str]:
    stopword_es = stopwords.words('spanish')
    palabras_limpias = []
    for palabra in palabras:
        if palabra not in stopword_es:
            palabras_limpias.append(palabra)
    return palabras_limpias

