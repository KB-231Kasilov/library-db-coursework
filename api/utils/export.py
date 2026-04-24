import csv
from django.http import HttpResponse
from books.models import Book
from django.http import JsonResponse
from books.models import Book


def export_books_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Title', 'Author'])

    for book in Book.objects.all():
        writer.writerow([book.id, book.title, book.author])

    return response

def export_books_json(request):
    data = list(Book.objects.values('id', 'title', 'author'))
    return JsonResponse(data, safe=False)