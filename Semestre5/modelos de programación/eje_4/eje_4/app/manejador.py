from .arbol_binario import ArbolBinario

def manejar_cliente(conexion, direccion, arbol, candado):
    try:
        numeros_recibidos = 0
        with conexion:
            while numeros_recibidos < 30:
                # Recibir datos del cliente
                datos = conexion.recv(1024).decode().strip()
                if not datos:
                    break
                
                try:
                    numero = int(datos)
                    if 10 <= numero <= 99:  # Validar número de 2 cifras
                        with candado:
                            arbol.insertar(numero)
                            numeros_recibidos += 1
                            
                        # Enviar respuesta al cliente
                        elementos = arbol.obtener_elementos()
                        respuesta = f"Número {numero} insertado. Árbol actual: {elementos}"
                        conexion.send(respuesta.encode())
                        
                        # Visualizar árbol cada 5 números
                        if numeros_recibidos % 5 == 0:
                            arbol.visualizar_arbol()
                    else:
                        conexion.send("Error: Ingrese un número de 2 cifras (10-99)".encode())
                except ValueError:
                    conexion.send("Error: Ingrese un número válido".encode())
                    
    except Exception as e:
        print(f"Error con cliente {direccion}: {e}")
    finally:
        print(f"Cliente {direccion} desconectado")
