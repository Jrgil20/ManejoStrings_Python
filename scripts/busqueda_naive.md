# Búsqueda Naive de Subcadenas en Python

## ¿Qué es?
La búsqueda Naive es un algoritmo sencillo para encontrar todas las ocurrencias de un patrón dentro de un texto. Compara el patrón con cada posible posición en el texto, una por una.

## ¿Cómo funciona?
1. Se toma el patrón y se compara con cada subcadena del texto de la misma longitud.
2. Si hay coincidencia, se registra la posición.
3. El proceso se repite hasta recorrer todo el texto.

## ¿Cuándo usarlo?
- Cuando el texto y el patrón son cortos.
- Para propósitos educativos o de demostración.
- Cuando la eficiencia no es crítica.

**No es recomendable para textos muy largos o patrones complejos, ya que su eficiencia es O((n-m+1)*m), donde n es la longitud del texto y m la del patrón.** 