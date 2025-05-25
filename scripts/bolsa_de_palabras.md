# Bolsa de Palabras (Bag of Words) para Representación de Documentos

## ¿Qué es?
La Bolsa de Palabras es un modelo sencillo para representar documentos de texto. Cada documento se describe por las palabras que contiene y la frecuencia de cada una, sin considerar el orden ni la relación entre ellas.

## ¿Cómo funciona?
1. Se define un vocabulario con todas las palabras presentes en el conjunto de documentos.
2. Cada documento se convierte en un vector o diccionario donde cada posición corresponde a una palabra del vocabulario y su valor es la frecuencia de esa palabra en el documento.
3. El resultado es una representación numérica fácil de comparar entre documentos.

## ¿Cuándo usarlo?
- Para comparar documentos por similitud de contenido.
- En tareas de clasificación de texto, recuperación de información y minería de textos.
- Cuando el orden de las palabras no es relevante para el análisis.

**La Bolsa de Palabras es útil por su simplicidad, aunque no captura la estructura ni el contexto de las palabras.** 