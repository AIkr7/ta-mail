import logging

from django.conf import settings
from backend.libs.client import Client
from backend.libs.client import ClientError

DOMAIN_NAME = 'mg.taman-siswa.com'
MAILGUN_API_URL = f'https://api.mailgun.net/v3/{DOMAIN_NAME}'

logger = logging.getLogger('MAILGUN')


class MailgunClient(Client):

    def __init__(self, *args, **kwargs):
        return super().__init__(MAILGUN_API_URL, auth=('api', settings.MAILGUN_API_KEY), *args, **kwargs)

    def get_headers(self, original_headers={}):
        return original_headers


class MailgunManager:
    client = MailgunClient()

    def send_message(self,
                      sender_name,
                      sender_address,
                      recipient_address,
                      subject,
                      content,
                      bcc=[],
                      cc=[],
                      attachments=[],
                      track_open=False,
                      extra_variables={},
                      tag=None,):

        files = []
        for filename, file_handle in attachments:
            files.append(("attachment", (filename, file_handle.read())))

        sender = "%s <%s@%s>" % (sender_name, sender_address, DOMAIN_NAME)

        parameters = {
            "sender": sender,
            "from": sender,
            "to": recipient_address,
            "subject": subject,
            "html": content,
            "o:tracking": "yes" if track_open else "no",
            "o:tracking-clicks": "no",
        }

        for key in extra_variables.keys():
            parameters["v:%s" % key] = extra_variables[key]

        if tag:
            parameters["o:tag"] = tag

        try:
            response = self.client.post(
                '/messages', data=parameters, files=files)
            logger.info(
                msg=f'Mailgun Success: {sender} -> {recipient_address}')
            return response
        except ClientError as ce:
            logger.error(
                msg=f'Mailgun Error: {sender} -> {recipient_address} {str(ce)}')
            raise ce
        except Exception as e:
            logger.error(msg=f'Exception Error: {str(ce)}')
            raise e
