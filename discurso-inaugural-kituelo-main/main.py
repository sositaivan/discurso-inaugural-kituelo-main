import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Parte I
def obtener_palabras(filename:str)->list[str]:
    with open(filename, 'r', encoding="utf8") as file:
        data = file.read()
        palabras = data.split()
    return palabras

disc = input("alfonsin.txt, cfk.txt o milei.txt /n")

listap = obtener_palabras(disc)
dicci = {}


for palabra in listap:
    if palabra in dicci:
        dicci[palabra] +=1
    else:
        dicci[palabra] = 1



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

listap_limpia = limpiar_palabras(listap)
listap_filtrada = sacar_conectores(listap_limpia)

dicci_filtrada = {}
for palabra in listap_filtrada:
    if palabra in dicci_filtrada:
        dicci_filtrada[palabra] += 1
    else:
        dicci_filtrada[palabra] = 1


def top_n_palabras(conteo_palabras:dict[str, int], n:int)->list[tuple[str, int]]:
    return sorted(conteo_palabras.items(), key=lambda x: x[1], reverse=True)[:n]


top = top_n_palabras(dicci_filtrada, 20)
for palabra, cantidad in top:
    print(f"{palabra}: {cantidad}")
    
    
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dicci_filtrada)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # No mostrar los ejes
plt.show()


