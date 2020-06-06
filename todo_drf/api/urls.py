
from django.contrib import admin
from django.urls import path
from .views import apioverview
#path of api endpoints
urlpatterns = [
    path('',apioverview,name="API Catch"),
   
]