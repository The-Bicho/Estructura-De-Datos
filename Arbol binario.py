class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            # Caso 1: Nodo con un solo hijo o sin hijos
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 2: Nodo con dos hijos
            nodo.valor = self._min_valor(nodo.derecha)
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)

        return nodo

    def _min_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Árbol original:")
# El resultado debería ser: 2, 3, 4, 5, 6, 7, 8
print(arbol.buscar(5).izquierda.valor, arbol.buscar(5).valor, arbol.buscar(5).derecha.valor)

# Eliminar el nodo con valor 5
arbol.eliminar(5)

print("Árbol después de eliminar el nodo con valor 5:")
# El resultado debería ser: 2, 3, 4, 6, 7, 8
print(arbol.buscar(6).izquierda.valor, arbol.buscar(6).valor, arbol.buscar(6).derecha.valor)
