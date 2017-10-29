from django.conf.urls import url
from tasks_app import views


urlpatterns = [
    url(r'^$', views.tasks, name='tasks'),
]
