from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from backend.apps.matchmaking.services import TutorRegistrationNotificationService
from backend.webhook.serializers.googleform import GoogleFormSerializer


class TutorRegistrationWebhook(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = GoogleFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        email = data.get('form_response').get('email_respondent')
        answers = data.get('form_response').get('answers')
        TutorRegistrationNotificationService()\
            .send_form_registration_feedback(email, answers)
        return Response(data="OK", status=status.HTTP_200_OK)
