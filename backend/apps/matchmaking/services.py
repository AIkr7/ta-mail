from rest_framework.exceptions import ValidationError
from backend.clients.gmail import GmailManager


class MatchmakingNotificationService:

    email_manager = GmailManager()

    def _get_typeform_definition_by_qref(self, qref: str, fields: list):
        for f in fields:
            if f.get('ref') == qref:
                return f
        return None

    def _get_email_registration(self, answers: list, definition: dict):
        EMAIL_REF = 'email_registration'
        customer_email_def = self._get_typeform_definition_by_qref(
            EMAIL_REF, definition.get('fields'))

        if customer_email_def is None:
            raise ValidationError('No Customer Email Definition Found')

        customer_email_field_id = customer_email_def.get('id')
        for ans in answers:
            if ans.get('field').get('id') == customer_email_field_id:
                # people may forget to set type to email field
                return ans.get('email', ans.get('text'))

        raise ValidationError('No Customer Email Found')

    def _tmp_generate_html(self, answers, definition):
        return '<html><p>Mohon menunggu hingga team kami menghubungi anda melalui email ini.</p></html>'

    def send_response_for_tutor_request(self, form_response: dict):
        sender_address = 'tamansiswa.indo'
        answer = form_response.get('answers')
        definition = form_response.get('definition')
        customer_email = self._get_email_registration(answer, definition)

        subject = 'Pencarian Tutor sedang diproses'
        content = self._tmp_generate_html(answer, definition)
        bcc = ['chef.riskyaltaresh@gmail.com']
        reply_to = ['tamansiswa.indo+helpdesk@gmail.com']
        email = self.email_manager.create_email_messsage(
            subject=subject, body=content, to=[customer_email], bcc=bcc, reply_to=reply_to)
        self.email_manager.send_message(email)


    def generate_html_message(self, answer: list):
        return '''<div dir="ltr">Halo Tutee, terima kasih sudah menjadikan TamanTutors menjadi teman belajarmu. 
        Pesananmu sudah diproses oleh admin. Selanjutnya admin akan mencocokkan jadwalmu dengan Tutor yang akan mengajar. 
        Setelah kecocokan jadwal dan Tutor sudah berhasil dilakukan, admin akan menghubungimu melalui Official Account Line untuk memberikan jadwal dan tempat belajarmu. 
        Selamat belajar Tutee :)</div>
        <div></div><div><br></div><div></div><div><br></div><div>Cheers!</div><div><div><div><div><br>
        <div dir="ltr" class="gmail_signature"><div dir="ltr"><div><div dir=
        ="ltr"><font color="#6aa84f" size="6" face="tahoma, sans-serif"><b>
        Ares</b></font><div><font color="#000000" size="4" face="tahoma, sans-serif"><b>CEO &amp; Co-founder, TamanSiswa</b>
        </font></div><div><font color="#000000" size="4" face="tahoma, sans-serif"><br></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">LINE : <a href="http://line.me/ti/p/~tamansiswa" target="_blank">@tamansiswa</a></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">Instagram : <a href="https://www.instagram.com/tamansiswa_/" target="_blank">@tamansiswa_</a></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">Email : <a href="mailto:tamansiswa.indo@gmail.com" target="_blank">tamansiswa.indo@gmail.com</a></font></div>
        <div><font color="#000000" face="tahoma, sans-serif"><br></font></div>
        <div><font color="#000000" face="tahoma, sans-serif">Taman-Siswa.com</font></div><div>
        <font color="#000000" face="tahoma, sans-serif">(Available Soon)</font>
        </div></div></div></div></div></div></div></div></div></div></div>'''

    def send_tutee_matchmaking_form_response(self, email_respondent: str, answers: list):
        sender_address = 'tamansiswa.indo'

        subject = 'Pencarian Tutor sedang diproses'
        content = self.generate_html_message(answers)
        bcc = ['moch.riskyaltaresh@gmail.com', 'nisrina.akalusyamoktika@gmail.com']
        reply_to = ['tamansiswa.indo+helpdesk@gmail.com']
        email = self.email_manager.create_email_messsage(
            subject=subject, body=content, to=[email_respondent], bcc=bcc, reply_to=reply_to)
        self.email_manager.send_message(email)

class TutorRegistrationNotificationService:

    email_manager = GmailManager()

    def generate_html_message(self, answers: list):
        return '''<div dir="ltr">Thank you for your registration as a tutor in TamanTutors by TamanSiswa.</div>
        <br><div>We are now reviewing your application and it has been a pleasure for us to read your ideas about education.
        We surely can't wait to start helping more people to enjoy their learning experience with the most dedicated tutor.</div>
        <br><div>We'll contact you as soon as possible to inform whether you're selected into interview or not.</div>
        <div></div><div><br></div><div></div><div><br></div><div>Cheers!</div><div><div><div><div><br>
        <div dir="ltr" class="gmail_signature"><div dir="ltr"><div><div dir=
        ="ltr"><font color="#6aa84f" size="6" face="tahoma, sans-serif"><b>
        Ares</b></font><div><font color="#000000" size="4" face="tahoma, sans-serif"><b>CEO &amp; Co-founder, TamanSiswa</b>
        </font></div><div><font color="#000000" size="4" face="tahoma, sans-serif"><br></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">LINE : <a href="http://line.me/ti/p/~tamansiswa" target="_blank">@tamansiswa</a></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">Instagram : <a href="https://www.instagram.com/tamansiswa_/" target="_blank">@tamansiswa_</a></font></div><div>
        <font color="#000000" face="tahoma, sans-serif">Email : <a href="mailto:tamansiswa.indo@gmail.com" target="_blank">tamansiswa.indo@gmail.com</a></font></div>
        <div><font color="#000000" face="tahoma, sans-serif"><br></font></div>
        <div><font color="#000000" face="tahoma, sans-serif">Taman-Siswa.com</font></div><div>
        <font color="#000000" face="tahoma, sans-serif">(Available Soon)</font>
        </div></div></div></div></div></div></div></div></div></div></div>'''

    def send_form_registration_feedback(self, email_respondent: str, answers: list):
        sender_address = 'tamansiswa.indo'

        subject = 'Tutor Registration is Being Processed'
        content = self.generate_html_message(answers)
        bcc = ['moch.riskyaltaresh@gmail.com', 'hnthalia@gmail.com']
        reply_to = ['tamansiswa.indo+helpdesk@gmail.com']
        email = self.email_manager.create_email_messsage(
            subject=subject, body=content, to=[email_respondent], bcc=bcc, reply_to=reply_to)
        self.email_manager.send_message(email)


