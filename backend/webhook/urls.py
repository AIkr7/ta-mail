from django.urls import path
from backend.webhook.views import typeform

urlpatterns = [
    path('matchmaking-form', typeform.MatchmakingTypeformWebhook.as_view(), name='matchmaking-typeform')
]
