from django import forms
from tasks_app.models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)
        # fields = '__all__'
        # fields = ('name', 'complete',)


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('complete',)
