
from django.contrib import admin
from django.urls import path
from .views import (apioverview,
                    tasklist,
                    taskdetail,
                    taskcreate,
                    taskupdate,
                    taskdelete,
                    )
#path of api endpoints
urlpatterns = [
    path('',apioverview,name="API Catch"),
    path('task-list/',tasklist,name="task list"),
    path('task-detail/<int:pk>/',taskdetail,name="task detail"),
    path('task-create/',taskcreate,name="task create"),
    path('task-update/<int:pk>/',taskupdate,name="task update"),
    path('task-delete/<int:pk>/',taskdelete,name="task update"),
]