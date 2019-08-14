import logging

from django.core.mail import EmailMessage
from django.core.mail import send_mail

logger = logging.getLogger('GMAIL')

default_sender_name = 'Taman Siswa'
default_sender_address = 'tamansiswa.indo@gmail.com'

class GmailManager:

    @staticmethod
    def create_email_messsage(
            subject,
            body,
            to,
            sender_name=default_sender_name,
            sender_address=default_sender_address,
            content_subtype="html",
            **kwargs):
        from_email = f'{sender_name} <{sender_address}>'
        email = EmailMessage(subject, body, from_email, to, **kwargs)
        email.content_subtype = content_subtype
        return email

    def send_message(self, email_message: EmailMessage):
        try:
            email_message.send(fail_silently=False)
        except Exception as e:
            logger.error(str(e))
