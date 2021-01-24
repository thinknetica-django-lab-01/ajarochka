from django.urls import path
from django.contrib.flatpages import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('bootstrap/', views.bootstrap, name = 'bootstrap')
]


