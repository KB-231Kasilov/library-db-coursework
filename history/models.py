from django.db import models
from users.models import User
from books.models import Book


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)  # reading / finished
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"
