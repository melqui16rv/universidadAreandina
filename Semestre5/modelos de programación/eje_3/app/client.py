import socket
import threading
from functions import generate_numbers_thread, format_message, decode_message

HOST = 'localhost'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def main():
    numbers = []
    lock = threading.Lock()
    
    # Iniciar hilo generador de números
    number_generator = threading.Thread(
        target=generate_numbers_thread,
        args=(numbers, lock),
        daemon=True
    )
    number_generator.start()
    
    while True:
        try:
            if numbers:
                with lock:
                    number = str(numbers.pop(0))
                client.send(format_message(number))
                
                response = decode_message(client.recv(1024))
                print(f"Respuesta del servidor: {response}")
                
                if response == "Perdiste":
                    break
                
                comando = input("Presione Enter para continuar o escriba 'terminar' para salir: ")
                if comando.lower() == 'terminar':
                    client.send(format_message('terminar'))
                    break
                    
        except Exception as e:
            print(f"Error: {e}")
            break
    
    client.close()

if __name__ == "__main__":
    main()
