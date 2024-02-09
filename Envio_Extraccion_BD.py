import network
import time
import urequests
from machine import Pin
from time import sleep

timeout = 0

#declaracion pines a los led de prueba
led_r=Pin(13, Pin.OUT)
led_a=Pin(12, Pin.OUT)

# Instanciamos el objeto wifi para controlar la interfaz STA
wifi = network.WLAN(network.STA_IF)
# Activamos la interfaz STA del ESP32
wifi.active(True)

# Iniciamos la conexión con los datos de nuestro AP
wifi.connect('Lab_IoT_5', '12345678ap')

if not wifi.isconnected():
    print("Conectando...")
    while not wifi.isconnected() and timeout < 5:
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)

if wifi.isconnected():
    print("Conectado")
    
    # Realizamos la solicitud GET al servidor
    url = 'http://192.168.0.10/obtener.php'
    req = urequests.get(url)
    
    # Manejamos la respuesta del servidor
    if req.status_code == 200:
        # Imprimimos el contenido de la respuesta
        response_text= req.text
        print(response_text)
        
        #el mensaje contiene letras y buscamos solo el valor numerico
        temp_start = response_text.find('=') + 1
        temp_str = response_text[temp_start:].strip()
        
        
        try:
        # Convertimos el valor a float
            temperatura = float(temp_str)
            
            # Ahora puedes usar la variable "temperatura" en tus condiciones
            if temperatura > 30.0:
                print("La temperatura es mayor a 30 grados")
                led_r.value(1)
                sleep(0.5)
                
            else:
                print("La temperatura es igual o menor a 30 grados")
                led_a.value(1)
                sleep(0.5)
                
        except ValueError:
            print("Error al buscar el valor numerico")
    else:
        print("Error al obtener datos. Código de estado:", req.status_code)

else:
    print('Time Out')
    print('No conectado')