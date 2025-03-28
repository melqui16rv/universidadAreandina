from graphviz import Digraph


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
        self.orden_insercion = []  # Nueva lista para guardar el orden de inserción

    def insertar(self, valor):
        self.orden_insercion.append(valor)  # Guardar el orden de inserción
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

    def obtener_elementos_insercion(self):
        return self.orden_insercion

    def cantidad_elementos(self):
        # Devolver la cantidad de elementos en el árbol
        return self.cantidad

    def visualizar_arbol(self):
        if not self.raiz:
            return "Árbol vacío"

        dot = Digraph()
        dot.attr('node', shape='circle')

        def agregar_nodos(dot, nodo):
            if nodo:
                dot.node(str(nodo.valor))
                if nodo.izquierda:
                    dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                    agregar_nodos(dot, nodo.izquierda)
                if nodo.derecha:
                    dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                    agregar_nodos(dot, nodo.derecha)

        agregar_nodos(dot, self.raiz)
        dot.render('arbol_binario', format='png', view=True)
        return "Visualización generada y guardada como 'arbol_binario.png'"

    def borrar_arbol(self):
        self.raiz = None
        self.cantidad = 0
        self.orden_insercion = []  # Limpiar también el orden de inserción
        return "Árbol binario borrado completamente"
