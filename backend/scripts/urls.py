from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views.logout import LogoutView
from .views.scripts import ScriptsViewSet
from .views.common.size import SizeViewSet
from .views.common.type import TypeViewSet

router = DefaultRouter()
router.register(
    r"scripts",
    ScriptsViewSet,
    basename="scripts"
)
router.register(
    r"size",
    SizeViewSet,
    basename="size"
)
router.register(
    r"type",
    TypeViewSet,
    basename="type"
)

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