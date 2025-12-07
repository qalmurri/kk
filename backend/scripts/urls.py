from django.urls import path
from .views.scripts import ScriptsView
from .views.authentification import LoginView
from .views.purpose import PurposeCreateView, PurposeByCodeView, PurposeUpdateView, PurposeAllView
from .views.size import SizeCreatedView, SizeAllView, SizeUpdateView
from .views.orderer import OrdererAllView, OrdererCreatedView, OrdererUpdateView
from .views.institute import InstituteAllView, InstituteCreatedView, InstituteUpdateView


urlpatterns = [
    path("login/", LoginView.as_view()), #done
    path("scripts/", ScriptsView.as_view()),
    path("purpose/", PurposeCreateView.as_view()), #done
    path("purpose/all/", PurposeAllView.as_view()), #done
    path("purpose/<int:code>/", PurposeByCodeView.as_view()), #done
    path("purpose/<int:id>/update/", PurposeUpdateView.as_view()), #done
    path("size/", SizeCreatedView.as_view()), #done
    path("size/all/", SizeAllView.as_view()), #done
    path("size/<int:id>/update/", SizeUpdateView.as_view()), #done
    path("orderer/", OrdererCreatedView.as_view()), #done
    path("orderer/all/", OrdererAllView.as_view()), #done
    path("orderer/<int:id>/update/", OrdererUpdateView.as_view()), #done
    path("institute/", InstituteCreatedView.as_view()), #done
    path("institute/all/", InstituteAllView.as_view()), #done
    path("institute/<int:id>/update/", InstituteUpdateView.as_view()), #done
]