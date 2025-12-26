from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import (
    LogoutView,
    ScriptsViewSet,
    SizeViewSet,
    TypeViewSet,
    SectionViewSet,
    PartViewSet,
    OrdererViewSet,
    NotePartViewSet,
    LabelViewSet,
    InstituteViewSet,
    DescriptionPartViewSet,
    CodeViewSet,
    ContentViewSet,
    CoverViewset,
    FlagViewSet,
    IsbnViewSet,
    TextViewSet,
    ByViewSet,
    DescriptionViewSet,
    NoteViewSet,
    ScriptOrdererViewSet,
    ScriptProcessViewSet,
    StatusViewSet
)

router = DefaultRouter()
router.register(r"scripts", ScriptsViewSet, basename="scripts")
router.register(r"size", SizeViewSet, basename="size")
router.register(r"type", TypeViewSet, basename="type")
router.register(r"section", SectionViewSet, basename="section")
router.register(r"part", PartViewSet, basename="part")
router.register(r"orderer", OrdererViewSet, basename="orderer")
router.register(r"notepart", NotePartViewSet, basename="notepart")
router.register(r"label", LabelViewSet, basename="label")
router.register(r"institute", InstituteViewSet, basename="institute")
router.register(r"descriptionpart", DescriptionPartViewSet, basename="descriptionpart")
router.register(r"code", CodeViewSet, basename="code")
router.register(r"content", ContentViewSet, basename="content")
router.register(r"coverbook", CoverViewset, basename="coverbook")
router.register(r"flag", FlagViewSet, basename="flag")
router.register(r"status", StatusViewSet, basename="status")
router.register(r"isbn", IsbnViewSet, basename="isbn")
router.register(r"text", TextViewSet, basename="text")
router.register(r"by", ByViewSet, basename="by")
router.register(r"description", DescriptionViewSet, basename="description")
router.register(r"note", NoteViewSet, basename="note")
router.register(r"scriptsorderer", ScriptOrdererViewSet, basename="scriptsorderer")
router.register(r"scriptsprocess", ScriptProcessViewSet,basename="scriptsprocess"
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

urlpatterns += router.urls