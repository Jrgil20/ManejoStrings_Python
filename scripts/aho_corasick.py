"""
Implementación del algoritmo Aho-Corasick para búsqueda eficiente de múltiples patrones en un texto.
"""
from collections import deque, defaultdict

class NodoTrie:
    def __init__(self):
        self.hijos = dict()
        self.fallo = 0
        self.salida = []

class AhoCorasick:
    def __init__(self, patrones):
        """
        Inicializa el autómata de Aho-Corasick con los patrones dados.
        Args:
            patrones (list[str]): Lista de patrones a buscar.
        """
        self.trie = [NodoTrie()]
        self._construir_trie(patrones)
        self._construir_fallos()

    def _construir_trie(self, patrones):
        for palabra in patrones:
            estado = 0
            for caracter in palabra:
                if caracter not in self.trie[estado].hijos:
                    self.trie.append(NodoTrie())
                    self.trie[estado].hijos[caracter] = len(self.trie) - 1
                estado = self.trie[estado].hijos[caracter]
            self.trie[estado].salida.append(palabra)

    def _construir_fallos(self):
        cola = deque()
        for caracter, estado in self.trie[0].hijos.items():
            self.trie[estado].fallo = 0
            cola.append(estado)
        while cola:
            estado_actual = cola.popleft()
            for caracter, siguiente_estado in self.trie[estado_actual].hijos.items():
                cola.append(siguiente_estado)
                estado_fallo = self.trie[estado_actual].fallo
                while caracter not in self.trie[estado_fallo].hijos and estado_fallo != 0:
                    estado_fallo = self.trie[estado_fallo].fallo
                self.trie[siguiente_estado].fallo = self.trie[estado_fallo].hijos.get(caracter, 0)
                self.trie[siguiente_estado].salida += self.trie[self.trie[siguiente_estado].fallo].salida

    def buscar(self, texto):
        """
        Busca todas las ocurrencias de los patrones en el texto.
        Args:
            texto (str): Texto donde buscar los patrones.
        Returns:
            dict: Diccionario con los patrones encontrados y sus posiciones en el texto.
        """
        resultado = defaultdict(list)
        estado = 0
        for i, caracter in enumerate(texto):
            while caracter not in self.trie[estado].hijos and estado != 0:
                estado = self.trie[estado].fallo
            estado = self.trie[estado].hijos.get(caracter, 0)
            for patron in self.trie[estado].salida:
                resultado[patron].append(i - len(patron) + 1)
        return dict(resultado)

if __name__ == "__main__":
    patrones = ["he", "she", "his", "hers"]
    texto = "ahishers"
    ac = AhoCorasick(patrones)
    resultado = ac.buscar(texto)
    print("Resultados de la búsqueda:")
    for patron, posiciones in resultado.items():
        print(f"Patrón '{patron}' encontrado en las posiciones: {posiciones}") 