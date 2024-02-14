from rest_framework import serializers
from .models import Tipe

class TipeSerializer(serializers.ModelSerializer):
     class Meta:
        model = Tipe
        fields = ['tipe']
