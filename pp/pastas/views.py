from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PastaSerializer
from .models import Pasta

def basic_auth(request):
    """
    Basic Auth.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

class PastaViewSet(viewsets.ModelViewSet):
    """
    List ALL pastas.
    """
    queryset = Pasta.objects.all().order_by('-date_created')
    serializer_class = PastaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

