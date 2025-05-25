"""
Cálculo del Longest Proper Prefix (LPP) que es también sufijo para un string.
"""

def longest_proper_prefix_sufijo(s: str) -> int:
    """
    Calcula la longitud del prefijo propio más largo que es también sufijo para el string dado.

    Args:
        s (str): Cadena de entrada.

    Returns:
        int: Longitud del prefijo propio más largo que es también sufijo.
    """
    n = len(s)
    lpp = 0
    for i in range(1, n):
        # Compara el prefijo propio s[0:i] con el sufijo s[n-i:]
        if s[:i] == s[n-i:]:
            lpp = i
    return lpp

if __name__ == "__main__":
    # Ejemplo de uso
    cadena = "ABAB"
    resultado = longest_proper_prefix_sufijo(cadena)
    print(f"La longitud del prefijo propio más largo que es también sufijo en '{cadena}' es: {resultado}") 