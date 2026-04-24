from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'role']
    list_filter = ['role']
    search_fields = ['full_name', 'email']