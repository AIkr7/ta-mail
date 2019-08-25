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


class TutorRegistrationNotificationService:

    email_manager = GmailManager()

    def generate_html_message(self, answers: list):
        return '''<div dir=3D"ltr">Thank you for your registration as a tutor in TamanTutors =
by TamanSiswa.=C2=A0<div><br><div>We have reviewed your application and it&=
#39;s been a pleasure to read your ideas about education.</div><div=
></div><div><br></div><div>We surely can&#39;t wai=
t to start helping more people to enjoy their learning experience with you.=
=C2=A0</div><div><br></div><div>Cheers!</div><div><div><div><div>--=C2=A0<b=
r><div dir=3D"ltr" class=3D"gmail_signature"><div dir=3D"ltr"><div><div dir=
=3D"ltr"><font color=3D"#6aa84f" size=3D"6" face=3D"tahoma, sans-serif"><b>=
Ares</b></font><div><font color=3D"#000000" size=3D"4" face=3D"tahoma, sans=
-serif"><b>CEO &amp; Co-founder, TamanSiswa</b></font></div><div><font colo=
r=3D"#000000" size=3D"4" face=3D"tahoma, sans-serif"><br></font></div><div>=
<font color=3D"#000000" face=3D"tahoma, sans-serif">LINE : @tamansiswa</fon=
t></div><div><font color=3D"#000000" face=3D"tahoma, sans-serif">Instagram =
: @tamansiswa_</font></div><div><font color=3D"#000000" face=3D"tahoma, san=
s-serif">Email :=C2=A0<a href=3D"mailto:tamansiswa.indo@gmail.com" target=
=3D"_blank">tamansiswa.indo@gmail.com</a>=C2=A0</font></div><div><font colo=
r=3D"#000000" face=3D"tahoma, sans-serif"><br></font></div><div><font color=
=3D"#000000" face=3D"tahoma, sans-serif">Taman-Siswa.com</font></div><div><=
font color=3D"#000000" face=3D"tahoma, sans-serif">(Available Soon)</font><=
/div></div></div></div></div></div></div></div></div></div></div>'''

    def send_form_registration_feedback(self, email_respondent: str, answers: list):
        sender_address = 'tamansiswa.indo'

        subject = 'Welcome!'
        content = self.generate_html_message(answers)
        bcc = ['chef.riskyaltaresh@gmail.com']
        reply_to = ['tamansiswa.indo+helpdesk@gmail.com']
        email = self.email_manager.create_email_messsage(
            subject=subject, body=content, to=[email_respondent], bcc=bcc, reply_to=reply_to)
        self.email_manager.send_message(email)
