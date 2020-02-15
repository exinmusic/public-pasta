from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PastaSerializer
from .models import Pasta

class PastaViewSet(viewsets.ModelViewSet):
    """
    List ALL pastas.
    """
    queryset = Pasta.objects.all().order_by('-date_created')
    serializer_class = PastaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

