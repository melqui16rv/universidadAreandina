from ejercicio1.appPilasColas import *
from ejercicio2.appPilasColas import *

class APP:
    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Menu Ejercicio 1")
            print("2. Menu Ejercicio 2")
            print("3. Cerrar app")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                app1 = APP_1()
                app1.menu_1()
            elif opcion == '2':
                app2 = APP_2()
                app2.menu_2()
            elif opcion == '3':
                print("Cerrando la aplicación...")
                break

if __name__ == "__main__":
    app = APP()
    app.menu()