from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, AccessViewSet, RatingViewSet, HistoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('access', AccessViewSet)
router.register('ratings', RatingViewSet)
router.register('history', HistoryViewSet)

urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

