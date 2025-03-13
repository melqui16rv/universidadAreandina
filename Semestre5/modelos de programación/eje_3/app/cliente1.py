import socket
import threading
import time
from server.functions import generar_numeros_hilo, formatear_mensaje, decodificar_mensaje, ordenamiento_burbuja

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

def main():
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

            numeros = []
            candado = threading.Lock()
            
            generador_numeros = threading.Thread(
                target=generar_numeros_hilo,
                args=(numeros, candado),
                daemon=True
            )
            generador_numeros.start()
            
            while True:
                try:
                    if len(numeros) >= 5:
                        with candado:
                            nums_generados = numeros.copy()
                            numeros.clear()
                        
                        nums_ordenados = ordenamiento_burbuja(nums_generados)
                        print("\nNúmeros generados y ordenados:", nums_ordenados)
                        
                        while True:
                            try:
                                seleccion = int(input("\nSeleccione uno de los números mostrados: "))
                                if seleccion in nums_ordenados:
                                    break
                                print("Error: Por favor seleccione uno de los números mostrados.")
                            except ValueError:
                                print("Error: Ingrese un número válido.")
                        
                        cliente.send(formatear_mensaje(str(seleccion)))
                        perdio_servidor = jugar_ronda(cliente, seleccion)
                        
                        while True:
                            continuar = input("\n¿Desea jugar otra ronda? (s/n): ").lower()
                            if continuar in ['s', 'n']:
                                break
                            print("Por favor, responda 's' para sí o 'n' para no")
                        
                        if continuar == 'n':
                            cliente.send(formatear_mensaje('terminar'))
                            respuesta_final = decodificar_mensaje(cliente.recv(1024))
                            print(f"\n{respuesta_final}")
                            break
                    
                    time.sleep(0.5)
                            
                except Exception as e:
                    print(f"Error: {e}")
                    break
    
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        print("\nCerrando cliente...")

if __name__ == "__main__":
    main()
