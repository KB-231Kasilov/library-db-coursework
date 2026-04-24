from django.contrib import admin
from .models import Author, Genre, Category, Publisher, Book, BookFile

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookFile)
