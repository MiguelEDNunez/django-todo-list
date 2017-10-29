from django.shortcuts import render
from tasks_app.forms import NewTaskForm
from tasks_app.models import Task

# Create your views here.


def index(request):
    return render(request, 'tasks_app/index.html')


# def tasks(request):
#     task_list = Task.objects.order_by("id")
#     task_dict = {'tasks': task_list}
#     return render(request, 'tasks_app/tasks.html', context=task_dict)


def tasks(request):
    task_list = Task.objects.order_by("id")
    task_dict = {'tasks': task_list}

    form = NewTaskForm()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return tasks(request, context=task_dict)
            # return index(request)
            # return tasks(request)
            return render(request, 'tasks_app/tasks.html', {'form': form, 'tasks': task_list})
        else:
            print('ERROR FORM INVALID')

    return render(request, 'tasks_app/tasks.html', {'form': form, 'tasks': task_list})
