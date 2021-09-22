from django import views
from django.db import router
from django.urls import path ,include
# from django.urls.conf import include
from . import views
from .views import RegisterAPI,LoginAPIView
# from knox import views as knox_views
from rest_framework.routers import DefaultRouter



app_name = 'user'


router = DefaultRouter()
router.register('', views.UserViewSet )

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPIView.as_view() , name = "Login"),
    # path('login/', LoginAPI.as_view() , name = "Login"),
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

    # Login admin


    path('user/', include(router.urls) , name='user'),
    #/api/user/ - GET 
    #/api/user/ -POST
    #/api/user/{user_id} - GET
    #/api/user/{user_id} - PUT
    #/api/user/{user_id} - DELETE



    # Login admin


]
