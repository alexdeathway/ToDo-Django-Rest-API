from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apioverview(request):
    return JsonResponse("Api Catch endpoint",safe=False)