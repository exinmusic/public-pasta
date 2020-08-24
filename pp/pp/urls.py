from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pastas import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'pastas', views.PastaViewSet)

urlpatterns = [
    path('', views.index),
    path('chef/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user/', views.user_status),
    path('api/submit/', views.PastaPublicSubmit.as_view()),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi/', RedirectView.as_view(url='/static/openapi-schema', permanent=False), name='openapi-schema'),
    path('api/docs/', TemplateView.as_view(
        template_name='pastas/swagger.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('authopenapi', get_schema_view(
        title="Authorized API",
        description="API for authed users.",
        version="1.0.0"
    ), name='notopenapi-schema'),    
    path('api/authdocs/', login_required(TemplateView.as_view(
        template_name='pastas/swagger.html',
        extra_context={'schema_url':'notopenapi-schema'}
    )), name='swagger-ui')
]
