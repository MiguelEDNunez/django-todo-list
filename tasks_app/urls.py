from django.conf.urls import url
from tasks_app import views


urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^(?P<pk>\d+)/edit/$', views.task_edit, name="task_edit"),
]
