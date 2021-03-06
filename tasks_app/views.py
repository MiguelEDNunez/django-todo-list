from tasks_app.forms import NewTaskForm, EditTaskForm
from tasks_app.models import Task

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'tasks_app/index.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(author=request.user).order_by("id")
    tasks_complete = tasks.filter(complete=True).order_by("id")
    tasks_todo = tasks.filter(complete=False)

    if request.method == 'POST':
        new_form = NewTaskForm(request.POST, prefix="new")
        edit_form = EditTaskForm(request.POST, prefix="edit")
        if new_form.is_valid():
            new_task = new_form.save(commit=False)
            new_task.author = request.user
            new_form.save()
            return render(request, 'tasks_app/task_list.html', {'new_form': new_form,
                                                                # 'edit_form': edit_form,
                                                                'tasks_complete': tasks_complete,
                                                                'tasks_todo': tasks_todo})
    else:
        new_form = NewTaskForm(prefix="new")
        edit_form = EditTaskForm(prefix="edit")
    return render(request, 'tasks_app/task_list.html', {'new_form': new_form,
                                                        # 'edit_form': edit_form,
                                                        'tasks_complete': tasks_complete,
                                                        'tasks_todo': tasks_todo})


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
