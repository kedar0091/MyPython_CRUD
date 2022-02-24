
from rest_framework import serializers

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    fname = serializers.CharField(max_length=100)
    lname = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)