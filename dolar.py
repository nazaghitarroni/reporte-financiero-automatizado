import requests
import csv
from datetime import datetime
import time



def obtenerValorDolar():
    try:
        dolar = requests.get("https://api.bluelytics.com.ar/v2/latest").json()
        oficial = (dolar['oficial']['value_avg'])
        blue = (dolar['blue']['value_avg'])
        brecha = round(((blue-oficial)/oficial)*100,2)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        with open('data/dolar.csv', mode="a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([fecha,oficial,blue,brecha])

        return [oficial,blue,brecha]

    except Exception as e:
        print(e)
        
    time.sleep(5)

obtenerValorDolar()
