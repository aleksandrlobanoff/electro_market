from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import RetailNetworkConfig
from .views import NetworkViewSet

router = DefaultRouter()
router.register(r'networks', NetworkViewSet, basename='network')

app_name = RetailNetworkConfig.name

urlpatterns = [
    path('api/', include(router.urls)),

]