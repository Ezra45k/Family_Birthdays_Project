import easyimap as e
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage


class DynamicEmail:

    def __init__(self):
        load_dotenv('.env')
        self.username = os.getenv('EMAIL_USERNAME')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.server = None

    def connect_server(self):
        print(f'Username: {self.username} \n'
              f'Password: {self.password}')
        self.server = e.connect('imap.gmail.com', self.username, self.password)
        print('Successfully connected.')

    def send_email(self, to, subject, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['to'] = to
        msg['From'] = self.username
        print(f'BEFORE EMAIL LOGIN'
              f'\nUsername: {self.username} \n'
              f'Password: {self.password}')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.username, self.password)
        self.server.send_message(msg)
        print('Successful mission.')
        self.server.quit()


if __name__ == '__main__':
    object = DynamicEmail()
    object.connect_server()
    object.send_email('9738205999@vtext.com', 'Cool', 'It worked!!')
