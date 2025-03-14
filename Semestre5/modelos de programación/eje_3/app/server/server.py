import socket
import threading
import random
from functions import formatear_mensaje, decodificar_mensaje, ordenamiento_burbuja

SERVIDOR = '127.0.0.1'
PUERTO = 65432

clientes = {}
candado = threading.Lock()
servidor_activo = True

def monitor_comandos():
    global servidor_activo
    while True:
        comando = input("\nEscriba 'apagar' para detener el servidor: ")
        if comando.lower() == 'apagar':
            print("\nApagando servidor...")
            servidor_activo = False
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((SERVIDOR, PUERTO))
            except:
                pass
            break

def manejar_cliente(conexion, direccion, id_cliente):
    try:
        print(f"Nuevo cliente {id_cliente} conectado desde {direccion}")
        aciertos = 0
        desaciertos = 0
        
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break
            
            mensaje = decodificar_mensaje(datos)
            if mensaje.lower() == 'terminar':
                resumen = f"Resumen final - Aciertos: {aciertos}, Desaciertos: {desaciertos}"
                conexion.send(formatear_mensaje(resumen))
                break
            
            try:
                objetivo = int(mensaje)
                print(f"\nCliente {id_cliente} envió el número: {objetivo}")
                
                disponibles = list(map(int, decodificar_mensaje(conexion.recv(1024)).split(',')))
                print(f"Números disponibles: {disponibles}")
                
                intentos = 0
                aciertos_ronda = 0
                desaciertos_ronda = 0
                intentados = []
                
                adivinado = False
                for i in range(3):
                    if adivinado:
                        break
                        
                    intentos += 1
                    numero_servidor = random.choice(disponibles)
                    intentados.append(numero_servidor)
                    
                    if numero_servidor == objetivo:
                        response = f"¡El número es {objetivo}! Lo adiviné en el intento {intentos} de 3"
                        aciertos_ronda += 1
                        aciertos += 1
                        adivinado = True
                    else:
                        desaciertos_ronda += 1
                        desaciertos += 1
                        response = f"Fallé con {numero_servidor}. Intento {intentos} de 3"
                        if intentos < 3:
                            response += f". Me quedan {3-intentos} intentos"
                    
                    conexion.send(formatear_mensaje(response))
                    
                    if not adivinado and intentos < 3:
                        conf = conexion.recv(1024)
                        if not conf:
                            return

                resumen_ronda = f"\nRonda finalizada - Total intentos: {intentos}"
                resumen_ronda += f"\nNúmeros intentados: {intentados}"
                resumen_ronda += f"\nResultado: {aciertos_ronda} aciertos, {desaciertos_ronda} desaciertos en esta ronda"
                resumen_ronda += f"\nScore total - Aciertos: {aciertos}, Desaciertos: {desaciertos}"
                
                if desaciertos_ronda == 3:
                    resumen_ronda += f"\nPerdiste - El número que debía adivinar era: {objetivo}"
                
                conexion.send(formatear_mensaje(resumen_ronda))
                
                if desaciertos_ronda == 3:
                    break
                
            except ValueError:
                conexion.send(formatear_mensaje("Error: Número no válido"))
            
    except Exception as e:
        print(f"Error con cliente {id_cliente}: {e}")
    finally:
        with candado:
            del clientes[id_cliente]
            print(f"\nCliente {id_cliente} desconectado")
            print(f"Clientes conectados: {list(clientes.keys())}")
        conexion.close()

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((SERVIDOR, PUERTO))
            servidor.listen()
            print(f"Servidor iniciado en {SERVIDOR}:{PUERTO}")
            
            monitor_thread = threading.Thread(target=monitor_comandos, daemon=True)
            monitor_thread.start()
            
            contador = 0
            
            while servidor_activo:
                try:
                    conexion, direccion = servidor.accept()
                    if not servidor_activo:
                        conexion.close()
                        break
                        
                    contador += 1
                    id_cliente = f"Cliente_{contador}"
                    
                    with candado:
                        clientes[id_cliente] = direccion
                        print(f"\nClientes conectados: {list(clientes.keys())}")
                    
                    hilo_cliente = threading.Thread(
                        target=manejar_cliente,
                        args=(conexion, direccion, id_cliente)
                    )
                    hilo_cliente.start()
                except socket.error:
                    if not servidor_activo:
                        break
                    
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        with candado:
            for id_cliente in list(clientes.keys()):
                del clientes[id_cliente]
        print("\nServidor cerrado correctamente")

if __name__ == "__main__":
    main()
