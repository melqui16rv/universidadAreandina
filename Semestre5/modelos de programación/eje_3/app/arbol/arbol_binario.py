from .nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        self.cantidad += 1
        
        if not self.raiz:
            self.raiz = nuevo_nodo
            return
            
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.derecha

    def obtener_elementos(self):
        elementos = []
        def inorden(nodo):
            if nodo:
                inorden(nodo.izquierda)
                elementos.append(nodo.valor)
                inorden(nodo.derecha)
        inorden(self.raiz)
        return elementos

    def cantidad_elementos(self):
        return self.cantidad

    def visualizar_arbol(self):
        if not self.raiz:
            return "Árbol vacío"

        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.izquierda), get_height(node.derecha)) + 1

        def get_width(height):
            return pow(2, height - 1)

        def print_level(node, level, position, width, offset):
            if not node:
                return
            if level == 1:
                # Centramos el número en un espacio de 3 caracteres
                value = str(node.valor).center(3)
                # Calculamos el espacio antes del valor
                spaces = " " * (position * width - offset)
                print(spaces + value, end='')
            else:
                print_level(node.izquierda, level - 1, position * 2 - 1, width // 2, offset)
                print_level(node.derecha, level - 1, position * 2, width // 2, offset)

        def print_connections(node, level, position, width, offset):
            if not node:
                return
            if level == 1:
                if node.izquierda or node.derecha:
                    spaces = " " * (position * width - offset - 1)
                    connection = "/ \\" if node.izquierda and node.derecha else \
                               "/  " if node.izquierda else \
                               "  \\" if node.derecha else "   "
                    print(spaces + connection, end='')
            else:
                print_connections(node.izquierda, level - 1, position * 2 - 1, width // 2, offset)
                print_connections(node.derecha, level - 1, position * 2, width // 2, offset)

        height = get_height(self.raiz)
        width = get_width(height)
        offset = 0

        for level in range(1, height + 1):
            print_level(self.raiz, level, 1, width, offset)
            print()  # Nueva línea después de cada nivel
            if level < height:  # No imprimir conexiones para el último nivel
                print_connections(self.raiz, level, 1, width, offset)
                print()  # Nueva línea después de las conexiones

        return ""
