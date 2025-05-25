# Algoritmo Knuth-Morris-Pratt (KMP) para Búsqueda de Subcadenas

## ¿Qué es?
El algoritmo Knuth-Morris-Pratt (KMP) es un método eficiente para buscar todas las ocurrencias de un patrón dentro de un texto. Utiliza información previa del patrón para evitar comparaciones innecesarias.

## ¿Cómo funciona?
1. Preprocesa el patrón para construir el arreglo LPS (Longest Prefix Suffix), que indica la mayor longitud de prefijo que es también sufijo.
2. Recorre el texto y el patrón simultáneamente, usando el arreglo LPS para saltar posiciones cuando hay un desajuste, evitando retrocesos innecesarios en el texto.
3. Registra las posiciones donde se encuentra el patrón.

## ¿Cuándo usarlo?
- Cuando se necesita buscar patrones en textos largos de manera eficiente.
- Cuando se requiere un algoritmo con complejidad lineal O(n + m), donde n es la longitud del texto y m la del patrón.
- En aplicaciones donde la eficiencia es importante, como editores de texto, motores de búsqueda, o análisis de ADN.

**KMP es más eficiente que la búsqueda Naive en la mayoría de los casos, especialmente con patrones y textos grandes.** 