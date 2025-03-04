class ArbolBinario:
    def __init__(self):
        # Inicializa el árbol binario con la raíz como None
        self.raiz = None
        
    def insertar(self, valor):
        from nodo import Nodo
        # Crea un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)
        
        # Si la raíz es None, el nuevo nodo se convierte en la raíz
        if not self.raiz:
            self.raiz = nuevo_nodo
            return
            
        actual = self.raiz
        while True:
            # Si el valor es menor que el valor del nodo actual, va a la izquierda
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.izquierda
            else:
                # Si el valor es mayor o igual que el valor del nodo actual, va a la derecha
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.derecha

    def recorrido_inorden(self):
        resultado = []
        
        def inorden(nodo):
            # Realiza un recorrido inorden (izquierda, raíz, derecha)
            if nodo:
                inorden(nodo.izquierda)
                resultado.append(nodo.valor)
                inorden(nodo.derecha)
                
        inorden(self.raiz)
        return resultado
    
    def nodos_dos_hijos(self):
        resultado = []
        
        def verificar(nodo):
            # Verifica si un nodo tiene dos hijos
            if nodo:
                verificar(nodo.izquierda)
                if nodo.izquierda and nodo.derecha:
                    resultado.append(nodo.valor)
                verificar(nodo.derecha)
                
        verificar(self.raiz)
        return resultado
    
    def nodos_hijo_par(self):
        resultado = []
        
        def verificar(nodo):
            # Verifica si un nodo tiene al menos un hijo con valor par
            if nodo:
                if ((nodo.izquierda and nodo.izquierda.valor % 2 == 0) or 
                    (nodo.derecha and nodo.derecha.valor % 2 == 0)):
                    resultado.append(nodo.valor)
                verificar(nodo.izquierda)
                verificar(nodo.derecha)
                
        verificar(self.raiz)
        return resultado
    
    def suma_hijos(self):
        resultado = []
        
        def calcular(nodo):
            # Calcula la suma de los valores de los hijos de cada nodo
            if nodo:
                suma = 0
                suma += nodo.izquierda.valor if nodo.izquierda else 0
                suma += nodo.derecha.valor if nodo.derecha else 0
                resultado.append(suma)
                calcular(nodo.izquierda)
                calcular(nodo.derecha)
                
        calcular(self.raiz)
        return resultado
    
    def encontrar_camino(self, valor):
        def buscar(nodo):
            # Busca un nodo con el valor dado
            if not nodo:
                return None
            if nodo.valor == valor:
                return nodo
            if valor < nodo.valor:
                return buscar(nodo.izquierda)
            return buscar(nodo.derecha)
            
        nodo = buscar(self.raiz)
        if not nodo:
            return None
            
        camino = []
        # Encuentra el camino desde la raíz hasta el nodo con el valor dado
        while nodo:
            camino.insert(0, nodo.valor)
            nodo = nodo.padre
        return camino
