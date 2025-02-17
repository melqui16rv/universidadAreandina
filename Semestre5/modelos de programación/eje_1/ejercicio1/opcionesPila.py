class pila:
    def __init__(self):
        self._pila=[]

    def agregar(self):
        while True:
            elemento = int(input("Numero a agregar a la pila: "))
            self._pila.insert(0, elemento)
   
            continuar = input("¿Quieres agregar otro número? (s / N o otra letra): ")
            if continuar.lower() != 's':
                break

    def mostrarlista(self):
        return (f"Lista: {self._pila}")

    def promedioLista(self):
        return (f"Promedio: {round(sum(self._pila) / len(self._pila), 2)}")

    def ultimoDato(self):
        return (f"Ultimo elemento: {(self._pila[-1])}")

    def canditadpares(self):
        canPares = 0
        for n in self._pila:
            if n % 2 == 0:
                canPares += 1
        return (f"Total pares: {canPares}")
















# if __name__ == "__main__":
#     fun = pila()
#     resultado = fun.agregar()
#     sumaPares = fun.canditadpares()
#     promedioLista = fun.promedioLista()
#     ultimoDato = fun.ultimoDato()
#     print("Elementos en la lista:", resultado)
#     print("Cantidad pares: ", sumaPares)
#     print("Promedio de la lista: ", promedioLista)
#     print("Ultimo dato de la lista: ", ultimoDato)
