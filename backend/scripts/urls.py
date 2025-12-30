from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import LogoutView
from .consumers import PresenceConsumer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views.script import (
    # SCRIPT
    ScriptViewSet,

    # COMMON
    SizeViewSet,
    InstituteViewSet,

    # COVER
    CoverViewset,

    # DESCRIPTION
    DescriptionViewSet,
    SectionDescriptionViewSet,
    TextDescriptionViewSet,

    # NOTE_
    NoteViewSet,
    SectionNoteViewSet,
    TextNoteViewSet,

    # ISBN
    TypeIsbnViewSet,
    IsbnViewSet,

    # STATUS
    LabelStatusViewSet,
    SectionStatusViewSet,
    StatusViewSet,

    # SCRIPPROCESS
    ByMadeViewSet,
    SectionMadeViewSet,
    MadeViewSet,

    # FLAG
    SectionFlagViewSet,
    FlagViewSet,

    # ORDERER 
    OrdererViewSet,
    ScriptOrdererViewSet
)

router = DefaultRouter()
# SCRIPT
router.register(r"script", ScriptViewSet, basename="script")

# COMMON
router.register(r"size", SizeViewSet, basename="size")
router.register(r"institute", InstituteViewSet, basename="institute")

# COVER
router.register(r"cover", CoverViewset, basename="cover")

# DESCRIPTION
router.register(r"description", DescriptionViewSet, basename="description")
router.register(r"sectiondescription", SectionDescriptionViewSet, basename="section_description")
router.register(r"textdescription", TextDescriptionViewSet, basename="text_description")

# NOTE_
router.register(r"note", NoteViewSet, basename="note")
router.register(r"sectionnote", SectionNoteViewSet, basename="section_note")
router.register(r"textnote", TextNoteViewSet, basename="text_note")

# ISBN
router.register(r"isbn", IsbnViewSet, basename="isbn")
router.register(r"typeisbn", TypeIsbnViewSet, basename="type_isbn")

# STATUS
router.register(r"labelstatus", LabelStatusViewSet, basename="label_status")
router.register(r"sectionstatus", SectionStatusViewSet, basename="section_status")
router.register(r"status", StatusViewSet, basename="status")

# SCRIPT PROCESS
router.register(r"bymade", ByMadeViewSet, basename="by_made")
router.register(r"sectionmade", SectionMadeViewSet, basename="section_made")
router.register(r"made", MadeViewSet,basename="made")

# FLAG
router.register(r"sectionflag", SectionFlagViewSet, basename="section_flag")
router.register(r"flag", FlagViewSet, basename="flag")

# ORDERER
router.register(r"orderer", OrdererViewSet, basename="orderer")
router.register(r"scriptsorderer", ScriptOrdererViewSet, basename="scriptsorderer")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

urlpatterns += router.urls

websocket_urlpatterns = [
    re_path(r"ws/presence/$", PresenceConsumer.as_asgi()),
]