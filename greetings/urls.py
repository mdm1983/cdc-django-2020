# greetings/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    url(r'^getList/', views.greetingsList.as_view()),
    #http://localhost:8000/greetings/getList/

    url(r'^insert/', views.insert.as_view()),
    #http://localhost:8000/greetings/insert?email=

    url(r'^login/', views.Login.as_view(), name='login'),
    #http://localhost:8000/greetings/login/

    url(r'^register/', views.Register.as_view(), name='register')
    #http://localhost:8000/greetings/register/

]