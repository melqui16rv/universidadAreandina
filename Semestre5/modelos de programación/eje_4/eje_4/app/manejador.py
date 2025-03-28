import os
from .arbol_binario import ArbolBinario
from .control import apagar, obtener_estado_apagado  # Importar la función para apagar el servidor y verificar estado
from .traductor import traducir_texto  # Importar función que consume Magic Loops
from .borbuja import ordenamiento_burbuja

def manejar_cliente(conexion, direccion, arbol, candado):
    try:
        with conexion:
            while True:
                try:
                    modo = conexion.recv(1024).decode()
                    if not modo:  # Si no hay datos, la conexión se cerró
                        break

                    if modo == "EXIT":
                        break

                    elif modo == "APAGAR_SERVIDOR":
                        print(f"Cliente {direccion} solicitó apagar el servidor")
                        conexion.send("Apagando el servidor...".encode())
                        apagar()
                        return  # Salir inmediatamente del manejador

                    elif modo == "BORRAR_ARBOL":
                        with candado:
                            respuesta = arbol.borrar_arbol()
                        conexion.send(respuesta.encode())

                    elif modo == "MODO_AUTO" or modo == "MODO_MANUAL":
                        numeros_recibidos = 0
                        while numeros_recibidos < 30:
                            datos = conexion.recv(1024).decode().strip()
                            if not datos or datos == "EXIT":
                                return
                            try:
                                numero = int(datos)
                                if 10 <= numero <= 99:
                                    with candado:
                                        arbol.insertar(numero)
                                        numeros_recibidos += 1
                                    elementos = arbol.obtener_elementos()
                                    respuesta = f"Número {numero} insertado. Árbol actual: {elementos}"
                                    conexion.send(respuesta.encode())
                                    if numeros_recibidos % 5 == 0:
                                        arbol.visualizar_arbol()
                                else:
                                    conexion.send("Error: Ingrese un número de 2 cifras (10-99)".encode())
                            except ValueError:
                                conexion.send("Error: Ingrese un número válido".encode())

                    elif modo.startswith("CHAT:"):
                        mensaje = modo[5:]
                        try:
                            respuesta = traducir_texto(mensaje)
                            if not respuesta:  # Si no hay respuesta
                                respuesta = "No se pudo obtener traducción"
                            conexion.send(respuesta.encode())
                        except Exception as e:
                            conexion.send(f"Error en la traducción: {str(e)}".encode())

                    elif modo == "CHAT_EXIT":
                        continue

                    elif modo == "VER_DATOS_INSERCION":
                        with candado:
                            elementos = arbol.obtener_elementos_insercion()
                            respuesta = f"Datos del árbol (orden de inserción): {elementos}"
                            conexion.send(respuesta.encode())

                    elif modo == "VER_DATOS_ORDENADOS":
                        with candado:
                            elementos = arbol.obtener_elementos()
                            elementos_ordenados = ordenamiento_burbuja(elementos.copy())
                            respuesta = f"Datos del árbol ordenados: {elementos_ordenados}"
                            conexion.send(respuesta.encode())

                except Exception as e:
                    print(f"Error al procesar mensaje del cliente: {e}")
                    conexion.send("Error en el servidor".encode())

    except Exception as e:
        print(f"Error con cliente {direccion}: {e}")
    finally:
        print(f"Cliente {direccion} desconectado")
        if obtener_estado_apagado():
            print("Cerrando conexión por apagado del servidor")
