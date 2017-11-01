from django.shortcuts import get_object_or_404, redirect, render
from tasks_app.forms import NewTaskForm, EditTaskForm
from tasks_app.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'tasks_app/index.html')


@login_required
def task_list(request):
    tasks = Task.objects.order_by("id")
    if request.method == 'POST':
        new_form = NewTaskForm(request.POST, prefix="new")
        edit_form = EditTaskForm(request.POST, prefix="edit")
        if new_form.is_valid():
            new_form.save()
            return render(request, 'tasks_app/task_list.html', {'new_form': new_form, 'edit_form': edit_form,
                                                                'tasks': tasks})
    else:
        new_form = NewTaskForm(prefix="new")
        edit_form = EditTaskForm(prefix="edit")
    return render(request, 'tasks_app/task_list.html', {'new_form': new_form, 'edit_form': edit_form, 'tasks': tasks})


@login_required
def task_edit(request, pk):
    # tasks = Task.objects.order_by("id")
    # new_form = NewTaskForm()
    edit_form = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        edit_form = EditTaskForm(request.POST, instance=edit_form)
        print(request.POST)
        if edit_form.is_valid():
            task = edit_form.save(commit=False)
            task.complete = True
            task.save()
            return redirect('task_list')
    # else:
        # edit_form = EditTaskForm(instance=edit_form)
    return redirect('task_list')
