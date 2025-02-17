class cola:
    def __init__(self):
        self._cola = []
        
    def agregar(self):
        while True:
            print(f"\nInformación Persona")
            codigo = int(input("Codigo: "))
            nombre = str(input("Nombre: "))
            telefono = int(input("Telefono: "))
            edad = int(input("Edad: "))
            
            self._cola.append((codigo, nombre, telefono, edad))
            # self._cola.append([codigo, nombre, telefono, edad])

            continuar = input("¿Quieres agregar otra persona? (s / N o otra letra): ")
            if continuar.lower() != 's':
                print(f"Personas agregadas: {len(self._cola)}")
                break    
    
    def mostrarlista(self):
        return (f"Lista: {self._cola}")
    
    def eliminarPrimero(self):
        if self._cola:
            self._cola.pop(0)
            return self.mostrarlista()
        else:
            return "La lista está vacía"
    
    def contarElementos(self):
        return (f"Total elementos: {len(self._cola)}")
