import socket
import threading
import time
from server.functions import generate_numbers_thread, format_message, decode_message, bubble_sort

SERVIDOR = '127.0.0.1'
PUERTO = 65432
TIMEOUT = 5

def jugar_ronda(cliente, numero_seleccionado):
    print(f"\nNúmero seleccionado: {numero_seleccionado}")
    
    # Siempre recibir 3 intentos
    for intento in range(3):
        try:
            respuesta = decode_message(cliente.recv(1024))
            print(f"Respuesta del servidor: {respuesta}")
            
            if intento < 2:  # Si no es el último intento
                confirmacion = input("\nPresione Enter para el siguiente intento...")
                cliente.send(format_message("siguiente"))
        except socket.error as e:
            print(f"Error de conexión: {e}")
            return True
    
    try:
        # Recibir resumen de la ronda
        resumen = decode_message(cliente.recv(1024))
        print(resumen)
    except socket.error as e:
        print(f"Error al recibir resumen: {e}")
        return True
    
    return "Perdiste" in resumen

def main():
    try:
        print(f"Intentando conectar al servidor {SERVIDOR}:{PUERTO}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(TIMEOUT)
            # Intentar conectar con reintento
            max_intentos = 5
            for intento in range(max_intentos):
                try:
                    cliente.connect((SERVIDOR, PUERTO))
                    # Obtener información del socket local
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
            
            # Iniciar hilo generador de números
            generador_numeros = threading.Thread(
                target=generate_numbers_thread,
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
                        
                        nums_ordenados = bubble_sort(nums_generados)
                        print("\nNúmeros generados y ordenados:", nums_ordenados)
                        
                        # Selección del número
                        while True:
                            try:
                                seleccion = int(input("\nSeleccione uno de los números mostrados: "))
                                if seleccion in nums_ordenados:
                                    break
                                print("Error: Por favor seleccione uno de los números mostrados.")
                            except ValueError:
                                print("Error: Ingrese un número válido.")
                        
                        # Enviar número y procesar intentos
                        cliente.send(format_message(str(seleccion)))
                        perdio_servidor = jugar_ronda(cliente, seleccion)
                        
                        # Preguntar si quiere jugar otra ronda
                        while True:
                            continuar = input("\n¿Desea jugar otra ronda? (s/n): ").lower()
                            if continuar in ['s', 'n']:
                                break
                            print("Por favor, responda 's' para sí o 'n' para no")
                        
                        if continuar == 'n':
                            cliente.send(format_message('terminar'))
                            respuesta_final = decode_message(cliente.recv(1024))
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
