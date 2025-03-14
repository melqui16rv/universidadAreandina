class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def insertar(self, valor):
        # Crear un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)
        self.cantidad += 1
        
        if not self.raiz:
            # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
            self.raiz = nuevo_nodo
            return
            
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    # Insertar el nuevo nodo en la subárbol izquierdo
                    actual.izquierda = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    # Insertar el nuevo nodo en la subárbol derecho
                    actual.derecha = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.derecha

    def obtener_elementos(self):
        # Obtener los elementos del árbol en orden ascendente
        elementos = []
        def inorden(nodo):
            if nodo:
                inorden(nodo.izquierda)
                elementos.append(nodo.valor)
                inorden(nodo.derecha)
        inorden(self.raiz)
        return elementos

    def cantidad_elementos(self):
        # Devolver la cantidad de elementos en el árbol
        return self.cantidad

    def visualizar_arbol(self):
        if not self.raiz:
            return "Árbol vacío"

        def get_height(node):
            # Obtener la altura del árbol
            if not node:
                return 0
            return max(get_height(node.izquierda), get_height(node.derecha)) + 1

        def print_level(nodes, level, max_level):
            if not any(nodes):
                return False
            floor = max_level - level
            edge_lines = 2 ** max(floor - 1, 0)
            first_spaces = 2 ** floor - 1
            between_spaces = 2 ** (floor + 1) - 1
            result = ' ' * first_spaces
            new_nodes = []
            for node in nodes:
                if node:
                    result += str(node.valor)
                    new_nodes.append(node.izquierda)
                    new_nodes.append(node.derecha)
                else:
                    result += ' '
                    new_nodes.append(None)
                    new_nodes.append(None)
                result += ' ' * between_spaces
            print(result)
            for i in range(1, edge_lines + 1):
                result = ''
                for j in range(len(nodes)):
                    result += ' ' * (first_spaces - i)
                    if nodes[j] is None:
                        result += ' ' * (edge_lines + edge_lines + i + 1)
                        continue
                    if nodes[j].izquierda:
                        result += '/'
                    else:
                        result += ' '
                    result += ' ' * (i + i - 1)
                    if nodes[j].derecha:
                        result += '\\'
                    else:
                        result += ' '
                    result += ' ' * (edge_lines + edge_lines - i)
                print(result)
            return new_nodes

        height = get_height(self.raiz)
        nodes = [self.raiz]
        for level in range(height):
            nodes = print_level(nodes, level, height)
        return ""
