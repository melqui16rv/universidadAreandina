from .manejador import manejar_cliente
import socket
import threading

SERVIDOR = '127.0.0.1'
PUERTO = 65432
clientes = {}
contador_clientes = 0
candado = threading.Lock()                                         


def main():
    global contador_clientes
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((SERVIDOR, PUERTO))
            servidor.listen()

            print(f"Servidor escuchando en {SERVIDOR}:{PUERTO}...")

            while True:
                conexion, direccion = servidor.accept()
                with candado:
                    contador_clientes += 1
                    id_cliente = f"Cliente_{contador_clientes}"
                    clientes[id_cliente] = direccion

                hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion, id_cliente))
                hilo.start()

    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        print("Servidor finalizado.")


if __name__ == "__main__":
    main()
