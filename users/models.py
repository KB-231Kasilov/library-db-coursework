from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('admin', 'Admin'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name="роль")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
