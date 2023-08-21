import smtplib
from colorama import init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from random import randint
from sys import platform
from os import system

def send(sender_email, sender_password, recipient_email, subject, html_content):
    count = 0
    while True:
    	try:
    		smtp_server = 'smtp.gmail.com'
    		smtp_port = 587
    		message = MIMEMultipart('alternative')
    		message['From'] = sender_email
    		message['To'] = recipient_email
    		message['Subject'] = subject
    		html_part = MIMEText(html_content, 'html', 'utf-8')
    		html_part.add_header('Content-Disposition', 'inline')
    		message.attach(html_part)
    		server = smtplib.SMTP(smtp_server, smtp_port)
    		server.starttls()
    		server.login(sender_email, sender_password)
    		server.sendmail(sender_email, recipient_email, message.as_string())
    		server.quit()
    		count += 1
    		print(f'\r   \033[1;38;5;202m│\033[1;38;5;148mSPAMS [{count}]', end='')
    		sleep(randint(0, 4))
    	except:
    		e = ' '
    		print(f'\r   \033[1;38;5;202m│\033[1;38;5;39mSLEEP   {e*len(str(count))}', end='')
    		sleep(60)

if platform in ['win32', 'win64']:
	system('cls')
else:
	system('clear')

init()

print('''
 \033[1;38;5;202m ██████╗███╗   ███╗ █████╗ ██╗██╗
 \033[1;38;5;203m██╔════╝████╗ ████║██╔══██╗██║██║
 \033[1;38;5;204m╚█████╗ ██╔████╔██║███████║██║██║
 \033[1;38;5;205m ╚═══██╗██║╚██╔╝██║██╔══██║██║██║
 \033[1;38;5;206m██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗
 \033[1;38;5;207m╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝''')

c = '■'

for i in range(39):
	print(f'\r \033[1;38;5;93m{c*i}', end='')
	sleep(0.01)

print('\n \033[1;38;5;202m[\033[1;4;38;5;202mDATA\033[0;0m\033[1;38;5;202m]\033[0;0m')

try:
	email = input('   \033[1;38;5;202m│\033[1;38;5;214mEmail: \033[1;38;5;180m')
	msg = input('   \033[1;38;5;202m│\033[1;38;5;214mMessage: \033[1;38;5;180m')
	html_data = f'''<!DOCTYPE html5><html lang='en'><head><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta charset='utf-8'></head><body><p>{msg}</p></body></html>'''
	print(' \033[1;38;5;202m[\033[1;4;38;5;202mPROCCESSING\033[0;0m\033[1;38;5;202m]\033[0;0m')
	send('annonymous.number.444@gmail.com', 'izciuazrjnmwgnxx', email, 'Annonymous', html_data)
except:
	print('\033[0;0m')