import json
import hmac
import hashlib
import base64

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class MatchmakingNotificationServiceTestCase(TestCase):

    def test_send_response_typeform_matchmaking_student(self):
        url = reverse('typeform-matchmaking-student')
        data = {
            "event_id": "01DJDHXETDWY0H6T4N6P2ZEQBB",
            "event_type": "form_response",
            "form_response": {
                "form_id": "cJKPNZ",
                "token": "z08q06tbnl6jg53un7z08q068l9uez1f",
                "landed_at": "2019-08-16T15:49:27Z",
                "submitted_at": "2019-08-16T15:49:38Z",
                "definition": {
                    "id": "cJKPNZ",
                    "title": "Daftar Matchmaking Siswa",
                    "fields": [
                        {
                            "id": "RWtYIE4ZZ9nJ",
                            "title": "Nama Lengkap Kamu",
                            "type": "short_text",
                            "ref": "b15fcb29-2573-48e1-8178-3f3f6662fc04",
                            "properties": {}
                        },
                        {
                            "id": "yXz5sq71BEW9",
                            "title": "Email Kamu",
                            "type": "email",
                            "ref": "email_registration",
                            "properties": {}
                        }
                    ]
                },
                "answers": [
                    {
                        "type": "text",
                        "text": "Wisnu Test",
                        "field": {
                            "id": "RWtYIE4ZZ9nJ",
                            "type": "short_text",
                            "ref": "b15fcb29-2573-48e1-8178-3f3f6662fc04"
                        }
                    },
                    {
                        "type": "email",
                        "email": "wisnuprama014@gmail.com",
                        "field": {
                            "id": "yXz5sq71BEW9",
                            "type": "email",
                            "ref": "email_registration"
                        }
                    }
                ]
            },
        }
        encoded_secret = 'sha256=XYrHQ0j6kWZPe1zgfGJL2mJaqHb+lkRJPXwVKrV9JSE='
        response = self.client.post(
            url, data=data, HTTP_TYPEFORM_SIGNATURE=encoded_secret, content_type='application/json')
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, str(response.content))
