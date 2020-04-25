from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PastaSerializer
from .models import Pasta
import json

@ensure_csrf_cookie
def index(request):
    return render(request, "build/index.html")

def user_login(request):
    """
    Basic Auth.
    """
    payload = json.loads(request.body.decode('utf-8'))
    username = payload['username']
    password = payload['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print(f"{user} just logged on.")
        return HttpResponse(f"{user}, you're logged in.")

def user_logout(request):
    logout(request)

def user_status(request):
    """
    Returns user status
    """
    if request.user.is_authenticated:
        return JsonResponse({"authenticated" : True, "username" : request.user.username})
    else:
        return JsonResponse({"authenticated":False})

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