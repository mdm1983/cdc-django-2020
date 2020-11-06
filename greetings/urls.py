# greetings/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    url(r'^getList/', views.greetingsList.as_view()),
    #http://localhost:8000/greetings/getList/

    url(r'^insert/', views.insert.as_view())
    #http://localhost:8000/greetings/insert?name=nome&surname=cognome
]