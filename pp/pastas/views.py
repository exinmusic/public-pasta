from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters as drfilters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import CharFilter, MultipleChoiceFilter, FilterSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .serializers import PastaSerializer
from .models import Pasta, CATEGORIES
import json

# MAIN
@ensure_csrf_cookie
def index(request):
    return render(request, "build/index.html")

# PASTA
class PastaViewSet(viewsets.ModelViewSet):
    """
    GET     -   List ALL pastas.
    POST    -   Create a pasta.
    PUT     -   Update pasta.
    """
    search_fields = ['name', 'text']
    filterset_fields = {'safe':['exact'], 'verified':['exact'], 'sentiment':['exact'], 'categories':['contains']}
    filter_backends = [DjangoFilterBackend, drfilters.SearchFilter]
    queryset = Pasta.objects.all().order_by('-date_created')
    serializer_class = PastaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PastaPublicSubmit(APIView):
    """
    POST    -   Create a pasta without privilage.

    PARAMETERS: 'name' 'text'
    """
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        payload = request.data
        Pasta.objects.create(name=payload['name'],text=payload['text'])
        return Response({"message":"Unreviewed pure Public Pasta! Fresh from the microwave..."})

# USER

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
    return HttpResponse("User logged out.")

def user_status(request):
    """
    Returns user status
    """
    if request.user.is_authenticated:
        token = Token.objects.get_or_create(user=request.user)
        return JsonResponse({"authenticated" : True, 
                            "username" : request.user.username, 
                            "token" : token[0].key})
    else:
        return JsonResponse({"authenticated":False})