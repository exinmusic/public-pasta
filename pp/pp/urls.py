from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pastas import views

router = routers.DefaultRouter()
router.register(r'pastas', views.PastaViewSet)

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user/', views.user_status),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
