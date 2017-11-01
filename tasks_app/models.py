from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='User', null=True)

    def __str__(self):
        return self.name
