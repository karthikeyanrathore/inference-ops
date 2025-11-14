from rest_framework import serializers
from django.core.exceptions import ValidationError
from mgmt.models import Organization

class OrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=90)
    website = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=3) 
    
    def validate_status(self, value):
        if value not in Organization.ORG_STATUS:
            raise ValidationError("invalid status code")
        return value