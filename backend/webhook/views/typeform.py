from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.apps.matchmaking.services import MatchmakingNotificationService
from backend.webhook.permissions import TypeformSignaturePermission


class MatchmakingTypeformWebhook(APIView):
    authentication_classes = ()
    permission_classes = (TypeformSignaturePermission,)

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('event_type') != 'form_response':
            MatchmakingNotificationService().send_response_for_tutor_request(
                data.get('form_response'))
        return Response(status=status.HTTP_200_OK)
