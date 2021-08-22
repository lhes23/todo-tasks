from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import AddTaskForm

# Create your views here.
tasks = ["far", "foo", "bar"]

def index(request):
    context = {"tasks":tasks}
    return render(request,"todo/index.html",context)

def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request,'todo/add.html',{"form":form})
    else:
        form = AddTaskForm()
        context = {"form":form}
        return render(request,'todo/add.html',context)