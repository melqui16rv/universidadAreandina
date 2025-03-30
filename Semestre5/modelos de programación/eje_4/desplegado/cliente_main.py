import socket

def iniciar_cliente_chat():
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado al chat por socket. Escribe 'exit' para salir.")
        while True:
            mensaje = input("Tú: ").strip()
            if mensaje.lower() == 'exit':
                s.send("EXIT".encode())
                break
            s.send(f"CHAT:{mensaje}".encode())
            respuesta = s.recv(1024).decode()
            print("Servidor:", respuesta)

if __name__ == "__main__":
    iniciar_cliente_chat()
