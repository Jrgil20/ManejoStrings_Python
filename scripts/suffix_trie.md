# Suffix Trie para Indexación de Sufijos

## ¿Qué es?
Un Suffix Trie es una estructura de datos basada en un trie (árbol de prefijos) que almacena todos los sufijos de un texto. Permite buscar cualquier subcadena de manera eficiente.

## ¿Cómo funciona?
1. Se insertan todos los sufijos del texto en el trie, de modo que cada camino desde la raíz representa un sufijo.
2. Cada nodo puede almacenar las posiciones donde inicia el sufijo correspondiente.
3. Para buscar un patrón, se recorre el trie siguiendo los caracteres del patrón; si se llega a un nodo, sus índices indican las posiciones de ocurrencia.

## ¿Cuándo usarlo?
- Cuando se requiere buscar rápidamente cualquier subcadena dentro de un texto.
- En aplicaciones de bioinformática, compresión de datos, análisis de texto y procesamiento de cadenas.
- Cuando el texto es fijo y se realizarán muchas búsquedas de patrones diferentes.

**El Suffix Trie es útil para búsquedas rápidas, aunque puede consumir mucha memoria para textos largos.** 