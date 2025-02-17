from .opcionesCola import *
from .opcionesPila import *

class APP_1:
    def __init__(self):
        self._cola = cola()
        self._pila = pila()

    def menupilas_1(self):
        while True:
            print("\nOpciones Pilas:")
            print("1. Agregar elemento a pila")
            print("2. Mostrar lista pila")
            print("3. Ver cantidad de números pares en pila")
            print("4. Ver promedio de la lista pila")
            print("5. Ver último dato de la lista pila")
            print("6. Mostrar todo")
            print("7. Regresar")
            opcion = input("Seleccione una opción: ")
            print("\n")
            
            if opcion == '1':
                self._pila.agregar()
            elif opcion == '2':
                print(self._pila.mostrarlista())
            elif opcion == '3':
                print(self._pila.canditadpares())
            elif opcion == '4':
                print(self._pila.promedioLista())
            elif opcion == '5':
                print(self._pila.ultimoDato())
            elif opcion == '6':
                print(self._pila.mostrarlista())
                print(self._pila.canditadpares())
                print(self._pila.promedioLista())
                print(self._pila.ultimoDato())
            elif opcion == '7':
                break

    def menucolas_1(self):
        while True:
            print("\nOpciones Colas:")
            print("1. Agregar elemento a cola")
            print("2. Mostrar lista cola")
            print("3. Ver cantidad de números pares en cola")
            print("4. Ver promedio de la lista cola")
            print("5. Ver último dato de la lista cola")
            print("6. Mostrar todo")
            print("7. Regresar")
            opcion = input("Seleccione una opción: ")
            print("\n")
            
            if opcion == '1':
                self._cola.agregar()
            elif opcion == '2':
                print(self._cola.mostrarlista())
            elif opcion == '3':
                print(self._cola.canditadpares())
            elif opcion == '4':
                print(self._cola.promedioLista())
            elif opcion == '5':
                print(self._cola.ultimoDato())
            elif opcion == '6':
                print(self._cola.mostrarlista())
                print(self._cola.canditadpares())
                print(self._cola.promedioLista())
                print(self._cola.ultimoDato())
            elif opcion == '7':
                break

    def menu_1(self):
        while True:
            print("\nMenú:")
            print("1. Menu Pilas")
            print("2. Menu Colas")
            print("3. Cerrar app")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.menupilas_1()
            elif opcion == '2':
                self.menucolas_1()
            elif opcion == '3':
                print("Cerrando la aplicación...")
                break

if __name__ == "__main__":
    app = APP_1()
    app.menu_1()