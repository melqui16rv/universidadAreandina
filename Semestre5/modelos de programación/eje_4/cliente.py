import socket

SERVIDOR = '127.0.0.1'
PUERTO = 65432

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((SERVIDOR, PUERTO))
            print("Conectado al servidor")
            numeros_enviados = 0
            
            while numeros_enviados < 30:
                numero = input(f"Ingrese número {numeros_enviados + 1}/30 (debe ser de 2 cifras): ")
                cliente.send(numero.encode())
                
                # Recibir respuesta del servidor
                respuesta = cliente.recv(1024).decode()
                print(respuesta)
                
                if not "Error" in respuesta:
                    numeros_enviados += 1
                    
            print("Se han enviado 30 números. Conexión finalizada.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
