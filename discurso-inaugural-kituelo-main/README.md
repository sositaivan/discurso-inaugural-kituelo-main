# Discurso Inaugural

## Introducción
Una forma de analizar discursos es quedarse con las palabras claves mas usadas. No es una métrica súper formal, pero es una buena puerta de entrada.
Los/Las presidentes hacen discursos inaugurales cuando inician su mandato. ¿Son todos iguales, o reflejan personas y épocas?

## Consigna

### Archivos previos
Este tp cuenta con algunos archivos base
- 3 archivos txt, con los discursos inaugurales de alfonsín (1983), cfk (2007) y milei (2023). Está bien variado: radical, peronista y libertario. De esta forma, soy inimputable en cuanto a acusaciones de *"zurdo adoctrinador", "liberfacho", "radical", "ñoqui del estado"*, etc.
- 1 archivo `main.py`, con algunas funciones ya hechas, algunas para la parte I y otras para la parte II.
  - `obtener_palabras` que toma de parámetro el nombre del archivo a leer, y devuelve una lista con todas las palabras del archivo. (Parte I)
  - `top_n_palabras` que toma dos parámetros: un diccionario de `palabras:cantidad` y la cantidad de palabras a tomar, y devuelve una lista de tuplas `palabras:cantidad` con las primeras "n" (el número pasado como 2do parámetro) palabras mas usadas. (Parte I)
  - `limpiar_palabras` que toma una lista de palabras y las "limpia", osea, devuelve una lista con las mismas palabras pero sin signos de puntuación. (Parte II)
  - `sacar_conectores` que tomar una lista de palabras y devuelve otra lista de palabras pero sin las palabras conectoras (y, o, de, desde, etc). (Parte II)

### Requisitos
Para poder hacer este tp, vamos a usar una librería, `nltk`, para procesar lenguaje natural. En python, las librerías se installan con `pip`. En este caso,
```cmd
pip install --user nltk
```

### Parte I

Crear un programa que, dado el nombre de un archivo de texto, devuelva el top 20 de palabras más usadas. Para este punto pueden leer el archivo usando la función `obtener_palabras` y pueden, dado un diccionario `palabra:cantidad` (para cada palabra cuantas apariciones tiene), sacar el top 20 con la función `top_n_palabras`.

¿Que es un diccionario `palabra:cantidad`? Supongamos que tengo el texto
```
mi vieja mula ya no es lo que era, ya no es lo que era
```
un diccionario contando las palabras por cantidad sería:
```python
{
  "mi":1,
  "vieja":1,
  "mula":1,
  "ya":2,
  "no":2,
  "es":2,
  "lo":2,
  "que":2,
  "era":2
}
```

**IMPORTANTE:** Para que está actividad tenga algún sentido pedagógico y aprendan algo, por favor no usen ni chatGPT de forma directa (no le pidan la solución). Y si googlean, vean de no usar el método `get` de diccionarios. Es solo por ahora para practicar, después les muestro como se usa.

Pero Shulian, ¡Son todos artículos! "de", "a", "y", etc. Calma. Pasen al punto II.

### Parte II

Vamos a emprolijar un poco el dataset. 
1. Eliminar signos de puntuación y mayúsculas. Pueden usar la función `limpiar_palabras`.
2. Eliminar artículos y otras palabras conectoras. Acá es donde usamos `nltk`, y pueden usar la función `sacar_conectores`.

Prueben que ande. Mucho mejor, ¿No? 
   
### Extra (opcional)

Estaría bueno algún gráfico bonito con colores, ¿no?. Vean de mostrar el resultado como `Wordcloud`. ¿Cómo se hace eso? La respuesta empieza con **G** y termina con **oogle**.

### Parte III

Corran el programa con los 3 discursos. ¿Que les llama la atención? Tomen nota de los que les llamó la atención para discutir.