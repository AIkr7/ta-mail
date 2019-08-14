from django.conf import settings
from django.core.management.commands import runserver

class Command(runserver.Command):
    default_port = settings.RUNSERVER_PORT
