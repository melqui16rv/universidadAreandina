def manejar_cliente(conexion, direccion):
    from .traductor import traducir_texto
    try:
        with conexion:
            while True:
                msg = conexion.recv(1024).decode()
                if not msg or msg == "EXIT":
                    break
                if msg.startswith("CHAT:"):
                    mensaje = msg[5:]
                    respuesta = traducir_texto(mensaje)
                    conexion.send(f"Respuesta del Servidor: {respuesta}".encode())
                elif msg == "CHAT_EXIT":
                    conexion.send("Respuesta del Servidor: Chat finalizado".encode())
                    break
                else:
                    conexion.send("Respuesta del Servidor: Comando no soportado".encode())
    except Exception as e:
        try:
            conexion.send("Respuesta del Servidor: Error en la comunicación".encode())
        except:
            pass
