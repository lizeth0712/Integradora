import requests
import json
import time

SHELLY_IP = "10.2.1.178" #ip del shelly
SHELLY_PORT = 80  # El puerto predeterminado es 80
SHELLY_USERNAME = "sotolizeth50@gmail.com"  # user de la cuenta activada
SHELLY_PASSWORD = "#######"  # pass de la cuenta activada

# Variables para almacenar el último valor registrado
ultimo_temperatura = "No disponible"
ultimo_humedad = "No disponible"

def obtener_datos_shelly():
    #url de la peticion
    url = f"http://{SHELLY_IP}:{SHELLY_PORT}/status"

    try:
        # obtencion de datos de la peticion
        respuesta = requests.get(url, auth=(SHELLY_USERNAME, SHELLY_PASSWORD))
        #datos en formato json convertidos a text
        datos = json.loads(respuesta.text)
        return datos
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

while True:
    datos_shelly = obtener_datos_shelly()

    if datos_shelly:
        #asignar el valor de temperatura y humedad
        temperatura = datos_shelly.get("tmp", {}).get("value", "No disponible")
        humedad = datos_shelly.get("hum", {}).get("value", "No disponible")

        # Actualiza los últimos valores registrados
        ultimo_temperatura = temperatura
        ultimo_humedad = humedad
    
        #imprime los valores
        print(f"Temperatura: {temperatura} °C, Humedad: {humedad}%")

    else:
        # Muestra los últimos valores registrados si no se pueden obtener nuevos datos
        print(f"Última lectura: Temperatura: {ultimo_temperatura} °C, Humedad: {ultimo_humedad}%")

    time.sleep(5)  # Actualiza cada 5 segundos
