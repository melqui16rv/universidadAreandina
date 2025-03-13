import socket
import threading
import time
from server.functions import generar_numeros_hilo, formatear_mensaje, decodificar_mensaje

SERVIDOR = '127.0.0.1'
PUERTO = 65432

def main():
    try:
        print(f"Cliente 2 - Intentando conectar al servidor {SERVIDOR}:{PUERTO}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            # Intentar conectar con reintento
            max_intentos = 5
            for intento in range(max_intentos):
                try:
                    cliente.connect((SERVIDOR, PUERTO))
                    print("¡Conectado al servidor!")
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
                target=generar_numeros_hilo,
                args=(numeros, candado),
                daemon=True
            )
            generador_numeros.start()
            
            while True:
                try:
                    if numeros:
                        with candado:
                            numero = str(numeros.pop(0))
                        cliente.send(formatear_mensaje(numero))
                        
                        respuesta = decodificar_mensaje(cliente.recv(1024))
                        print(f"Cliente 2 - Respuesta del servidor: {respuesta}")
                        
                        if respuesta == "Perdiste":
                            break
                        
                        comando = input("Cliente 2 - Presione Enter para continuar o escriba 'terminar' para salir: ")
                        if comando.lower() == 'terminar':
                            cliente.send(formatear_mensaje('terminar'))
                            break
                            
                except Exception as e:
                    print(f"Cliente 2 - Error: {e}")
                    break
    
    except ConnectionRefusedError:
        print("Cliente 2 - No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Cliente 2 - Error: {e}")

if __name__ == "__main__":
    main()
