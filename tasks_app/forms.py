from django import forms
from tasks_app.models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
