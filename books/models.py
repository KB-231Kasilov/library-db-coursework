from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="автор")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="жанр")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="издательство")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookFile(models.Model):
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('epub', 'EPUB'),
        ('docx', 'DOCX'),
    ]

    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name='file',
        verbose_name="книга"
    )
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, verbose_name="формат")
    size = models.IntegerField(verbose_name="размер")  # размер в байтах
    path_to_file = models.FileField(upload_to='books/', verbose_name="путь_к_файлу")

    def __str__(self):
        return f"{self.book.title} - {self.format}"

    class Meta:
        verbose_name = "Файл книги"
        verbose_name_plural = "Файлы книг"
