# -*- coding: utf-8 -*-
"""textblob.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/vitojph/kschool-nlp-18/blob/master/notebooks/textblob.ipynb
"""

# install the requirements
# pip install textblob

"""# `textblob`: otro módulo para tareas de PLN (`NLTK` + `pattern`)

[textblob](http://textblob.readthedocs.org/) es una librería de procesamiento del texto para Python que permite realizar tareas de Procesamiento del Lenguaje Natural como análisis morfológico, extracción de entidades, análisis de opinión, traducción automática, etc.

Está construida sobre otras dos librerías muy famosas de Python: [NLTK](http://www.nltk.org/) y [pattern](http://www.clips.ua.ac.be/pages/pattern-en). La principal ventaja de [textblob](http://textblob.readthedocs.org/) es que permite combinar el uso de las dos herramientas anteriores en un interfaz más simple.

Vamos a apoyarnos en [este tutorial](http://textblob.readthedocs.org/en/dev/quickstart.html) para aprender a utilizar algunas de sus funcionalidades más llamativas. 

Lo primero es importar el objeto `TextBlob` que nos permite acceder a todas las herramentas que incluye.
"""

from textblob import TextBlob

"""Vamos a crear nuestro primer ejemplo de *textblob* a través del objeto `TextBlob`. Piensa en estos *textblobs* como una especie de cadenas de texto de Python, analaizadas y enriquecidas con algunas características extra. """

texto = """In new lawsuits brought against the ride-sharing companies Uber and Lyft, the top prosecutors in Los Angeles 
and San Francisco counties make an important point about the lightly regulated sharing economy. The consumers who 
participate deserve a very clear picture of the risks they're taking"""
t = TextBlob(texto)

print(t.sentences)

print("Tenemos", len(t.sentences), "oraciones.\n")

for sentence in t.sentences:
    print(sentence)
    print("-" * 75)

"""## Procesando oraciones, palabras y entidades

Podemos segmentar en oraciones y en palabras nuestra texto de ejemplo simplemente accediendo a las propiedades `.sentences` y `.words`. Imprimimos por pantalla: 
"""

# imprimimos las oraciones
for sentence in t.sentences:
    print(sentence)
    print("-" * 75)

# y las palabras
print(t.words)
print(texto.split())

"""La propiedad `.noun_phrases` nos permite acceder a la lista de entidades (en realidad, son sintagmas nominales) incluídos en nuestro *textblob*. Así es como funciona."""

print("el texto de ejemplo contiene", len(t.noun_phrases), "entidades")
for element in t.noun_phrases:
    print("-", element)

# jugando con lemas, singulares y plurales
for word in t.words:
    if word.endswith("s"):
        print(word.lemmatize(), word, word.singularize())
    else:
        print(word.lemmatize(), word, word.pluralize())

# ¿cómo podemos hacer la lematización más inteligente?
for item in t.tags:
    if item[1] == "NN":
        print(item[0], "-->", item[0].pluralize())
    elif item[1] == "NNS":
        print(item[0], "-->," item[0].singularize())
    else:
        print(item[0], item[0].lemmatize())

"""## Análisis sintático

Aunque podemos utilizar otros analizadores, por defecto el método `.parse()` invoca al analizador morfosintáctico del módulo  `pattern.en` que ya conoces.
"""

# análisis sintáctico
print(t.parse())

"""## Traducción automática


A partir de cualquier texto procesado con `TextBlob`, podemos acceder a un traductor automático de bastante calidad con el método `.translate`. Fíjate en cómo lo usamos. Es obligatorio indicar la lengua de destinto. La lengua de origen, se puede predecir a partir del texto de entrada. 
"""

# de chino a inglés y español
oracion_zh = "中国探月工程 亦稱嫦娥工程，是中国启动的第一个探月工程，于2003年3月1日正式启动"
t_zh = TextBlob(oracion_zh)
print(t_zh.translate(from_lang="zh-CN", to="en"))
print(t_zh.translate(from_lang="zh-CN", to="es"))

oracion_ru = "В 1943 году была отправлена в США, где выступала в защиту британской «белой книги», после чего работала в Канаде и Индии."
t_ru = TextBlob(oracion_ru)
print(t_ru.translate(from_lang="ru", to="en"))
print(t_ru.translate(from_lang="ru", to="es"))

print("--------------")

t_es = TextBlob(
    "La deuda pública ha marcado nuevos récords en España en el tercer trimestre"
)
print(t_es.translate(to="el"))
print(t_es.translate(to="ru"))
print(t_es.translate(to="eu"))
print(t_es.translate(to="fi"))
print(t_es.translate(to="fr"))
print(t_es.translate(to="nl"))
print(t_es.translate(to="gl"))
print(t_es.translate(to="ca"))
print(t_es.translate(to="zh"))
print(t_es.translate(to="la"))
print(t_es.translate(to="cs"))

# con el slang no funciona tan bien
print("--------------")
t_ita = TextBlob("Sono andato a Milano e mi sono divertito un bordello.")
print(t_ita.translate(to="en"))
print(t_ita.translate(to="es"))

"""## WordNet

`textblob`, más concretamente, cualquier objeto de la clase `Word`, nos permite acceder a la información de WordNet. 
"""

# WordNet
from textblob import Word
from textblob.wordnet import VERB

# ¿cuántos synsets tiene "car"
word = Word("car")
print(word.synsets)

# dame los synsets de la palabra "hack" como verbo
print(Word("hack").get_synsets(pos=VERB))

# imprime la lista de definiciones de "car"
print(Word("car").definitions)

# recorre la jerarquía de hiperónimos
for s in word.synsets:
    print(s.hypernym_paths())

"""## Análisis de opinion"""

# análisis de opinión
opinion1 = TextBlob("This new restaurant is great. I had so much fun!! :-P")
print(opinion1.sentiment)

opinion2 = TextBlob("Google News to close in Spain.")
print(opinion2.sentiment)

# subjetividad 0:1
# polaridad -1:1

print(opinion1.sentiment.polarity)

if opinion1.sentiment.subjectivity > 0.5:
    print("Hey, esto es una opinion")

"""### Ejercicio 1

Prueba a analizar distintas oraciones en inglés (combinando verbos que indican información subjetiva, palabras con distinta carga emocional, añadiendo emoticonos, etc.) para ver si eres capaz de entender el funcionamiento de este analizador de opiniones.
"""

# escribe tu código aquí

"""`TextBlob` da acceso a [otro tipo de analizadores](https://textblob.readthedocs.io/en/dev/advanced_usage.html#sentiment-analyzers) de opinión, por ejemplo, un clasificador basado en *Naive Bayes*. Prueba qué tal funciona:"""

from textblob.sentiments import NaiveBayesAnalyzer

for oracion in oraciones:
    t = TextBlob(oracion, analyzer=NaiveBayesAnalyzer())
    print(t.sentiment)

"""## Otras curiosidades"""

#  corrección ortográfica
b1 = TextBlob("I havv goood speling!")
print(b1.correct())

b2 = TextBlob("Miy naem iz Jonh!")
print(b2.correct())

b3 = TextBlob("Boyz dont cri")
print(b3.correct())

b4 = TextBlob("psicological posesion achifmen comitment")
print(b4.correct())

"""## Hasta el infinito, y más allá

En este breve resumen solo consideramos las posibilidades que ofrece `TextBlob` por defecto. Pero si necesitas personalizar las herramientas, echa un vistazo a [la documentación avanzada](http://textblob.readthedocs.org/en/dev/advanced_usage.html#advanced). 
"""