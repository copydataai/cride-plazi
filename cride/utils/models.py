"""Django models Utilities"""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model(abstract).
      + created: DateTime
      + modified: DateTime
    """
    created = models.DateTimeField('created at', auto_now_add=True)

    modified = models.DateTimeField('modified at', auto_now=True)


    class Meta:
        abstract: bool = True
        get_latest_by: str = 'created'
        ordering: list = ['-created', '-modified']
