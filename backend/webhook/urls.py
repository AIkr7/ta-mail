from django.urls import path
from backend.webhook.views import typeform

urlpatterns = [
    path('typeform/matchmaking/student', typeform.MatchmakingTypeformWebhook.as_view(), name='matchmaking-typeform')
]
