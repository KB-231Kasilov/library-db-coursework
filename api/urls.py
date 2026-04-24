from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, AccessViewSet, RatingViewSet, HistoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .utils.export import export_books_csv
from django.urls import path
from .utils.export import export_books_csv, export_books_json
from django.urls import path

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('access', AccessViewSet)
router.register('ratings', RatingViewSet)
router.register('history', HistoryViewSet)

urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('export/books/csv/', export_books_csv),
    path('export/books/json/', export_books_json),
]
