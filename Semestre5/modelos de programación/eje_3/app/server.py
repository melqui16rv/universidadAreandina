import socket
from functions import format_message, decode_message
import random

HOST = 'localhost'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

def main():
    consecutive_fails = 0
    aciertos = 0
    desaciertos = 0
    
    print("Servidor esperando conexiones...")
    conn, addr = server.accept()
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
                
            message = decode_message(data)
            if message.lower() == 'terminar':
                break
                
            numero_servidor = random.randint(1, 10)
            numero_cliente = int(message)
            
            if numero_servidor == numero_cliente:
                response = f"¡Acierto! Número: {numero_servidor}"
                consecutive_fails = 0
                aciertos += 1
            else:
                response = f"Fallé. Mi número: {numero_servidor}, Tu número: {numero_cliente}"
                consecutive_fails += 1
                desaciertos += 1
            
            if consecutive_fails >= 3:
                response = "Perdiste"
                conn.send(format_message(response))
                break
                
            conn.send(format_message(response))
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print(f"\nResultados finales:\nAciertos: {aciertos}\nDesaciertos: {desaciertos}")
    conn.close()
    server.close()

if __name__ == "__main__":
    main()
