import smtplib
import ssl
import os


def send_mail(message, reciever = 'ruthvick.bandaru@stonybrook.edu'):
    """
    This function uses the smtplib and ssl libraries to send an email from
    an email address whose access key has been provided in the system environments
    :param message:
    :param reciever:
    :return:
    """
    host = 'smtp.gmail.com'
    port = '465'

    username = 'ruthvick2005@gmail.com'
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
