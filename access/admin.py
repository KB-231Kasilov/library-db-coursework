from django.contrib import admin
from .models import Access

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'type', 'start_date', 'end_date', 'status']
    list_filter = ['type', 'status']