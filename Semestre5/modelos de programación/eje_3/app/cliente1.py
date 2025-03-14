import socket
import threading
import time
from server.functions import generar_numeros_hilo, formatear_mensaje, decodificar_mensaje, ordenamiento_burbuja
from arbol.arbol_binario import ArbolBinario

SERVIDOR = '127.0.0.1'
PUERTO = 65432
TIEMPO_ESPERA = 5

def jugar_ronda(cliente, numero_seleccionado):
    print(f"\nNúmero seleccionado: {numero_seleccionado}")
    
    for intento in range(3):
        try:
            respuesta = decodificar_mensaje(cliente.recv(1024))
            print(f"Respuesta del servidor: {respuesta}")
            
            if intento < 2:
                confirmacion = input("\nPresione Enter para el siguiente intento...")
                cliente.send(formatear_mensaje("siguiente"))
        except socket.error as e:
            print(f"Error de conexión: {e}")
            return True
    
    try:
        resumen = decodificar_mensaje(cliente.recv(1024))
        print(resumen)
    except socket.error as e:
        print(f"Error al recibir resumen: {e}")
        return True
    
    return "Perdiste" in resumen

def mostrar_menu_arbol(arbol):
    print("\n** MENÚ DEL ÁRBOL **")
    print("1. Agregar número al árbol")
    print("2. Visualizar árbol (orden ascendente)")
    print("3. Visualizar estructura del árbol")
    print("4. Jugar a adivinar número")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    arbol = ArbolBinario()
    try:
        print(f"Intentando conectar al servidor {SERVIDOR}:{PUERTO}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(TIEMPO_ESPERA)
            max_intentos = 5
            for intento in range(max_intentos):
                try:
                    cliente.connect((SERVIDOR, PUERTO))
                    direccion_local = cliente.getsockname()
                    print(f"¡Conectado al servidor desde el puerto local {direccion_local[1]}!")
                    break
                except ConnectionRefusedError:
                    if intento < max_intentos - 1:
                        print(f"Intento {intento + 1} fallido. Reintentando en 2 segundos...")
                        time.sleep(2)
                    else:
                        raise

            while True:
                opcion = mostrar_menu_arbol(arbol)
                
                if opcion == "1":
                    try:
                        numero = int(input("Ingrese un número para agregar al árbol: "))
                        arbol.insertar(numero)
                        print(f"Número {numero} agregado al árbol.")
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
                            seleccion = int(input("\nSeleccione uno de los números mostrados: "))
                            if seleccion in elementos_ordenados:
                                break
                            print("Error: Por favor seleccione uno de los números mostrados.")
                        except ValueError:
                            print("Error: Ingrese un número válido.")
                    
                    cliente.send(formatear_mensaje(str(seleccion)))
                    perdio_servidor = jugar_ronda(cliente, seleccion)

                elif opcion == "5":
                    cliente.send(formatear_mensaje('terminar'))
                    respuesta_final = decodificar_mensaje(cliente.recv(1024))
                    print(f"\n{respuesta_final}")
                    break

                else:
                    print("Opción no válida. Por favor intente de nuevo.")

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        print("\nCerrando cliente...")

if __name__ == "__main__":
    main()
