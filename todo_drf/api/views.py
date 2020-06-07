from django.shortcuts import render
from django.http import JsonResponse

#REST framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importing serializers
from .serializers import TaskSerializer

#importing models
from .models import Task
# Create your views here.
@api_view(['Get'])
def apioverview(request):
    api_urls={
    '/task-list/':'List of task',
    '/task-detail/':'Detail of task',
    }
    return Response(api_urls)
@api_view(['Get'])
def tasklist(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['Get'])
def taskdetail(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['Post'])
def taskcreate(request):
    serializer=TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response("Created successfully")

@api_view(['Post'])
def taskupdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response("Updated successfully")

@api_view(['DELETE'])
def taskdelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("Deleted successfully")

