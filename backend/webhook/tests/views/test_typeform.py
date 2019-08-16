import json

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class MatchmakingNotificationServiceTestCase(TestCase):

    def setUp(self):
        self.form_response = {
            "event_id": "01DJDG5S6JTG0D4VGB3Y3K3X2M",
            "event_type": "form_response",
            "form_response": {
                "form_id": "cJKPNZ",
                "token": "01DJDG5S6JTG0D4VGB3Y3K3X2M",
                "landed_at": "2019-08-16T15:19:14Z",
                "submitted_at": "2019-08-16T15:19:14Z",
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
                        "text": "Lorem ipsum dolor",
                        "field": {
                            "id": "RWtYIE4ZZ9nJ",
                            "type": "short_text",
                            "ref": "b15fcb29-2573-48e1-8178-3f3f6662fc04"
                        }
                    },
                    {
                        "type": "email",
                        "email": "an_account@example.com",
                        "field": {
                            "id": "yXz5sq71BEW9",
                            "type": "email",
                            "ref": "email_registration"
                        }
                    }
                ]
            }
        }

    def test_send_response_typeform_matchmaking_student(self):
        url = reverse('typeform-matchmaking-student')
        data = self.form_response.copy()
        encoded_secret = 'sha256=MLaRuhw63AbfMCqNFwtrV+D9FmKbZ1q0YQqwSVMGsuY='
        response = self.client.post(
            url, data=data, HTTP_TYPEFORM_SIGNATURE=encoded_secret, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
