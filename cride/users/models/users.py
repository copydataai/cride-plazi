
# Django
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator

# Models
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change
    the username field to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': "An user with that email already exists."
        }
        )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number be entered in the format: +999999999. Up to 15 digits allowed"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name',)

    is_client = models.BooleanField(
        'client',
        default=True,
        )
    is_verified = models.BooleanField(
        'verified',
        default=True,
        )

    def __str__(self):
        return self.username
