import csv
import matplotlib.pyplot as plt
from datetime import datetime
import os
from dolar import obtenerValorDolar
from cripto import obtenerCriptos 

def crearGrafico():
    fechas = []
    oficial = []
    blue = []
    with open("data/dolar.csv", mode='r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Si hay encabezado
        for fila in reader:
            if len(fila) < 3:
                continue
            fechas.append(datetime.strptime(fila[0], "%Y-%m-%d %H:%M"))
            oficial.append(float(fila[1]))
            blue.append(float(fila[2]))

    plt.plot(fechas, oficial, label="Oficial")
    plt.plot(fechas, blue, label="Blue")
    plt.xlabel("Fecha")
    plt.ylabel("Precio en ARS")
    plt.title("Evolución del dólar oficial y dólar blue")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(f'imagenes/graficos{fechas[-1]}.png')
    plt.close()
    return (f'imagenes/graficos{fechas[-1]}.png')

crearGrafico()