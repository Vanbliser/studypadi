from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import validators
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

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
            raise serializers.ValidationError("Bad request. Unknown field(s).")
        
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
            raise serializers.ValidationError("Bad request. Unknown field(s).")
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
            raise serializers.ValidationError("Bad request. Unknown field(s).")
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
            raise serializers.ValidationError("Bad request. Unknown field(s).")
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request=request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials")
        if not user.is_verified:
            raise AuthenticationFailed("Email not verified")
        token = user.tokens()
        user.record_login()
        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'access_token': token.get('access'), 
            'refresh_token': token.get('refresh')
        }

class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    base_url = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        fields = ["email", "base_url"]
        extra_kwargs = {
            'email': {'required': True},
            'base_url': {'required': True}
        }

    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request. Unknown field(s).")
        email = attrs.get("email")
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exit")
        base_url = attrs.get('base_url')
        if not validators.url(base_url):
            raise serializers.ValidationError("The base url is not a valid URL")
        return attrs

class SetNewPasswordSerializer(serializers.Serializer):
    uidBase64 = serializers.CharField(max_length=64, write_only=True)
    token = serializers.CharField(write_only=True)
    new_password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=100, min_length=6, write_only=True)

    class Meta:
        fields = ["uidBase64", "token", "new_password", "confirm_password"]
        extra_kwargs = {
            "uidBase64": {"required": True},
            "token": {"required": True},
            "new_password": {"required": True},
            "confirm_password": {"required": True}
        }
    
    def validate(self, attrs):
        allowed_fields = set(self.fields.keys())
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request. Unknown field(s).")
        
        password = attrs.get("new_password")
        password2 = attrs.get("confirm_password")
        print(password, password2)
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        
        uidBase64 = attrs.get('uidBase64')
        token = attrs.get('token')
        try:
            id = force_str(urlsafe_base64_decode(uidBase64))
            if not User.objects.filter(id=id).exists():
                raise serializers.ValidationError("User ID does not exit")
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user=user, token=token):
                raise AuthenticationFailed('Reset link has expired')
            user.set_password(password)
            user.save()
        except Exception:
            raise AuthenticationFailed('Invalid or expired link')
        
        return user

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    class Meta:
        fields = ["refresh_token"]
        extra_kwargs = {
            "refresh_token": {"required": True}
        }
    def validate(self, attrs):
        allowed_fields = set(self.fields.keys())
        extra_fields = set(self.initial_data.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError("Bad request. Unknown field(s).")
        try:
            refresh_token = attrs.get("refresh_token")
            token=RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            raise serializers.ValidationError("Bad token.")
        return attrs
