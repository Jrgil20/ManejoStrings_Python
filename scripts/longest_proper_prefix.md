# Longest Proper Prefix (LPP) que es también Sufijo

## ¿Qué es?
El Longest Proper Prefix (LPP) que es también sufijo es la mayor longitud de un prefijo propio de una cadena que coincide exactamente con un sufijo propio de la misma cadena. Un prefijo propio es aquel que no es igual a la cadena completa.

## ¿Cómo funciona?
1. Se recorren todos los posibles prefijos propios de la cadena.
2. Para cada prefijo, se compara con el sufijo de igual longitud al final de la cadena.
3. Se guarda la mayor longitud donde ambos coinciden.

## ¿Cuándo usarlo?
- Es fundamental en algoritmos de búsqueda de patrones como KMP, donde se utiliza para construir el arreglo LPS.
- Útil en problemas de análisis de cadenas, autómatas y teoría de lenguajes formales.
- Cuando se requiere identificar repeticiones o patrones internos en una cadena.

**El LPP ayuda a optimizar búsquedas y análisis de patrones en strings.** 