import socket
import threading
from functions import format_message, decode_message, bubble_sort
import random

HOST = '127.0.0.1'
PORT = 65432

clientes_conectados = {}
lock = threading.Lock()

def handle_client(conn, addr, client_id):
    try:
        print(f"Nuevo cliente {client_id} conectado desde {addr}")
        consecutive_fails = 0
        aciertos = 0
        desaciertos = 0
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            message = decode_message(data)
            if message.lower() == 'terminar':
                break
            
            # Convertir string de números a lista
            numeros_cliente = [int(x) for x in message.split(',')]
            numeros_ordenados = bubble_sort(numeros_cliente.copy())
            
            # El servidor intenta adivinar el orden
            intento_servidor = bubble_sort([random.randint(1, 10) for _ in range(len(numeros_cliente))])
            
            if intento_servidor == numeros_ordenados:
                response = f"¡Acierto! Números ordenados: {numeros_ordenados}"
                consecutive_fails = 0
                aciertos += 1
            else:
                response = f"Fallé. Mi intento: {intento_servidor}, Números correctos: {numeros_ordenados}"
                consecutive_fails += 1
                desaciertos += 1
            
            if consecutive_fails >= 3:
                response = "Perdiste"
                conn.send(format_message(response))
                break
                
            conn.send(format_message(response))
            
        print(f"\nResultados finales de {client_id}:\nAciertos: {aciertos}\nDesaciertos: {desaciertos}")
        
    except Exception as e:
        print(f"Error con cliente {client_id}: {e}")
    finally:
        with lock:
            del clientes_conectados[client_id]
            print(f"\nCliente {client_id} desconectado")
            print(f"Clientes conectados: {list(clientes_conectados.keys())}")
        conn.close()

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen()
            print(f"Servidor iniciado en {HOST}:{PORT}")
            
            client_counter = 0
            
            while True:
                conn, addr = server.accept()
                client_counter += 1
                client_id = f"Cliente_{client_counter}"
                
                with lock:
                    clientes_conectados[client_id] = addr
                    print(f"\nClientes conectados: {list(clientes_conectados.keys())}")
                
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(conn, addr, client_id)
                )
                client_thread.start()
                
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        print("Servidor cerrado")

if __name__ == "__main__":
    main()
