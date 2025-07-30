from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from .tasks import notify

def home(request):
    tasks = Task.objects.all()
    return render(request, 'interview_02/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            res = notify.delay(form.data)
            print(res)
            return redirect('interview_02:home')
    else:
        form = TaskForm()
    return render(request, 'interview_02/addTask.html', {'form':form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('interview_02:home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'interview_02/addTask.html', {'form':form, 'action':'edit'})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('interview_02:home')
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer