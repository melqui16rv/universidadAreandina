import random
import threading
import time

def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j], arreglo[j]
    return arreglo

def generar_numero():
    return random.randint(1, 10)

def generar_numeros_hilo(numeros, candado):
    while True:
        with candado:
            if len(numeros) < 5:
                numeros.append(generar_numero())
        time.sleep(1)

def formatear_mensaje(mensaje):
    return mensaje.encode('utf-8')

def decodificar_mensaje(mensaje):
    return mensaje.decode('utf-8')
