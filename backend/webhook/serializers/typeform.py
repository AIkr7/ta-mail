from rest_framework import serializers


class TypeFormSerializer(serializers.Serializer):
    event_id = serializers.CharField()
    event_type = serializers.CharField()
    form_response = serializers.JSONField()
