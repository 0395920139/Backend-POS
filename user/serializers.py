from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.serializers import ModelSerializar





# user serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','username','first_name','last_name')

#Register Serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','username', 'password','first_name','last_name','is_active',
                    'is_staff','is_superuser','date_joined','receive_newsletter','birth_date','address',
                    'about_me','profile_image')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        first_name = validated_data['first_name']
        is_active = validated_data['is_active']
        is_staff = validated_data['is_staff']
        is_superuser = validated_data['is_superuser']
        date_joined = validated_data['date_joined']
        receive_newsletter = validated_data['receive_newsletter']
        birth_date = validated_data['birth_date']
        address = validated_data['address']
        about_me = validated_data['about_me']
        profile_image = validated_data['profile_image']

        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],first_name,
                                        is_active,is_staff,is_superuser,date_joined,receive_newsletter,birth_date,address,about_me,profile_image)    
        return user
