import socket
import time
from utils.codificador import formatear_mensaje, decodificar_mensaje
from cliente.preguntas import PREGUNTAS

SERVIDOR = '127.0.0.1'
PUERTO = 65432


def enviar_30_numeros(cliente):
    print("\nEnviando 30 números al servidor...")
    for i in range(30):
        while True:
            try:
                num = int(input(f"Ingrese el número #{i+1} (2 cifras): "))
                if 10 <= num <= 99:
                    cliente.send(formatear_mensaje(str(num)))
                    confirmacion = decodificar_mensaje(cliente.recv(1024))
                    print(f"Servidor: {confirmacion}")
                    break
                else:
                    print("Debe ser un número de 2 cifras (entre 10 y 99).")
            except ValueError:
                print("Ingrese un número válido.")


def menu_preguntas(cliente):
    while True:
        print("\n--- CHAT CON EL SERVIDOR (5 preguntas) ---")
        for idx, pregunta in enumerate(PREGUNTAS, 1):
            print(f"{idx}. {pregunta}")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "6":
            cliente.send(formatear_mensaje("salir"))
            print("\nConexión finalizada.")
            break

        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            seleccion = PREGUNTAS[int(opcion)-1]
            cliente.send(formatear_mensaje(seleccion))
            respuesta = decodificar_mensaje(cliente.recv(2048))
            print(f"\nServidor responde: {respuesta}")
        else:
            print("Opción inválida.")


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((SERVIDOR, PUERTO))
            print("Conectado al servidor.")

            enviar_30_numeros(cliente)
            menu_preguntas(cliente)

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que esté en ejecución.")


if __name__ == "__main__":
    main()
