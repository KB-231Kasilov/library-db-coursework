from django.db import models
from users.models import User
from books.models import Book


class Access(models.Model):
    TYPE_CHOICES = [
        ('temporary', 'временный'),
        ('permanent', 'бессрочный'),
    ]

    STATUS_CHOICES = [
        ('active', 'активен'),
        ('inactive', 'неактивен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="тип_доступа")
    start_date = models.DateField(verbose_name="дата_начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="дата_окончания")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="статус")

    def __str__(self):
        return f"{self.user.full_name} - {self.book.title} - {self.status}"

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"