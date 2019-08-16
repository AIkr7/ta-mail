import json
from django.test import TestCase
from backend.apps.matchmaking.services import MatchmakingNotificationService

class MatchmakingNotificationServiceTestCase(TestCase):

    def setUp(self):
        self.form_response = json.loads('''{
            "form_id": "lT4Z3j",
            "token": "a3a12ec67a1365927098a606107fac15",
            "submitted_at": "2018-01-18T18:17:02Z",
            "landed_at": "2018-01-18T18:07:02Z",
            "definition": {
                "id": "lT4Z3j",
                "title": "Webhooks example",
                "fields": [
                    {
                        "id": "SMEUb7VJz92Q",
                        "title": "Email Kamu",
                        "type": "email",
                        "ref": "email_registration",
                        "allow_multiple_selections": false,
                        "allow_other_choice": false
                    }
                ]
            },
            "answers": [
                {
                    "type": "email",
                    "email": "wisnu.under@gmail.com",
                    "field": {
                        "id": "SMEUb7VJz92Q",
                        "type": "email"
                    }
                }
            ]
        }''')

    def test_send_response_for_tutor_request(self):
        service = MatchmakingNotificationService()
        raised = False
        err = ''
        try:
            service.send_response_for_tutor_request(self.form_response)
        except Exception as e:
            err = str(e)
            raised = True
        self.assertFalse(raised, 'Send Matchmaking notification failed: ' + err)
