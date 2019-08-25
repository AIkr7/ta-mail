import json
from django.test import TestCase
from backend.apps.matchmaking.services import MatchmakingNotificationService
from backend.apps.matchmaking.services import TutorRegistrationNotificationService


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
        self.assertFalse(
            raised, 'Send Matchmaking notification failed: ' + err)


class TutorRegistrationNotificationServiceTestCase(TestCase):

    def setUp(self):
        self.response = json.loads(
            '''{"title":"Pendaftaran Tutor TamanTutors Wave 1","form_id":"10i6p1XMcTYjLorc-iz3LoYpUUi-8SDUxLqy2gSjtnaA","form_response":{"email_respondent":"tamansiswa.indot@gmail.com","answers":[{"name":"Nama lengkap - Nama panggilan kamu","value":"test","inline":false},{"name":"Asal studi - Jurusan - Angkatan masuk kamu","value":"tets","inline":false},{"name":"Nomor telepon kamu","value":"081234567890","inline":false},{"name":"Domisili kamu","value":"test","inline":false},{"name":"Pelajaran yang ingin kamu ajar","value":"Matematika","inline":false},{"name":"Mengapa kamu ingin mengajar?","value":"test","inline":false},{"name":"Bagaimana cara mengajar terbaik menurutmu?","value":"test","inline":false},{"name":"Dari mana kamu mendengar tentang TamanTutors?","value":"Teman","inline":false},{"name":"CV kamu","value":"1uF3hZLkWhPkhLglzRTLnfKDzHl6Z8EEt","inline":false},{"name":"Kartu Tanda Siswa/Mahasiswa kamu","value":"184yuq_Q3J2NlsVkL9mC6j0nSGuadhmsv","inline":false}]}}''')

    def test_send_form_registration_feedback(self):
        service = TutorRegistrationNotificationService()
        raised = False
        err = ''
        try:
            email = self.response.get('form_response').get('email_respondent')
            service.send_form_registration_feedback(
                email, self.response.get('form_response').get('answers'))
        except Exception as e:
            err = str(e)
            raised = True
        self.assertFalse(
            raised, 'Send Form Registration Feedback notification failed: ' + err)
