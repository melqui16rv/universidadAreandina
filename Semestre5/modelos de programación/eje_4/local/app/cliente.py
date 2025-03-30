import socket
import random

SERVIDOR = '127.0.0.1'
PUERTO = 65432

def generar_numeros_aleatorios():
    return [random.randint(10, 99) for _ in range(30)]

def enviar_numero(cliente_socket, numero):
    cliente_socket.send(str(numero).encode())
    respuesta = cliente_socket.recv(1024).decode()
    print(respuesta)
    return "Error" not in respuesta

def modo_automatico(cliente_socket):
    numeros = generar_numeros_aleatorios()
    for i, numero in enumerate(numeros, 1):
        print(f"Enviando número {i}/30: {numero}")
        if not enviar_numero(cliente_socket, numero):
            return False
    return True

def modo_manual(cliente_socket):
    numeros_enviados = 0
    while numeros_enviados < 30:
        numero = input(f"Ingrese número {numeros_enviados + 1}/30 (debe ser de 2 cifras, 'q' para salir): ")
        if numero.lower() == 'q':
            return False
        
        if enviar_numero(cliente_socket, numero):
            numeros_enviados += 1
    return True

def modo_chat(cliente_socket):
    print("Modo chat iniciado (escriba 'q' para salir)")
    cliente_socket.send("MODO_CHAT".encode())
    while True:
        try:
            mensaje = input("Tú: ").strip()
            if not mensaje:
                continue
                
            if mensaje.lower() == 'q':
                cliente_socket.send("CHAT_EXIT".encode())
                break
            
            mensaje = f"CHAT:{mensaje}"
            cliente_socket.send(mensaje.encode())
            respuesta = cliente_socket.recv(1024).decode()
            if respuesta:
                print(f"Servidor: {respuesta}")
            else:
                print("No se recibió respuesta del servidor")
                break
                
        except ConnectionError:
            print("Se perdió la conexión con el servidor")
            break
        except Exception as e:
            print(f"Error en el chat: {e}")
            break

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Modo automático (30 números aleatorios)")
    print("2. Modo manual (ingresar números uno a uno)")
    print("3. Chatear con el servidor")
    print("4. Borrar árbol binario")
    print("5. Apagar servidor")
    print("6. Salir")
    print("7. Ver datos del árbol (orden de inserción)")
    print("8. Ver datos del árbol ordenados")
    return input("Seleccione una opción: ")

def iniciar_cliente():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((SERVIDOR, PUERTO))
            print("Conectado al servidor")
            
            while True:
                opcion = mostrar_menu()
                
                if opcion == '1':
                    cliente.send("MODO_AUTO".encode())
                    if modo_automatico(cliente):
                        print("30 números enviados exitosamente")
                
                elif opcion == '2':
                    cliente.send("MODO_MANUAL".encode())
                    if modo_manual(cliente):
                        print("30 números enviados exitosamente")
                
                elif opcion == '3':
                    cliente.send("MODO_CHAT".encode())
                    modo_chat(cliente)
                
                elif opcion == '4':
                    cliente.send("BORRAR_ARBOL".encode())
                    respuesta = cliente.recv(1024).decode()
                    print(f"Respuesta del servidor: {respuesta}")
                
                elif opcion == '5':
                    cliente.send("APAGAR_SERVIDOR".encode())
                    respuesta = cliente.recv(1024).decode()
                    print(f"Respuesta del servidor: {respuesta}")
                    break
                
                elif opcion == '7':
                    cliente.send("VER_DATOS_INSERCION".encode())
                    respuesta = cliente.recv(1024).decode()
                    print(f"Respuesta del servidor: {respuesta}")
                
                elif opcion == '8':
                    cliente.send("VER_DATOS_ORDENADOS".encode())
                    respuesta = cliente.recv(1024).decode()
                    print(f"Respuesta del servidor: {respuesta}")
                
                elif opcion == '6':
                    cliente.send("EXIT".encode())
                    break
                
                else:
                    print("Opción no válida")
                    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Conexión finalizada")
