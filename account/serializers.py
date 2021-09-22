from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth.models import User

# from django.contrib.auth import authenticate
# from django.core import exceptions
# from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()





# user serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name')

#Register Serializers



class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password') 
        extra_kwargs = {
                        'password': {'write_only': True}
                        }
    def save(self):
        account = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],

        )
        account.set_password(self.validated_data['password'])
        account.save()
        return account

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {'password': {'write_only': True}}

# class AuthToken_Serializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={'input_type': 'password'})

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(email=email, password=password)
#             print(user)

#             if user:
#                 if not user.is_active:
#                     msg = _('User account is disabled.')
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = _('Unable to log in with provided credentials.')
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = _('Must include "email" and "password".')
#             raise exceptions.ValidationError(msg)

#         data['user'] = user
#         return data
