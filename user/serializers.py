from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.serializers import ModelSerializar




# user serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','password')

#Register Serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','username', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], first_name = validated_data['first_name'],)    
        return user
