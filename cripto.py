import requests
import csv
from datetime import datetime
import os
import time

def obtenerCriptos(reintentos=3, espera=5):
    url_coingecko = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,usdt&vs_currencies=usd"
    
    # Asegurar que la carpeta 'data' existe
    os.makedirs("data", exist_ok=True)

    for intento in range(reintentos):
        try:
            response = requests.get(url_coingecko, timeout=10)
            response.raise_for_status()  # Lanza error si status != 200
            data = response.json()
            bitcoin = data['bitcoin']['usd']
            ethereum = data['ethereum']['usd']
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

            with open('data/cripto.csv', mode='a', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([fecha, bitcoin, ethereum])

            return [bitcoin, ethereum]

        except Exception as e:
            print(f"Error al obtener criptos (intento {intento+1}): {e}")
            if intento < reintentos - 1:
                time.sleep(espera)
            else:
                print("No se pudo obtener la información después de varios intentos.")
                return None
