from django.urls import path, include
from rest_framework import routers
from .views import CompanySearchView, CompanyViewSet

router = routers.DefaultRouter()
router.register("", CompanyViewSet)

urlpatterns = [
    path("search/", CompanySearchView.as_view(), name="company_search"),
    path("", include(router.urls)),
]
