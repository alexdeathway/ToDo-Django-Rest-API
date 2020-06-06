from django.shortcuts import render
from django.http import JsonResponse

#REST framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importing serializers
from .serializers import TaskSerializer

# Create your views here.
@api_view(['get'])
def apioverview(request):
    api_urls={
    'list':'/task-list/',
    }
    return Response(api_urls)