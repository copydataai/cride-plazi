"""Profile model"""
# Django
from django.db import models

# Models
from cride.utils.models import CRideModel
from cride.users.models import User

class Profile(CRideModel):
    """Profile model.

    """
    user = models.OneToOneField(User, models.CASCADE)

    # Profile
    biography = models.TextField(max_length=500)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
        )

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered"
        )

    def __str__(self):
        return str(self.user)
