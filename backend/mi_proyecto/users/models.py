from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Puedes añadir campos adicionales
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_driver = models.BooleanField(default=False)
