from flask import Flask, render_template, request, jsonify
from .traductor import traducir_texto 
import socket, threading
from .manejador import manejar_cliente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje = data.get("mensaje")
    if not mensaje:
        return jsonify({"mensaje": "Respuesta del Servidor: Mensaje vacío"}), 400
    respuesta = traducir_texto(mensaje)
    return jsonify({"mensaje": f"Respuesta del Servidor: {respuesta}"})

def iniciar_socket_server():
    HOST = '0.0.0.0'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conexion, direccion = s.accept()
            threading.Thread(target=manejar_cliente, args=(conexion, direccion), daemon=True).start()

if __name__ == "__main__":
    # Iniciar hilo de socket para chat
    threading.Thread(target=iniciar_socket_server, daemon=True).start()
    app.run(debug=True)
