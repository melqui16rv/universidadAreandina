import threading
from arbol.arbol_binario import *
from utils.codificador import *
from vistas.consola_arbol import *

arboles_por_cliente = {}
candado = threading.Lock()


def manejar_cliente(conexion, direccion, id_cliente):
    print(f"Cliente {id_cliente} conectado desde {direccion}")
    arbol = ArbolBinario()

    try:
        # Recibir 30 números
        for i in range(30):
            data = conexion.recv(1024)
            numero = int(decodificar_mensaje(data))
            arbol.insertar(numero)
            conexion.send(formatear_mensaje(f"Número {numero} insertado correctamente."))

        # Menú de preguntas
        while True:
            data = conexion.recv(1024)
            pregunta = decodificar_mensaje(data)
            if pregunta == "salir":
                break

            respuesta = responder_pregunta(pregunta, arbol)
            conexion.send(formatear_mensaje(respuesta))

    except Exception as e:
        print(f"Error con cliente {id_cliente}: {e}")
    finally:
        conexion.close()
        print(f"Cliente {id_cliente} desconectado")


def responder_pregunta(pregunta, arbol):
    if "raíz" in pregunta or "raiz" in pregunta:
        return f"La raíz del árbol es: {arbol.raiz.valor if arbol.raiz else 'Árbol vacío'}"

    elif "nodos" in pregunta:
        return f"El árbol tiene {arbol.cantidad_elementos()} nodos."

    elif "recorrido" in pregunta:
        elementos = arbol.obtener_elementos()
        return f"Recorrido en orden: {elementos}"

    elif "altura" in pregunta:
        return f"La altura del árbol es: {arbol.altura()}"

    elif "mayor" in pregunta or "menor" in pregunta:
        mayor = arbol.mayor()
        menor = arbol.menor()
        return f"Mayor: {mayor}, Menor: {menor}"

    else:
        return "No entiendo la pregunta."

# Esta función se usará desde server.py al aceptar una nueva conexión
