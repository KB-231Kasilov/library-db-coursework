from django.db import models
from users.models import User
from books.models import Book


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")
    value = models.IntegerField(verbose_name="значение")  # 1-5

    def __str__(self):
        return f"{self.user.full_name} - {self.book.title}: {self.value}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        unique_together = ['user', 'book']  # один пользователь - одна оценка на книгу