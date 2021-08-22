from django import views
from django.db import router
from django.urls import path ,include
# from django.urls.conf import include
from . import views
from .views import LoginAPI, RegisterAPI,LoginAPI
from knox import views as knox_views
from rest_framework.routers import DefaultRouter



app_name = 'user'


router = DefaultRouter()
router.register('', views.UserViewSet )

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view() , name = "Login"),
    path('api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/user/', include(router.urls) , name='user'),
    #/api/user/ - GET 
    #/api/user/ -POST
    #/api/user/{user_id} - GET
    #/api/user/{user_id} - PUT
    #/api/user/{user_id} - DELETE


]
