"""
Implementación de un Suffix Trie para indexación eficiente de todos los sufijos de un texto.
"""

class NodoTrie:
    def __init__(self):
        self.hijos = dict()
        self.indices = []  # Guarda las posiciones donde inicia el sufijo

class SuffixTrie:
    def __init__(self, texto):
        """
        Construye el Suffix Trie para el texto dado.
        Args:
            texto (str): Texto sobre el que se construye el trie de sufijos.
        """
        self.raiz = NodoTrie()
        self.texto = texto
        self._construir_trie()

    def _construir_trie(self):
        n = len(self.texto)
        for i in range(n):
            nodo = self.raiz
            for c in self.texto[i:]:
                if c not in nodo.hijos:
                    nodo.hijos[c] = NodoTrie()
                nodo = nodo.hijos[c]
                nodo.indices.append(i)

    def buscar(self, patron):
        """
        Busca el patrón en el Suffix Trie y retorna las posiciones donde aparece.
        Args:
            patron (str): Patrón a buscar.
        Returns:
            list: Lista de posiciones donde inicia el patrón en el texto.
        """
        nodo = self.raiz
        for c in patron:
            if c not in nodo.hijos:
                return []
            nodo = nodo.hijos[c]
        return nodo.indices

if __name__ == "__main__":
    texto = "bananas"
    trie = SuffixTrie(texto)
    patron = "ana"
    posiciones = trie.buscar(patron)
    print(f"El patrón '{patron}' se encuentra en las posiciones: {posiciones}") 