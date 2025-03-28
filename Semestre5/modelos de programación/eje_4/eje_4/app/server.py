from .manejador import manejar_cliente
from .arbol_binario import ArbolBinario
from .control import apagar, obtener_estado_apagado
import socket
import threading
import sys
from flask import Flask, render_template, send_file, jsonify, request, redirect, url_for

SERVIDOR = '127.0.0.1'
PUERTO = 65432
PUERTO_BASE = 65432
puertos_disponibles = set(range(PUERTO_BASE + 1, PUERTO_BASE + 100))  # Rango de puertos dinámicos
arbol_binario = ArbolBinario()
candado = threading.Lock()
app = Flask(__name__)

PASSWORD = "eje_4"
servidor_activo = True  # Estado del servidor

def iniciar_servidor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((SERVIDOR, PUERTO))
            servidor.listen()
            print(f"Servidor escuchando en {SERVIDOR}:{PUERTO}...")

            while not obtener_estado_apagado():
                try:
                    servidor.settimeout(1)
                    conexion, direccion = servidor.accept()
                    print(f"Cliente conectado desde {direccion}")
                    hilo = threading.Thread(target=manejar_cliente, 
                                             args=(conexion, direccion, arbol_binario, candado))
                    hilo.start()
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"Error en la conexión: {e}")

    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        print("Servidor apagado correctamente.")
        sys.exit(0)  # Asegura que el programa termine completamente

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imagen')
def imagen():
    arbol_binario.visualizar_arbol()
    return send_file('/Users/melquiromero/Documents/GitHub/universidadAreandina/Semestre5/modelos de programación/eje_4/eje_4/vistaArbol/arbol_binario.png', mimetype='image/png')

@app.route('/menu', methods=['POST'])
def menu():
    opcion = request.json.get('opcion')
    # Procesar la opción seleccionada (similar al cliente)
    # ... lógica para manejar las opciones ...
    return jsonify({"mensaje": "Opción procesada correctamente"})

@app.route('/obtener_puerto', methods=['GET'])
def obtener_puerto():
    if puertos_disponibles:
        puerto = puertos_disponibles.pop()
        return jsonify({"puerto": puerto})
    return jsonify({"error": "No hay puertos disponibles"}), 500

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            return redirect(url_for('control_servidor'))
        else:
            return render_template('admin.html', error="Contraseña incorrecta")
    return render_template('admin.html')

@app.route('/control_servidor', methods=['GET', 'POST'])
def control_servidor():
    global servidor_activo
    if request.method == 'POST':
        accion = request.form.get('accion')
        if accion == 'apagar':
            servidor_activo = False
            return render_template('control_servidor.html', estado="Servidor apagado", servidor_activo=servidor_activo)
        elif accion == 'activar':
            servidor_activo = True
            return render_template('control_servidor.html', estado="Servidor activado", servidor_activo=servidor_activo)
    return render_template('control_servidor.html', estado="Servidor activo" if servidor_activo else "Servidor apagado", servidor_activo=servidor_activo)

if __name__ == "__main__":
    iniciar_servidor()
