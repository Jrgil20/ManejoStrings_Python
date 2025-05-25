"""
Implementación del algoritmo de búsqueda Naive para encontrar todas las ocurrencias de un patrón en un texto.
"""

def busqueda_naive(texto: str, patron: str) -> list:
    """
    Busca todas las posiciones donde el patrón aparece en el texto usando el algoritmo Naive.

    Args:
        texto (str): El texto donde buscar.
        patron (str): El patrón a buscar.

    Returns:
        list: Lista de índices donde inicia el patrón en el texto.
    """
    posiciones = []
    n = len(texto)
    m = len(patron)
    # Recorrer el texto hasta donde el patrón puede encajar
    for i in range(n - m + 1):
        # Comparar el segmento del texto con el patrón
        if texto[i:i + m] == patron:
            posiciones.append(i)
    return posiciones


if __name__ == "__main__":
    # Ejemplo de uso
    texto_ejemplo = "ABABDABACDABABCABAB"
    patron_ejemplo = "ABAB"
    resultado = busqueda_naive(texto_ejemplo, patron_ejemplo)
    print(f"El patrón '{patron_ejemplo}' se encuentra en las posiciones: {resultado}") 