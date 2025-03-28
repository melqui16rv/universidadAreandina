from .manejador import manejar_cliente
from .arbol_binario import ArbolBinario
import socket
import threading

SERVIDOR = '127.0.0.1'
PUERTO = 65432
arbol_binario = ArbolBinario()
candado = threading.Lock()

def iniciar_servidor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((SERVIDOR, PUERTO))
            servidor.listen()
            print(f"Servidor escuchando en {SERVIDOR}:{PUERTO}...")

            while True:
                conexion, direccion = servidor.accept()
                print(f"Cliente conectado desde {direccion}")
                hilo = threading.Thread(target=manejar_cliente, 
                                     args=(conexion, direccion, arbol_binario, candado))
                hilo.start()

    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        print("Servidor finalizado.")


if __name__ == "__main__":
    iniciar_servidor()
