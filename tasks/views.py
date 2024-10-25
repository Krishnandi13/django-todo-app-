from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    
    tasks=Task.objects.all()
    return render(request,'index.html',{
        'tasks':tasks
        
    })

def completed(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    completed_tasks=Task.objects.filter(completed=True)
    return render(request,'completed.html',{
        'tasks':completed_tasks
    })

def remaining(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    remaining_tasks=Task.objects.filter(completed=False)
    return render(request,'remaining.html',{
        'tasks':remaining_tasks
    })

def add_task(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.method =='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        due_date=request.POST.get('due_date')
        due_time=request.POST.get('due_time')
        completed=False
        
        if title !="" and due_date !="" and due_date!="" :
            task=Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time=due_time,
                completed=completed
                
            )
            task.save()
            return redirect('home')
    else:
         return render(request,'add_task.html')
    return render(request,'add_task.html')

def delete_task(request,task_id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    task = Task.objects.get(id=task_id)
    return render(request,'delete.html',{
        "task": task
    })
   
def task_detail(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {
        "task": task
    }) 
    
def toggle_complete(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    task = Task.objects.get(id=task_id)
    if task:
        task.completed= not task.completed
        task.save()
        return redirect('home')   
          
def remove_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')   

