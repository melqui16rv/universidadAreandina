class cola:
    def __init__(self):
        self._cola = []
        
    def agregar(self):
        while True:
            elemento = int(input("Numero a agregar a la cola: "))
            self._cola.append(elemento)
            
            continuar = input("¿Quieres agregar otro número? (s / N o otra letra): ")
            if continuar.lower() != 's':
                break    
    
    def mostrarlista(self):
        return (f"Lista: {self._cola}")
    
    def promedioLista(self):
        return (f"Promedio: {round(sum(self._cola) / len(self._cola), 2)}")
    
    def ultimoDato(self):
        return (f"Ultimo elemento: {self._cola[-1]}")
    
    def canditadpares(self):
        canPares = 0
        for n in self._cola:
            if n % 2 == 0:
                canPares += 1
        return (f"Total pares: {canPares}")














# if __name__ == "__main__": 
#     fun = cola()
#     resultado = fun.agregar()
#     sumaPares = fun.canditadpares()
#     promedioLista = fun.promedioLista()
#     ultimoDato = fun.ultimoDato()
#     print("Elementos en la lista:", resultado)
#     print("Cantidad pares: ", sumaPares)
#     print("Promedio de la lista: ", promedioLista)
#     print("Ultimo dato de la lista: ", ultimoDato)
