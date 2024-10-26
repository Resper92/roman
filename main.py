from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_templlate = Template(Path("templates/index.html").read_text())
html_cont = html_templlate.substitute({'name': 'Irene', 'date': 'tomorow'})

my_email['to'] = 'irebades@icloud.com'
my_email['subject'] = "lets go out"
my_email.set_content(html_cont, 'html')

with smtplib.SMTP("smtp.gmail.com", 587)as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login('romanovskyyroman@gmail.com', 'korv ogvl ztoy qxss')
    smtp_server.send_message(my_email)
    print('succes')
