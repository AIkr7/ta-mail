import hmac
import hashlib
import base64

from django.conf import settings
from rest_framework.permissions import BasePermission


class TypeformSignaturePermission(BasePermission):

    def has_permission(self, request, view):
        secret = settings.TYPEFORM_WEBHOOK_SECRET
        received_typeform_signature = request.META.get('HTTP_TYPEFORM_SIGNATURE', '')
        dig = hmac.new(secret, msg=request.body, digestmod=hashlib.sha256).digest()
        actual_signature = f'sha256={base64.b64encode(dig).decode()}'
        return actual_signature == received_typeform_signature
