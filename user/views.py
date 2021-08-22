from django.db.models import query
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from django.contrib.auth.models import User




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # queryset = User.objects.filter(email = request.data['email'])
        # if queryset == True :
        #     print("da ton tai")
        # else :
        #     print('chua co')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



#login

class LoginAPI(KnoxLoginView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(request.user.get_all_permissions)
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#login

# list user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# list user




# class CheckUser(View):
    
#     def check_email(self , request):
#         if me
#         query_email = User.objects.filter()





        
        


