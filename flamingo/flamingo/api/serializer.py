from django.db.models import fields
from .models import *
from rest_framework import serializers


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["value","timestamp"]
        
