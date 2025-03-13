import socket
import threading
import time
from server.functions import generar_numeros_hilo, formatear_mensaje, decodificar_mensaje

SERVIDOR = '127.0.0.1'
PUERTO = 65432

def main():
    try:
        print(f"Intentando conectar al servidor {SERVIDOR}:{PUERTO}...")
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
                    if len(numeros) >= 5:
                        with candado:
                            nums_para_enviar = numeros.copy()
                            numeros.clear()
                        
                        numeros_str = ','.join(map(str, nums_para_enviar))
                        cliente.send(formatear_mensaje(numeros_str))
                        
                        respuesta = decodificar_mensaje(cliente.recv(1024))
                        print(f"Números enviados: {nums_para_enviar}")
                        print(f"Respuesta del servidor: {respuesta}")
                        
                        if respuesta == "Perdiste":
                            break
                        
                        comando = input("Presione Enter para continuar o escriba 'terminar' para salir: ")
                        if comando.lower() == 'terminar':
                            cliente.send(formatear_mensaje('terminar'))
                            break
                            
                except Exception as e:
                    print(f"Error: {e}")
                    break
    
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
