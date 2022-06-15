from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    photo = models.ImageField(
        upload_to='user_photo',
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=15,
        choices=GENDER_CHOICE,
    )
    birthdate = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.username)
