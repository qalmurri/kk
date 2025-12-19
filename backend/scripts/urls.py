from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views.logout import LogoutView
from .views.scripts import ScriptsView
from .views.status import (
    StatusCreateView,
    StatusByCodeView,
    StatusUpdateView,
    StatusAllView
)
from .views.size import (
    SizeCreatedView,
    SizeAllView,
    SizeUpdateView
)
from .views.orderer import (
    OrdererAllView,
    OrdererCreatedView,
    OrdererUpdateView
)
from .views.institute import (
    InstituteAllView,
    InstituteCreatedView,
    InstituteUpdateView
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
    path(
        "scripts/",
        ScriptsView.as_view()
    ),
    path(
        "purpose/",
        StatusCreateView.as_view()
    ),
    path(
        "purpose/all/",
        StatusAllView.as_view()
    ),
    path(
        "purpose/<int:code>/",
        StatusByCodeView.as_view()
    ),
    path(
        "purpose/<int:id>/update/",
        StatusUpdateView.as_view()
    ),
    path(
        "size/",
        SizeCreatedView.as_view()
    ), 
    path(
        "size/all/",
        SizeAllView.as_view()
    ), 
    path(
        "size/<int:id>/update/",
        SizeUpdateView.as_view()
    ),
    path(
        "orderer/",
        OrdererCreatedView.as_view()
    ),
    path(
        "orderer/all/",
        OrdererAllView.as_view()
    ),
    path(
        "orderer/<int:id>/update/",
        OrdererUpdateView.as_view()
    ),
    path(
        "institute/",
        InstituteCreatedView.as_view()
    ),
    path(
        "institute/all/",
        InstituteAllView.as_view()
    ),
    path(
        "institute/<int:id>/update/",
        InstituteUpdateView.as_view()
    ),
]