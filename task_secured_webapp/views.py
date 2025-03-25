from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskCategory, ActualTask
from .forms import TaskFormCreate

# Home Page
def home(request):
    return HttpResponse("Welcome to the Task management webapp!")  


def show_all_task(request):
    all_tasks = ActualTask.objects.all()
    print(f"Fetched tasks: {all_tasks.count()} tasks")
    return render(request, 'tasks/task_list.html', {'tasks': all_tasks})  

def specific_task_detail(request, task_id):
    task = get_object_or_404(ActualTask, id=task_id)
    # task.if_expired(); 
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_creation(request):
    if request.method == 'POST':
        form = TaskFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskFormCreate() 

    return render(request, 'tasks/task_create.html', {'form': form})


def task_category_list(request):
    task_categories = TaskCategory.objects.all()
    print(f"Categories fetched: {task_categories.count()}") 
    return render(request, 'tasks/category_list.html', {'categories': task_categories})

def category_based_tasks(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    tasks = ActualTask.objects.filter(task_category=category)   

    for task in tasks:
        print(f"Task ID: {task.id}, Title: {task.task_title}")  
    return render(request, 'tasks/category_tasks.html', {'category': category, 'tasks': tasks})
