from django.urls import path, include
from django.urls.resolvers import URLPattern
from authapp import views

urlpatterns= [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('userdata/', views.userdata, name='userdata')
]