apagar_servidor = False  # Variable global para controlar el apagado del servidor

def apagar():
    global apagar_servidor
    apagar_servidor = True

def obtener_estado_apagado():
    return apagar_servidor
