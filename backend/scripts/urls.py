from django.urls import path
from .views.scripts import ScriptsView
from .views.purpose import PurposeCreateView, PurposeByCodeView, PurposeUpdateView, PurposeAllView
from .views.size import SizeCreatedView, SizeAllView, SizeUpdateView
from .views.orderer import OrdererAllView, OrdererCreatedView, OrdererUpdateView
from .views.institute import InstituteAllView, InstituteCreatedView, InstituteUpdateView
from .views.logout import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.script_orderer import ScriptOrdererCreateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
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

    path("script-orderer/create/", ScriptOrdererCreateView.as_view(), name="script-orderer-create"),
]