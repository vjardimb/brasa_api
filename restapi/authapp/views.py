from authapp.models import User
from django.http.response import HttpResponse
from restapi.settings import DATABASES
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.
'''class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, pk, request):
        method = self.request.method
        User = User.objects.get(pk=pk)
        if method == 'DELETE':
            if request.password == User.password:
                User.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_304_NOT_MODIFIED)'''
#import csv, sys, os, django

'''
project_dir = "/parcare/src/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'restapi.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()
'''
'''
from django.contrib.auth import authenticate
from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

file = 'usersdb.csv'

data = csv.reader(open(file), delimiter=";")
for row in data:
  if row[0] != "Number":
    # Post.id = row[0]
    Post=User()
    Post.password = row[0]
    Post.last_login = "2018-09-27 05:51:42.521991"
    Post.is_superuser = "0"
    Post.age = row[4]
    Post.first_name = row[1]
    Post.email = row[3]
    Post.is_staff = "1"
    Post.is_active = "1"
    Post.date_joined = "2018-09-27 05:14:50"
    Post.last_name=row[2]
    email=row[3]dfwegaraerghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    Post.save()'''

from django.http import JsonResponse
from csv import reader
from django.contrib.auth.models import User

def userdata(request):
    file = 'usersdb.csv'

    data = reader(open(file), delimiter=";")
    data = []
    for row in data:
        user = User()
        user.set_password(row[0])
        user.last_login = "2018-09-27 05:51:42.521991"
        user.is_superuser = "0"
        user.age = row[4]
        user.first_name = row[1]
        user.email = row[3]
        user.is_staff = "1"
        user.is_active = "1"
        user.date_joined = "2018-09-27 05:14:50"
        user.last_name=row[2]
        data.append(user)
    User.objects.bulk_create(data)
    return JsonResponse('user csv is now working', safe=False)