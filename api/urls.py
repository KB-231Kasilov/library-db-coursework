from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    BookViewSet, UserViewSet, AccessViewSet, RatingViewSet, HistoryViewSet,
    AuthorViewSet, GenreViewSet, CategoryViewSet, PublisherViewSet, BookFileViewSet
)
from .utils.export import export_books_csv, export_books_json

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('publishers', PublisherViewSet)
router.register('book-files', BookFileViewSet)
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