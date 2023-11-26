from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from .models import Network

from .serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """
    Набор представлений CRUD для модели поставщика.
    """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']
