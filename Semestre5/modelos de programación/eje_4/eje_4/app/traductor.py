import requests
import json

def traducir_texto(texto, target_language="en"):
    url = 'https://magicloops.dev/api/loop/run/f07aa2b8-e360-46e4-aedd-8bc5c7746a25'
    payload = {"text": texto, "targetLanguage": target_language}
    
    try:
        response = requests.get(url, json=payload)
        if response.status_code == 200:
            try:
                responseJson = response.json()
                # Extraer solo la traducción (loopOutput) del JSON
                traduccion = responseJson.get('loopOutput', 'No se encontró traducción')
                return f"Traducción: {traduccion}"
            except json.JSONDecodeError:
                return "Error: No se pudo procesar la respuesta del servidor"
            except Exception as e:
                return f"Error al procesar la respuesta: {str(e)}"
        else:
            return f"Error en la traducción. Código: {response.status_code}"
    except Exception as e:
        return f"Error de conexión: {str(e)}"


