import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import os

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
        self.orden_insercion = []
        self.graphviz_disponible = False

    def insertar(self, valor):
        if valor in self.obtener_elementos():
            print(f"El valor {valor} ya existe en el árbol. Por favor, inserte otro número.")
            return

        self.orden_insercion.append(valor)  # Guardar el orden de inserción
        nuevo_nodo = Nodo(valor)
        self.cantidad += 1
        
        if not self.raiz:
            self.raiz = nuevo_nodo
            # Actualizar la visualización del árbol
            self.visualizar_arbol()
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

        # Actualizar la visualización del árbol
        self.visualizar_arbol()

    def obtener_elementos(self):
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

    def visualizar_arbol(self, ruta_guardado='./local/vistaArbol/arbol_binario'):
        if not self.raiz:
            return "Árbol vacío"

        try:
            os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)

            G = nx.DiGraph()
            pos = {}
            ancho_total = self._calcular_ancho_subarbol(self.raiz)
            self._agregar_nodos_networkx(self.raiz, 0, 0, pos, G, ancho_total)
            fig = plt.figure(figsize=(12, 8))
            nx.draw(G, pos,
                   with_labels=True,
                   node_color='lightblue',
                   node_size=2000,
                   font_size=16,
                   font_weight='bold',
                   arrows=True,
                   edge_color='gray',
                   arrowsize=20)
            plt.savefig(f"{ruta_guardado}.png", bbox_inches='tight')
            plt.close(fig)
            
            print(f"Árbol actualizado en: {ruta_guardado}.png")
            return "Visualización generada exitosamente"
            
        except Exception as e:
            print(f"Error al generar visualización: {e}")
            return self._visualizar_texto()
        finally:
            plt.close('all')

    def _agregar_nodos_networkx(self, nodo, x, y, pos, G, ancho_subarbol=1):
        if nodo:
            G.add_node(nodo.valor)
            pos[nodo.valor] = (x, -y)
            ancho_izquierdo = self._calcular_ancho_subarbol(nodo.izquierda)
            ancho_derecho = self._calcular_ancho_subarbol(nodo.derecha)
            if nodo.izquierda:
                nuevo_x = x - (ancho_izquierdo + 0.5)
                G.add_edge(nodo.valor, nodo.izquierda.valor)
                self._agregar_nodos_networkx(nodo.izquierda, nuevo_x, y + 1, pos, G, ancho_izquierdo)

            if nodo.derecha:
                nuevo_x = x + (ancho_derecho + 0.5)
                G.add_edge(nodo.valor, nodo.derecha.valor)
                self._agregar_nodos_networkx(nodo.derecha, nuevo_x, y + 1, pos, G, ancho_derecho)

    def _calcular_ancho_subarbol(self, nodo):

        if not nodo:
            return 0
        return 1 + self._calcular_ancho_subarbol(nodo.izquierda) + self._calcular_ancho_subarbol(nodo.derecha)

    def borrar_arbol(self):
        self.raiz = None
        self.cantidad = 0
        self.orden_insercion = [] 
        return "Árbol binario borrado completamente"
