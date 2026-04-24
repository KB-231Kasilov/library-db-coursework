from django.db import models
from users.models import User
from books.models import Book


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")