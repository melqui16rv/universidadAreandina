class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = None  # Añadimos referencia al padre para facilitar el camino
