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
from .views.common.section import SectionViewSet
from .views.common.part import PartViewSet
from .views.common.orderer import OrdererViewSet
from .views.common.notepart import NotePartViewSet
from .views.common.label import LabelViewSet
from .views.common.institute import InstituteViewSet
from .views.common.descriptionpart import DescriptionPartViewSet
from .views.common.code import CodeViewSet

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
router.register(
    r"section",
    SectionViewSet,
    basename="section"
)
router.register(
    r"part",
    PartViewSet,
    basename="part"
)
router.register(
    r"orderer",
    OrdererViewSet,
    basename="orderer"
)
router.register(
    r"notepart",
    NotePartViewSet,
    basename="notepart"
)
router.register(
    r"label",
    LabelViewSet,
    basename="label"
)
router.register(
    r"institute",
    InstituteViewSet,
    basename="institute"
)
router.register(
    r"descriptionpart",
    DescriptionPartViewSet,
    basename="descriptionpart"
)
router.register(
    r"code",
    CodeViewSet,
    basename="code"
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