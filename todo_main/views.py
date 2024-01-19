from django.shortcuts import render

from todo.models import Task


def home(request):
    # Filter is used to filter multiple data based on some condition
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    #print(tasks)
    
    # Completed tasks
    completed_tasks = Task.objects.filter(is_completed=True)
    
    context = {
        'tasks' : tasks,
    }
    return render(request, 'home.html', context)