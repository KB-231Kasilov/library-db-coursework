import os
import json
import datetime
import decimal

from django.core.management.base import BaseCommand
from books.models import Book
from users.models import User
from history.models import History
from ratings.models import Rating


# 🧠 универсальный JSON encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # Decimal (цены)
        if isinstance(obj, decimal.Decimal):
            return float(obj)

        # datetime (created_at и т.д.)
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return super().default(obj)


class Command(BaseCommand):
    help = "Create JSON backup of database"

    def handle(self, *args, **kwargs):
        os.makedirs("backups", exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"backups/backup_{timestamp}.json"

        data = {
            "users": list(User.objects.values()),
            "books": list(Book.objects.values()),
            "history": list(History.objects.values()),
            "ratings": list(Rating.objects.values()),
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)

        self.stdout.write(self.style.SUCCESS(f"Backup created: {file_path}"))