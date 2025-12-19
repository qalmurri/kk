from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views.logout import LogoutView
from .views.scripts import ScriptsViewSet

router = DefaultRouter()
router.register("scripts", ScriptsViewSet, basename="scripts")

urlpatterns = [
    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='auth_logout'
    ),

]

urlpatterns += router.urls