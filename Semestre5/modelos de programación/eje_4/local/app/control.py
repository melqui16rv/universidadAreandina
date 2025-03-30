apagar_servidor = False

def apagar():
    global apagar_servidor
    apagar_servidor = True

def obtener_estado_apagado():
    return apagar_servidor
