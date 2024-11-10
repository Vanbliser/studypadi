"""Contains Manager classes
"""


from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """User manager class to create user
    """

    def email_validator(self, email):
        """validate email
        """
        try:
            validate_email(email)
        except ValidationError as exc:
            raise ValueError(_("Please enter a valid email address")) from exc

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """create user
        """

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError (_("an email is required"))

        if not first_name:
            raise ValueError(_("first name is required"))

        if not last_name:
            raise ValueError(_("last name is required"))


        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """Create super admin
        """

        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("user_role", 'SUP')
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("user_role") != 'SUP':
            raise ValueError(_("superuser must have a SUP role"))

        if extra_fields.get("is_verified") is not True:
            raise ValueError(_("is verified must be true for admin user"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is superuser must be true for admin user"))

        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        return user
