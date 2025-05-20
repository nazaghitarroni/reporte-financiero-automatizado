import requests
from bs4 import BeautifulSoup

def obtener_cotizaciones():
    resultados = {}

    # GGAL desde InvertirOnline
    try:
        url_ggal = "https://iol.invertironline.com/titulo/cotizacion/bcba/ggal/grupo-financiero-galicia-s.a"
        response = requests.get(url_ggal)
        soup = BeautifulSoup(response.text, "html.parser")
        precio_ggal = soup.select_one(".titulo-dato-precio .main-value")
        resultados["GGAL"] = precio_ggal.text.strip() if precio_ggal else "No encontrado"
    except Exception as e:
        resultados["GGAL"] = f"Error: {e}"

    # AL30 desde InvertirOnline
    try:
        url_al30 = "https://iol.invertironline.com/titulo/cotizacion/bcba/al30d/bono-rep.-argentina-usd-step-up-2030"
        response = requests.get(url_al30)
        soup = BeautifulSoup(response.text, "html.parser")
        precio_al30 = soup.select_one(".titulo-dato-precio .main-value")
        resultados["AL30"] = precio_al30.text.strip() if precio_al30 else "No encontrado"
    except Exception as e:
        resultados["AL30"] = f"Error: {e}"

    # MERVAL desde TradingView
    try:
        url_merval = "https://es.tradingview.com/symbols/BCBA-IMV/"
        response = requests.get(url_merval, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        precio_merval = soup.select_one("div.tv-symbol-price-quote__value")
        resultados["MERVAL"] = precio_merval.text.strip() if precio_merval else "No encontrado"
    except Exception as e:
        resultados["MERVAL"] = f"Error: {e}"

    return resultados

# Ejecutar para probar individualmente
if __name__ == "__main__":
    cotizaciones = obtener_cotizaciones()
    for activo, precio in cotizaciones.items():
        print(f"{activo}: {precio}")
