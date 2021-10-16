from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import  path
from tab1 import views as v1
urlpatterns = [

    path('',v1.index),
    path('result',v1.starting)


]
