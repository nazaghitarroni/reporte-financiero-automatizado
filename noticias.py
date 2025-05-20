import requests
from bs4 import BeautifulSoup

def obtener_noticias_ambito():
    url = "https://www.ambito.com/economia"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    noticias = []
    for articulo in soup.select("article")[:5]:  # Extrae las primeras 5 noticias
        titulo_tag = articulo.find("h2")
        if titulo_tag:
            titulo = titulo_tag.get_text(strip=True)
            enlace_tag = titulo_tag.find("a")
            enlace = enlace_tag["href"] if enlace_tag else None
            if enlace and not enlace.startswith("http"):
                enlace = "https://www.ambito.com" + enlace
            noticias.append({"titulo": titulo, "enlace": enlace})
    return noticias

# Ejemplo de uso

