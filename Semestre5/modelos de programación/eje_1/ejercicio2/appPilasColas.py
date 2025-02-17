from .opcionesCola import *
from .opcionesPila import *

class APP_2:
    def __init__(self):
        self._cola = cola()
        self._pila = pila()

    def menupilas_2(self):
        while True:
            print("\nOpciones Pilas:")
            print("1. Agregar elemento a pila")
            print("2. Mostrar lista pila")
            print("3. Ver cantidad de elementos de pila")
            print("4. Eliminar primer dato de la pila")
            print("5. Mostrar todo")
            print("6. Regresar")
            opcion = input("Seleccione una opción: ")
            print("\n")
            
            if opcion == '1':
                self._pila.agregar()
            elif opcion == '2':
                print(self._pila.mostrarlista())
            elif opcion == '3':
                print(self._pila.contarElementos())
            elif opcion == '4':
                print(self._pila.eliminarPrimero())
            elif opcion == '5':
                print(self._pila.mostrarlista())
                print(self._pila.contarElementos())
            elif opcion == '6':
                break

    def menucolas_2(self):
        while True:
            print("\nOpciones Colas:")
            print("1. Agregar elemento a cola")
            print("2. Mostrar lista cola")
            print("3. Ver cantidad de elementos de cola")
            print("4. Eliminar primer dato de la cola")
            print("5. Mostrar todo")
            print("6. Regresar")
            opcion = input("Seleccione una opción: ")
            print("\n")
            
            if opcion == '1':
                self._cola.agregar()
            elif opcion == '2':
                print(self._cola.mostrarlista())
            elif opcion == '3':
                print(self._cola.contarElementos())
            elif opcion == '4':
                print(self._cola.eliminarPrimero())
            elif opcion == '5':
                print(self._cola.mostrarlista())
                print(self._cola.contarElementos())
            elif opcion == '6':
                break

    def menu_2(self):
        while True:
            print("\nMenú:")
            print("1. Menu Pilas")
            print("2. Menu Colas")
            print("3. Cerrar app")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.menupilas_2()
            elif opcion == '2':
                self.menucolas_2()
            elif opcion == '3':
                print("Cerrando la aplicación...")
                break

if __name__ == "__main__":
    app = APP_2()
    app.menu_2()