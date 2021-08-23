from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from .forms import AddTaskForm
from .models import Task

def index(request):
    context = {"tasks":Task.objects.all()}
    return render(request,"todo/index.html",context)

def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            new_task = Task(task=task)
            new_task.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request,'todo/add.html',{"form":form})
    else:
        form = AddTaskForm()
        context = {"form":form}
        return render(request,'todo/add.html',context)

def task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "todo/task.html",{"task":task})

def delete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todo:index')