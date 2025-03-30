import os
from .arbol_binario import ArbolBinario
from .control import apagar, obtener_estado_apagado
from .traductor import traducir_texto
from .borbuja import ordenamiento_burbuja
import matplotlib.pyplot as plt

def manejar_cliente(conexion, direccion, arbol, candado):
    modo_actual = None
    numeros_recibidos = 0
    
    try:
        with conexion:
            while True:
                try:
                    datos = conexion.recv(1024).decode()
                    if not datos:
                        break

                    # Cambio de modo
                    if datos in ["MODO_AUTO", "MODO_MANUAL", "MODO_CHAT"]:
                        modo_actual = datos
                        numeros_recibidos = 0
                        continue

                    # Comandos especiales
                    if datos == "EXIT":
                        break
                    elif datos == "APAGAR_SERVIDOR":
                        print(f"Cliente {direccion} solicitó apagar el servidor")
                        conexion.send("Apagando el servidor...".encode())
                        apagar()
                        return  # Salir inmediatamente del manejador
                    elif datos == "BORRAR_ARBOL":
                        with candado:
                            respuesta = arbol.borrar_arbol()
                        conexion.send(respuesta.encode())
                    elif datos == "VER_DATOS_INSERCION":
                        with candado:
                            elementos = arbol.obtener_elementos_insercion()
                            respuesta = f"Datos del árbol (orden de inserción): {elementos}"
                            conexion.send(respuesta.encode())
                    elif datos == "VER_DATOS_ORDENADOS":
                        with candado:
                            elementos = arbol.obtener_elementos()
                            elementos_ordenados = ordenamiento_burbuja(elementos.copy())
                            respuesta = f"Datos del árbol ordenados: {elementos_ordenados}"
                            conexion.send(respuesta.encode())
                    elif datos == "CHAT_EXIT":
                        modo_actual = None
                        continue

                    # Procesar según el modo actual
                    if modo_actual == "MODO_CHAT":
                        if datos.startswith("CHAT:"):
                            mensaje = datos[5:]
                            try:
                                respuesta = traducir_texto(mensaje)
                                conexion.send(respuesta.encode())
                            except Exception as e:
                                conexion.send(f"Error en la traducción: {str(e)}".encode())
                    
                    elif modo_actual in ["MODO_AUTO", "MODO_MANUAL"]:
                        try:
                            numero = int(datos)
                            if 10 <= numero <= 99:
                                with candado:
                                    arbol.insertar(numero)
                                    numeros_recibidos += 1
                                elementos = arbol.obtener_elementos()
                                respuesta = f"Número {numero} insertado. Árbol actual: {elementos}"
                                conexion.send(respuesta.encode())
                            else:
                                conexion.send("Error: Ingrese un número de 2 cifras (10-99)".encode())
                        except ValueError:
                            conexion.send("Error: Ingrese un número válido".encode())

                except Exception as e:
                    print(f"Error al procesar mensaje del cliente: {e}")
                    conexion.send("Error en el servidor".encode())

    except Exception as e:
        print(f"Error con cliente {direccion}: {e}")
    finally:
        print(f"Cliente {direccion} desconectado")
        if obtener_estado_apagado():
            print("Cerrando conexión por apagado del servidor")
            plt.close('all')  # Asegurar que se cierren todas las figuras
