from django.contrib import admin
from .models import Author, Genre, Category, Publisher, Book, BookFile

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Publisher)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'category', 'publisher', 'price']
    list_filter = ['author', 'genre', 'category', 'publisher']
    search_fields = ['title']

@admin.register(BookFile)
class BookFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'format', 'size']