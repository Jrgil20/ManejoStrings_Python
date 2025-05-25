# Algoritmo Aho-Corasick para Búsqueda de Múltiples Patrones

## ¿Qué es?
Aho-Corasick es un algoritmo eficiente para buscar simultáneamente múltiples patrones en un texto. Utiliza un trie (árbol de prefijos) y un arreglo de fallos para realizar la búsqueda en tiempo lineal respecto al tamaño del texto y los patrones.

## ¿Cómo funciona?
1. **Construcción del trie:** Se insertan todos los patrones en un trie, donde cada nodo representa un estado.
2. **Construcción del arreglo de fallos:** Para cada nodo, se determina a qué otro nodo regresar si ocurre un fallo (no hay coincidencia), similar al arreglo de fallos en KMP pero aplicado al trie.
3. **Búsqueda:** Se recorre el texto carácter por carácter, navegando por el trie y usando los enlaces de fallo cuando no hay coincidencia. Cuando se llega a un nodo con salida, se han encontrado uno o más patrones.

## ¿Cuándo usarlo?
- Cuando se necesita buscar muchos patrones a la vez en un texto grande.
- En aplicaciones como filtrado de contenido, detección de palabras clave, análisis de logs, motores de búsqueda, etc.
- Cuando la eficiencia es importante, ya que su complejidad es O(n + m + z), donde n es la longitud del texto, m la suma de longitudes de los patrones y z el número de ocurrencias encontradas.

**Aho-Corasick es ideal para búsquedas masivas de patrones y es ampliamente utilizado en procesamiento de texto y bioinformática.** 