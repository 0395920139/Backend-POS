from django.http import HttpResponse
from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from rest_framework




# Register API
# class RegisterAPI(generics.GenericAPIView):


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# #login

class LoginAPIView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data) # check username và password
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)

# #login
# list user

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes =(permissions.AllowAny)
    queryset = User.objects.all()
    serializer_class = UserSerializer


# list user




# class CheckUser(View):
    
#     def check_email(self , request):
#         if me
#         query_email = User.objects.filter()





        
        


