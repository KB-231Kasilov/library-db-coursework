from django.db import models
from users.models import User
from books.models import Book


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")

    def __str__(self):
        return f"{self.user.full_name} - {self.book.title}"

    class Meta:
        verbose_name = "История книг"
        verbose_name_plural = "История книг"
        unique_together = ['user', 'book']  # чтобы не дублировать
