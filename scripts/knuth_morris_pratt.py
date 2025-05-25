"""
Implementación del algoritmo Knuth-Morris-Pratt (KMP) para encontrar todas las ocurrencias de un patrón en un texto.
"""

def calcular_lps(patron: str) -> list:
    """
    Calcula el arreglo LPS (Longest Prefix Suffix) para el patrón.

    Args:
        patron (str): El patrón para el cual calcular el arreglo LPS.

    Returns:
        list: El arreglo LPS.
    """
    lps = [0] * len(patron)
    longitud = 0  # longitud del prefijo-sufijo más largo
    i = 1
    while i < len(patron):
        if patron[i] == patron[longitud]:
            longitud += 1
            lps[i] = longitud
            i += 1
        else:
            if longitud != 0:
                longitud = lps[longitud - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(texto: str, patron: str) -> list:
    """
    Busca todas las posiciones donde el patrón aparece en el texto usando el algoritmo KMP.

    Args:
        texto (str): El texto donde buscar.
        patron (str): El patrón a buscar.

    Returns:
        list: Lista de índices donde inicia el patrón en el texto.
    """
    posiciones = []
    n = len(texto)
    m = len(patron)
    lps = calcular_lps(patron)
    i = 0  # índice para texto
    j = 0  # índice para patrón
    while i < n:
        if patron[j] == texto[i]:
            i += 1
            j += 1
        if j == m:
            posiciones.append(i - j)
            j = lps[j - 1]
        elif i < n and patron[j] != texto[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return posiciones

if __name__ == "__main__":
    # Ejemplo de uso
    texto_ejemplo = "ABABDABACDABABCABAB"
    patron_ejemplo = "ABABCABAB"
    resultado = kmp(texto_ejemplo, patron_ejemplo)
    print(f"El patrón '{patron_ejemplo}' se encuentra en las posiciones: {resultado}") 