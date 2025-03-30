from .manejador import manejar_cliente
from .arbol_binario import ArbolBinario
from .control import apagar, obtener_estado_apagado
import socket
import threading
import sys
import matplotlib.pyplot as plt

SERVIDOR = '127.0.0.1'
PUERTO = 65432
arbol_binario = ArbolBinario()
candado = threading.Lock()

def iniciar_servidor():
    servidor = None
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Intentar vincular el puerto
        try:
            servidor.bind((SERVIDOR, PUERTO))
        except OSError as e:
            print(f"Error al vincular puerto {PUERTO}. Asegúrese de que no esté en uso.")
            return

        servidor.listen(5)  # Permitir hasta 5 conexiones pendientes
        print(f"Servidor escuchando en {SERVIDOR}:{PUERTO}...")
        print("Presione Ctrl+C para detener el servidor")

        while not obtener_estado_apagado():
            try:
                servidor.settimeout(1)
                conexion, direccion = servidor.accept()
                print(f"Cliente conectado desde {direccion}")
                hilo = threading.Thread(target=manejar_cliente, 
                                     args=(conexion, direccion, arbol_binario, candado))
                hilo.daemon = True  # Hacer el hilo daemon
                hilo.start()
            except socket.timeout:
                continue
            except KeyboardInterrupt:
                print("\nDeteniendo el servidor...")
                apagar()
                break
            except Exception as e:
                print(f"Error en la conexión: {e}")

    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        if servidor:
            servidor.close()
        # Cerrar todas las figuras de matplotlib
        plt.close('all')
        print("Servidor apagado correctamente.")


if __name__ == "__main__":
    iniciar_servidor()
