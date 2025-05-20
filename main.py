import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import time
from crearReporte import crearReporte 

cont = 0

for i in range(1):
    try:
        EMAIL = "robotitosautomaticos@gmail.com"
        PASSWORD = "zxsr lmcu zohk dfot"
        RECEPTOR = "cabreracsophia@gmail.com"
        pdf = crearReporte()
        dia = datetime.now().strftime("%d-%m-%Y-%H-%m")
        mensaje = MIMEMultipart()
        mensaje["Subject"] = "Reporte financiero diario."
        mensaje["From"] = EMAIL
        mensaje["TO"] = RECEPTOR

        cuerpo = MIMEText("Estimado,\nAdjunto reporte financiero diario.\n\nSaludos.", 'plain')
        mensaje.attach(cuerpo)

        with open(f"reportes/Reporte-Financiero-{datetime.now().strftime('%d-%m-%Y')}.pdf", "rb") as f:
            adjunto = MIMEApplication(f.read(), _subtype="pdf")
            adjunto.add_header("Content-Disposition", "attachment", filename="reporte-financiero.pdf")
            mensaje.attach(adjunto)

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, RECEPTOR,mensaje.as_string())
        print("Alerta enviada.")
    except Exception as e:
        print("Error: ", e)
    time.sleep(5)