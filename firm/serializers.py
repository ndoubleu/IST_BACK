from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(default=False) 
    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_superuser = validated_data['is_superuser'],
            is_staff = True
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password","is_superuser" )