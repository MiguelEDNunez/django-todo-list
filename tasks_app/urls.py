from django.conf.urls import url
from tasks_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', views.task_edit, name="task_edit"),
]
