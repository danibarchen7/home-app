from .models import Properties
from rest_framework import serializers

class PropertiesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Properties
        fields = '__all__'