from django.urls import path
from backend.webhook.views import typeform
from backend.webhook.views import googleform

urlpatterns = [
    path('typeform/matchmaking/student', typeform.MatchmakingTypeformWebhook.as_view(),
         name='typeform-matchmaking-student'),
    path('googleform/tutor/registration', googleform.TutorRegistrationWebhook.as_view(),
         name='googleform-tutor-registration'),
]
