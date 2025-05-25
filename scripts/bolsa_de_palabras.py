"""
Implementación del modelo de Bolsa de Palabras (Bag of Words) para representar documentos de texto.
"""
from collections import Counter
import re

def bolsa_de_palabras(documento):
    """
    Convierte un documento de texto en un diccionario de frecuencias de palabras (bolsa de palabras).
    Args:
        documento (str): Texto del documento.
    Returns:
        dict: Diccionario con palabras como claves y frecuencias como valores.
    """
    # Convertir a minúsculas y extraer palabras
    palabras = re.findall(r'\b\w+\b', documento.lower())
    return dict(Counter(palabras))

if __name__ == "__main__":
    doc = "El rápido zorro marrón salta sobre el perro perezoso. El zorro es rápido y marrón."
    resultado = bolsa_de_palabras(doc)
    print("Bolsa de palabras del documento:")
    for palabra, frecuencia in resultado.items():
        print(f"'{palabra}': {frecuencia}") 