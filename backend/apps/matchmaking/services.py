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
            raise Exception('No Customer Email Definition Found')

        customer_email_field_id = customer_email_def.get('id')
        for ans in answers:
            if ans.get('field').get('id') == customer_email_field_id:
                # people may forget to set type to email field
                return ans.get('email', ans.get('text'))

        raise Exception('No Customer Email Found')

    def _tmp_generate_html(self, answers, definition):
        return '<html><h1>Test Template</h1></html>'

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
