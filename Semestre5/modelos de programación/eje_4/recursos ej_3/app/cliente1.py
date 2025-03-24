import socket
import threading
import time
from server.functions import generar_numeros_hilo, formatear_mensaje, decodificar_mensaje, ordenamiento_burbuja
from arbol.arbol_binario import ArbolBinario

SERVIDOR = '127.0.0.1'
PUERTO = 65432
TIEMPO_ESPERA = 5

def jugar(cliente, numero, disponibles):
    print(f"\nNúmero seleccionado: {numero}")
    
    cliente.send(','.join(map(str, disponibles)).encode('utf-8'))  # Cambiado a .encode
    
    for intento in range(3):
        try:
            respuesta = cliente.recv(1024).decode('utf-8')  # Cambiado a .decode
            print(f"Respuesta del servidor: {respuesta}")
            
            if "¡El número es" in respuesta:
                return False
            
            if intento < 2:
                input("\nPresione Enter para el siguiente intento...")
                cliente.send("siguiente".encode('utf-8'))  # Cambiado a .encode
        except socket.error as e:
            print(f"Error de conexión: {e}")
            return True
    
    try:
        resumen = cliente.recv(1024).decode('utf-8')  # Cambiado a .decode
        print(resumen)
    except socket.error as e:
        print(f"Error al recibir resumen: {e}")
        return True
    
    return "Perdiste" in resumen

def menu_arbol(arbol):
    print("\n** MENÚ DEL ÁRBOL **")
    print("1. Agregar número")
    print("2. Ver árbol (orden ascendente)")
    print("3. Ver estructura del árbol")
    print("4. Jugar a adivinar número")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    arbol = ArbolBinario()
    try:
        print(f"Intentando conectar al servidor {SERVIDOR}:{PUERTO}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(TIEMPO_ESPERA)
            for intento in range(5):
                try:
                    cliente.connect((SERVIDOR, PUERTO))
                    print(f"¡Conectado al servidor desde el puerto local {cliente.getsockname()[1]}!")
                    break
                except ConnectionRefusedError:
                    if intento < 4:
                        print(f"Intento {intento + 1} fallido. Reintentando en 2 segundos...")
                        time.sleep(2)
                    else:
                        raise

            while True:
                opcion = menu_arbol(arbol)
                
                if opcion == "1":
                    try:
                        numero = int(input("Ingrese un número: "))
                        arbol.insertar(numero)
                        print(f"Número {numero} agregado.")
                    except ValueError:
                        print("Por favor ingrese un número válido.")

                elif opcion == "2":
                    elementos = arbol.obtener_elementos()
                    if elementos:
                        print("\nElementos del árbol (ordenados):")
                        print(ordenamiento_burbuja(elementos.copy()))
                    else:
                        print("El árbol está vacío.")

                elif opcion == "3":
                    print("\nEstructura del árbol:")
                    print(arbol.visualizar_arbol())

                elif opcion == "4":
                    if arbol.cantidad_elementos() < 5:
                        print("Debe tener al menos 5 elementos en el árbol para jugar.")
                        continue
                    
                    elementos = arbol.obtener_elementos()
                    elementos_ordenados = ordenamiento_burbuja(elementos.copy())
                    print("\nNúmeros disponibles:", elementos_ordenados)
                    
                    while True:
                        try:
                            seleccion = int(input("\nSeleccione un número: "))
                            if seleccion in elementos_ordenados:
                                break
                            print("Error: Seleccione un número válido.")
                        except ValueError:
                            print("Error: Ingrese un número válido.")
                    
                    cliente.send(str(seleccion).encode('utf-8'))  # Cambiado a .encode
                    perdio = jugar(cliente, seleccion, elementos_ordenados)

                elif opcion == "5":
                    cliente.send('terminar'.encode('utf-8'))  # Cambiado a .encode
                    print(f"\n{cliente.recv(1024).decode('utf-8')}")  # Cambiado a .decode
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        print("\nCerrando cliente...")

if __name__ == "__main__":
    main()
