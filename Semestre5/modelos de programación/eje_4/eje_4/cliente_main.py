import requests
from app.cliente import iniciar_cliente

if __name__ == "__main__":
    try:
        response = requests.get("http://127.0.0.1:5000/obtener_puerto")
        if response.status_code == 200:
            puerto = response.json().get("puerto")
            print(f"Conectando al servidor en el puerto dinámico: {puerto}")
            iniciar_cliente(puerto)
        else:
            print("Error al obtener un puerto dinámico del servidor")
    except Exception as e:
        print(f"Error al conectar con el servidor: {e}")
