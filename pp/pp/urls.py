from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pastas import views

router = routers.DefaultRouter()
router.register(r'pastas', views.PastaViewSet)

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/user/', views.user_status),
    path('api/', include(router.urls)),
    path('basic-auth/', views.basic_auth),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pastas/<pk>', views.PastaRetrieveUpdateView.as_view(), name='pasta_retrieve_update'),
]
