def dibujar_arbol(nodo, prefijo="", es_izquierda=True):
    if nodo is not None:
        resultado = ""
        resultado += dibujar_arbol(nodo.derecha, prefijo + ("│   " if es_izquierda else "    "), False)
        resultado += f"{prefijo}{'└── ' if es_izquierda else '┌── '}{nodo.valor}\n"
        resultado += dibujar_arbol(nodo.izquierda, prefijo + ("    " if es_izquierda else "│   "), True)
        return resultado
    return ""

# Para usarlo desde el servidor o el cliente (modo texto):
# print(dibujar_arbol(arbol.raiz))
