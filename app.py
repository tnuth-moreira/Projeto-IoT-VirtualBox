import network
import time
import urequests
from machine import Pin
from dht import DHT11

ssid = "YOU_SSID"
password = "YOU_PASSWORD"

dht_pin = Pin(4)
dht_sensor = DHT11(dht_pin)
relay_pin = Pin(5, Pin.OUT)
relay_pin.off()

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print("Conectando ao Wi-Fi...")
        time.sleep(1)
    print("Conectado ao Wi-Fi")

def send_to_thingspeak(temperature, humidity):
    write_api_key = "FR2HSQN9D8O34H0H"
    url = f"https://api.thingspeak.com/update?api_key={write_api_key}&field1={temperature}&field2={humidity}"
    response = urequests.get(url)
    print("Status do envio:", response.status_code)
    print("Corpo da resposta:", response.text)
    response.close()

connect_wifi()

while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        print("Temperatura:", temperature, "°C", "Umidade:", humidity, "%")
        
        if temperature > 31 or humidity > 70:
            relay_pin.on()
        else:
            relay_pin.off()
        
        send_to_thingspeak(temperature, humidity)
        
    except OSError:
        print("Falha ao ler o sensor DHT!")
    
    time.sleep(20)
