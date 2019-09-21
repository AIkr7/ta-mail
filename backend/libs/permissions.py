from django.conf import settings
from rest_framework.permissions import BasePermission


class IsRequestHasAPIKey(BasePermission):
    message = 'Forbidden Request'

    def has_permission(self, request, view):
        user_key = request.META.get('HTTP_API_KEY')
        if user_key == settings.SECRET_KEY:
            return True
        else:
            return False
