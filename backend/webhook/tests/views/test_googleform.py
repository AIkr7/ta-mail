import json
import hmac
import hashlib
import base64

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class TutorRegistrationWebhookTestCase(TestCase):

    def test_google_form_tutor_registration(self):
        url = reverse('googleform-tutor-registration')
        data = json.loads('''{"title":"Pendaftaran Tutor TamanTutors Wave 1","form_id":"10i6p1XMcTYjLorc-iz3LoYpUUi-8SDUxLqy2gSjtnaA","form_response":{"email_respondent":"tamansiswa.indot@gmail.com","answers":[{"name":"Nama lengkap - Nama panggilan kamu","value":"test","inline":false},{"name":"Asal studi - Jurusan - Angkatan masuk kamu","value":"tets","inline":false},{"name":"Nomor telepon kamu","value":"081234567890","inline":false},{"name":"Domisili kamu","value":"test","inline":false},{"name":"Pelajaran yang ingin kamu ajar","value":"Matematika","inline":false},{"name":"Mengapa kamu ingin mengajar?","value":"test","inline":false},{"name":"Bagaimana cara mengajar terbaik menurutmu?","value":"test","inline":false},{"name":"Dari mana kamu mendengar tentang TamanTutors?","value":"Teman","inline":false},{"name":"CV kamu","value":"1uF3hZLkWhPkhLglzRTLnfKDzHl6Z8EEt","inline":false},{"name":"Kartu Tanda Siswa/Mahasiswa kamu","value":"184yuq_Q3J2NlsVkL9mC6j0nSGuadhmsv","inline":false}]}}''')
        response = self.client.post(url, data=data, content_type='application/json', HTTP_API_KEY=settings.SECRET_KEY)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, str(response.content))


class MatchMakingWebhookTestCase(TestCase):

    def test_google_form_matchmaking(self):
        url = reverse('googleform-matchmaking')
        data = json.loads('''{"title":"Pesan Tutor","form_id":"1O6pKadjJVC0jO04rQ_iQu-mTlOEo4YwK37MRZDw_Xvk","form_response":{"email_respondent":"fijarlaz@gmail.com","answers":[{"name":"Nama Panggilan","value":"Fijar","inline":false},{"name":"Nomor Handphone / ID LINE","value":"081247938013 / fijarlaz","inline":false},{"name":"Asal studi kamu - Jurusan - Tingkat ","value":"UI - Ilkom - Semester 3","inline":false},{"name":"Mata Pelajaran/Kuliah yang Ingin Dipelajari ","value":"Computer Science","inline":false},{"name":"Materi dari Mata Pelajaran/Kuliah yang Ingin Dipelajari ","value":"Sistem Cerdas","inline":false},{"name":"Tujuan Belajar (Bisa Pilih >1)","value":"Mengikuti rasa ingin tahu","inline":false},{"name":"Tanggal Belajar","value":"2019-09-26","inline":false},{"name":"Jam Mulai","value":"10:00","inline":false},{"name":"Jam Selesai","value":"12:00","inline":false},{"name":"Jumlah Peserta Belajar (Termasuk Pemesan)","value":"5","inline":false},{"name":"Lokasi Belajar Pilihan - Alamat","value":"Kutek","inline":false},{"name":"Apakah Kamu Ingin Berlangganan TamanTutors?","value":"Ya, aku ingin berlangganan.","inline":false}]}}''')
        response = self.client.post(url, data=data, content_type='application/json', HTTP_API_KEY=settings.SECRET_KEY)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, str(response.content))
