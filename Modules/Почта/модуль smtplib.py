# материал этого конспекта: https://code.tutsplus.com/ru/tutorials/sending-emails-in-python-with-smtp--cms-29975
"""
Следующий скрипт позволит вам отправить электронное письмо через SMTP-сервер Gmail.
Тем не менее, Google не разрешит вход через smtplib, поскольку этот тип входа помечен как «менее безопасный».
Чтобы решить эту проблему, перейдите на страницу https://www.google.com/settings/security/lesssecureapps,
когда вы вошли в свою учетную запись Google, и «Разрешить менее безопасные приложения».
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()
message = "Это письмо, сгенерированное роботом"

# setup the parameters of the message
password = ""
msg['From'] = ""
msg['To'] = ""
msg['Subject'] = "Subscription"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
