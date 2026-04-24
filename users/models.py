from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('admin', 'Admin'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
