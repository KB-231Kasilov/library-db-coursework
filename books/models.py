from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=255)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class BookFile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    format = models.CharField(max_length=10)
    size = models.IntegerField()
    file_path = models.CharField(max_length=500)
