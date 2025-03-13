import socket
import threading
import random
from functions import format_message, decode_message, bubble_sort

HOST = '127.0.0.1'
PORT = 65432

clientes_conectados = {}
lock = threading.Lock()
servidor_activo = True

def monitor_comandos():
    global servidor_activo
    while True:
        comando = input("\nEscriba 'apagar' para detener el servidor: ")
        if comando.lower() == 'apagar':
            print("\nApagando servidor...")
            servidor_activo = False
            # Crear una conexión temporal para desbloquear accept()
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
            except:
                pass
            break

def handle_client(conn, addr, client_id):
    try:
        print(f"Nuevo cliente {client_id} conectado desde {addr}")
        aciertos_totales = 0
        desaciertos_totales = 0
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            message = decode_message(data)
            if message.lower() == 'terminar':
                resumen = f"Resumen final - Aciertos: {aciertos_totales}, Desaciertos: {desaciertos_totales}"
                conn.send(format_message(resumen))
                break
            
            try:
                numero_objetivo = int(message)
                print(f"\nCliente {client_id} envió el número: {numero_objetivo}")
                
                intentos_ronda = 0
                aciertos_ronda = 0
                desaciertos_ronda = 0
                numeros_intentados = []  # Lista para guardar los números intentados
                
                # Siempre hacer los 3 intentos
                for i in range(3):
                    intentos_ronda += 1
                    numero_servidor = random.randint(1, 10)
                    numeros_intentados.append(numero_servidor)
                    
                    if numero_servidor == numero_objetivo:
                        response = f"¡El número es {numero_objetivo}! Lo adiviné en el intento {intentos_ronda} de 3"
                        aciertos_ronda += 1
                        aciertos_totales += 1
                    else:
                        desaciertos_ronda += 1
                        desaciertos_totales += 1
                        response = f"Fallé con {numero_servidor}. Intento {intentos_ronda} de 3"
                        if intentos_ronda < 3:
                            response += f". Me quedan {3-intentos_ronda} intentos"
                        else:
                            response = f"Fallé con {numero_servidor}. Perdiste - No pude adivinar el número {numero_objetivo}. Intenté con los números: {numeros_intentados}"
                    
                    conn.send(format_message(response))
                    
                    # Si no es el último intento y no acertó, esperar confirmación
                    if intentos_ronda < 3 and numero_servidor != numero_objetivo:
                        conf = conn.recv(1024)
                        if not conf:
                            return
                
                # Enviar resumen de la ronda
                resumen_ronda = f"\nRonda finalizada - Total intentos: {intentos_ronda}"
                resumen_ronda += f"\nNúmeros intentados: {numeros_intentados}"
                resumen_ronda += f"\nResultado: {aciertos_ronda} aciertos, {desaciertos_ronda} desaciertos en esta ronda"
                resumen_ronda += f"\nScore total - Aciertos: {aciertos_totales}, Desaciertos: {desaciertos_totales}"
                
                if desaciertos_ronda == 3:
                    resumen_ronda += f"\nPerdiste - El número que debía adivinar era: {numero_objetivo}"
                
                conn.send(format_message(resumen_ronda))
                
                # Terminar si hubo 3 desaciertos
                if desaciertos_ronda == 3:
                    break
                
            except ValueError:
                conn.send(format_message("Error: Número no válido"))
            
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
            
            # Iniciar hilo monitor de comandos
            monitor_thread = threading.Thread(target=monitor_comandos, daemon=True)
            monitor_thread.start()
            
            client_counter = 0
            
            while servidor_activo:
                try:
                    conn, addr = server.accept()
                    if not servidor_activo:
                        conn.close()
                        break
                        
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
                except socket.error:
                    if not servidor_activo:
                        break
                    
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        # Cerrar conexiones de clientes activos
        with lock:
            for client_id in list(clientes_conectados.keys()):
                del clientes_conectados[client_id]
        print("\nServidor cerrado correctamente")

if __name__ == "__main__":
    main()
