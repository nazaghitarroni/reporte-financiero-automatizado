from dolar import obtenerValorDolar
from cripto import obtenerCriptos
from acciones import obtener_cotizaciones
from fpdf import FPDF
from datetime import datetime
from graficos import crearGrafico
from noticias import obtener_noticias_ambito
import os



def formateadorLinea(titulo, precio):
    return f"{titulo}: ${precio}"

class PDFReporte(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, f"REPORTE FINANCIERO - {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='C')
        self.ln(2)
        self.set_draw_color(100, 100, 100)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

def crearReporte():
    os.makedirs("reportes", exist_ok=True)

    dolar = obtenerValorDolar()
    criptos = obtenerCriptos()
    acciones = obtener_cotizaciones()
    noticias_arg = obtener_noticias_ambito()[:4]

    pdf = PDFReporte()
    pdf.add_page()

    # Cotizaciones
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Cotizaciones", ln=True, align='C')
    pdf.ln(5)

    x_col1 = 15
    x_col2 = 110
    y_start = pdf.get_y()
    line_height = 8
    col_width = 85

    pdf.set_xy(x_col1, y_start)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(col_width, line_height, "Divisas y Criptomonedas", ln=0)

    pdf.set_xy(x_col2, y_start)
    pdf.cell(col_width, line_height, "Acciones", ln=1)
    pdf.set_font("Helvetica", "", 11)

    cotizaciones_izq = [
        formateadorLinea("Dólar Oficial", dolar[0]),
        formateadorLinea("Dólar Blue", dolar[1]),
        formateadorLinea("Bitcoin", criptos[0]),
        formateadorLinea("Ethereum", criptos[1]),
    ]

    cotizaciones_der = [
        formateadorLinea("MERVAL", acciones["MERVAL"]),
        formateadorLinea("AL30", acciones["AL30"]),
        formateadorLinea("GGAL", acciones["GGAL"]),
        "",
    ]

    for i in range(len(cotizaciones_izq)):
        y = pdf.get_y()
        pdf.set_xy(x_col1, y)
        pdf.cell(col_width, line_height, cotizaciones_izq[i], ln=0)
        pdf.set_xy(x_col2, y)
        pdf.cell(col_width, line_height, cotizaciones_der[i], ln=1)

    # Línea divisoria
    pdf.ln(10)
    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    # Noticias destacadas
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Noticias Destacadas", ln=True, align="C")
    pdf.ln(5)

    ancho_texto = 180
    margen_izquierdo = 15

    for noticia in noticias_arg:
        if pdf.get_y() > 240:
            pdf.add_page()

        pdf.set_font("Helvetica", "B", 12)
        pdf.set_x(margen_izquierdo)
        pdf.multi_cell(ancho_texto, 8, noticia["titulo"])
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(0, 0, 255)
        pdf.set_x(margen_izquierdo)
        pdf.write(8, "Leer nota completa", noticia["enlace"])
        pdf.set_text_color(0, 0, 0)
        pdf.ln(10)
        pdf.set_draw_color(210, 210, 210)
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        pdf.ln(5)

    # Página final con gráfico
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Evolución Dolares (Últimos días)", ln=True, align='C')
    pdf.ln(10)

    ruta_grafico = crearGrafico()
    pdf.image(ruta_grafico, x=20, w=170)

    nombre_archivo = f"reportes/Reporte-Financiero-{datetime.now().strftime('%d-%m-%Y')}.pdf"
    pdf.output(nombre_archivo)
    print(f"Reporte guardado en: {nombre_archivo}")

if __name__ == "__main__":
    crearReporte()
