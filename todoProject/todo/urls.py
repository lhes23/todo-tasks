from django.urls import path
from django.urls.conf import include
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name="index"),
    path('add/',views.add,name="add"),
    path('<task_id>',views.task,name="task"),
    path('delete_task/<task_id>',views.delete_task,name="delete_task")
]
