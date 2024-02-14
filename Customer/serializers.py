from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Customers


# from .models import Customers
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['username']



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customers.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customers
        fields = ('id','username', 'email', 'phone','user_type','password', 'password2',
                   'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'duration': {'required': False},
            'holiday': {'required': False},
            'longitude': {'required': False},
            'laditude': {'required': False},

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = Customers.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_type = validated_data['user_type']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user