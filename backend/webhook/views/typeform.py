from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from backend.apps.matchmaking.services import MatchmakingNotificationService
from backend.webhook.permissions import TypeformSignaturePermission
from backend.webhook.serializers.typeform import TypeFormSerializer


class MatchmakingTypeformWebhook(APIView):
    authentication_classes = ()
    permission_classes = (TypeformSignaturePermission,)

    def post(self, request, *args, **kwargs):
        serializer = TypeFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        if data.get('event_type') == 'form_response':
            MatchmakingNotificationService().send_response_for_tutor_request(
                data.get('form_response'))
        return Response(data="OK", status=status.HTTP_200_OK)
