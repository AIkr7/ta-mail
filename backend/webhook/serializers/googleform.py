from rest_framework import serializers


class GoogleFormSerializer(serializers.Serializer):
    form_id = serializers.CharField()
    title = serializers.CharField()
    form_response = serializers.JSONField()
