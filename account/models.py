"""Contains model classes
"""


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
    

class User(AbstractBaseUser, PermissionsMixin):
    """User model
    """

    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def get_full_name(self):
        """get full name of User
        """
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        """user token
        """
        refresh_token = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token)   
        }

    def record_login(self):
        """Record user login with additional logic
        """

        now = timezone.now()
        self.last_login = now
        self.save(update_fields=['last_login'])
