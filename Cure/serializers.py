from rest_framework import serializers
from .models import Cures

class CureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cures
        fields = '__all__'
        
        