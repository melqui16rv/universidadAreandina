from arbol_binario import ArbolBinario

def mostrar_menu():
    print("\n** MENÚ DE OPERACIONES **")
    print("1. Mostrar recorrido en orden")
    print("2. Mostrar nodos con dos hijos")
    print("3. Mostrar nodos con hijo par")
    print("4. Mostrar suma de hijos")
    print("5. Buscar camino hacia un nodo")
    print("6. Mostrar todos los resultados")
    print("7. Salir")
    return input("Seleccione una opción: ")

def mostrar_todos_resultados(arbol):
    print("\nRecorrido en orden:")
    print(" ".join(map(str, arbol.recorrido_inorden())))
    
    print("\nLos que tienen 2 hijos:")
    print(" ".join(map(str, arbol.nodos_dos_hijos())))
    
    print("\nLos nodos que tienen 1 hijo par:")
    print(" ".join(map(str, arbol.nodos_hijo_par())))
    
    print("\nSuma de sus hijos:")
    print(" ".join(map(str, arbol.suma_hijos())))
    
    camino = arbol.encontrar_camino(4)  # Valor por defecto: 4
    print("\nBuscando el camino hacia el nodo 4:")
    if camino:
        print(f"El camino es: {' '.join(map(str, camino))}")
    else:
        print("El nodo no existe")

def main():
    arbol = ArbolBinario()
    
    # Datos estáticos sacados del modelo de el documento de la actividad
    valores = [18, 5, 3, 4, 1, 8, 20, 19, 21, 22]
    
    # Construcción del árbol
    for valor in valores:
        arbol.insertar(valor)
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            print("\nRecorrido en orden:")
            print(" ".join(map(str, arbol.recorrido_inorden())))
            
        elif opcion == "2":
            print("\nLos que tienen 2 hijos:")
            print(" ".join(map(str, arbol.nodos_dos_hijos())))
            
        elif opcion == "3":
            print("\nLos nodos que tienen 1 hijo par:")
            print(" ".join(map(str, arbol.nodos_hijo_par())))
            
        elif opcion == "4":
            print("\nSuma de sus hijos:")
            print(" ".join(map(str, arbol.suma_hijos())))
            
        elif opcion == "5":
            try:
                nodo_buscar = int(input("\nIngrese el nodo a buscar: "))
                camino = arbol.encontrar_camino(nodo_buscar)
                if camino:
                    print(f"El camino es: {' '.join(map(str, camino))}")
                else:
                    print("El nodo no existe")
            except ValueError:
                print("Por favor, ingrese un número válido")
                
        elif opcion == "6":
            mostrar_todos_resultados(arbol)
            
        elif opcion == "7":
            print("\n¡Gracias por usar el programa!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
