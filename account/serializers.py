from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    """user registration serializer
    """

    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True},
            'confirm_password': {'required': True},
        }


    def validate(self, attrs):
        """check if password and confirm password matches
        """
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request")
        
        password = attrs.get("password", '')
        confirm_password = attrs.get("confirm_password", "")
        if password != confirm_password:
            raise serializers.ValidationError("passwords do not match")
        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data["email"],
            password = validated_data.get("password"),
            first_name = validated_data.get("first_name"),
            last_name = validated_data.get("last_name")
        )
        return user
    
class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["otp", "email"]
        extra_kwargs = {
            'otp': {'required': True},
            'email': {'required': True}
        }
    
    def validate(self, data):
        allowed_fields = set(self.fields.keys())

        # Check for any additional fields
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request")
        return data
    

class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["email"]
        extra_kwargs = {
            'email': {'required': True}
        }

    def validate(self, data):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request")
        return data

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'access_token', 'refresh_token']
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }

    def validate(self, attrs):
        allowed_fields = set(['email', 'password'])
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request")
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request=request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials")
        if not user.is_verified:
            raise AuthenticationFailed("Email not verified")
        token = user.tokens()

        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'access_token': token.get('access'), 
            'refresh_token': token.get('refresh')
        }

