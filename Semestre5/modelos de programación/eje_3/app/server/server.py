import socket
import threading
import random
from functions import formatear_mensaje, decodificar_mensaje, ordenamiento_burbuja

SERVIDOR = '127.0.0.1'
PUERTO = 65432

clientes_conectados = {}
candado = threading.Lock()
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
                    s.connect((SERVIDOR, PUERTO))
            except:
                pass
            break

def manejar_cliente(conexion, direccion, id_cliente):
    try:
        print(f"Nuevo cliente {id_cliente} conectado desde {direccion}")
        aciertos_totales = 0
        desaciertos_totales = 0
        
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break
            
            mensaje = decodificar_mensaje(datos)
            if mensaje.lower() == 'terminar':
                resumen = f"Resumen final - Aciertos: {aciertos_totales}, Desaciertos: {desaciertos_totales}"
                conexion.send(formatear_mensaje(resumen))
                break
            
            try:
                numero_objetivo = int(mensaje)
                print(f"\nCliente {id_cliente} envió el número: {numero_objetivo}")
                
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
                    
                    conexion.send(formatear_mensaje(response))
                    
                    # Si no es el último intento y no acertó, esperar confirmación
                    if intentos_ronda < 3 and numero_servidor != numero_objetivo:
                        conf = conexion.recv(1024)
                        if not conf:
                            return
                
                # Enviar resumen de la ronda
                resumen_ronda = f"\nRonda finalizada - Total intentos: {intentos_ronda}"
                resumen_ronda += f"\nNúmeros intentados: {numeros_intentados}"
                resumen_ronda += f"\nResultado: {aciertos_ronda} aciertos, {desaciertos_ronda} desaciertos en esta ronda"
                resumen_ronda += f"\nScore total - Aciertos: {aciertos_totales}, Desaciertos: {desaciertos_totales}"
                
                if desaciertos_ronda == 3:
                    resumen_ronda += f"\nPerdiste - El número que debía adivinar era: {numero_objetivo}"
                
                conexion.send(formatear_mensaje(resumen_ronda))
                
                # Terminar si hubo 3 desaciertos
                if desaciertos_ronda == 3:
                    break
                
            except ValueError:
                conexion.send(formatear_mensaje("Error: Número no válido"))
            
    except Exception as e:
        print(f"Error con cliente {id_cliente}: {e}")
    finally:
        with candado:
            del clientes_conectados[id_cliente]
            print(f"\nCliente {id_cliente} desconectado")
            print(f"Clientes conectados: {list(clientes_conectados.keys())}")
        conexion.close()

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((SERVIDOR, PUERTO))
            servidor.listen()
            print(f"Servidor iniciado en {SERVIDOR}:{PUERTO}")
            
            # Iniciar hilo monitor de comandos
            monitor_thread = threading.Thread(target=monitor_comandos, daemon=True)
            monitor_thread.start()
            
            contador_clientes = 0
            
            while servidor_activo:
                try:
                    conexion, direccion = servidor.accept()
                    if not servidor_activo:
                        conexion.close()
                        break
                        
                    contador_clientes += 1
                    id_cliente = f"Cliente_{contador_clientes}"
                    
                    with candado:
                        clientes_conectados[id_cliente] = direccion
                        print(f"\nClientes conectados: {list(clientes_conectados.keys())}")
                    
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
        # Cerrar conexiones de clientes activos
        with candado:
            for id_cliente in list(clientes_conectados.keys()):
                del clientes_conectados[id_cliente]
        print("\nServidor cerrado correctamente")

if __name__ == "__main__":
    main()
