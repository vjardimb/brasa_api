from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework import viewsets
from .models import *

'''class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','password', 'first_name', 'last_name','age')'''

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password', 'first_name', 'last_name','age')

''' class UserViewSet (viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer'''

