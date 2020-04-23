from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PastaSerializer
from .models import Pasta

def index(request):
    return render(request, "build/index.html")

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
    GET     -   List ALL pastas.
    POST    -   Creat a pasta.
    """
    queryset = Pasta.objects.all().order_by('-date_created')
    serializer_class = PastaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PastaRetrieveUpdateView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    '''
    GET     -   Retrieves a pasta using id.
    PUT    -    Updates a pasta using id.
    '''
    queryset = Pasta.objects.all()
    serializer_class = PastaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)