from django.urls import path
from django.contrib.flatpages import views
from . import views


urlpatterns += [
    path('', views.index, name='index'),
    path('about', views.flatpage, {'url': '/about/'}, name = 'about'),
    path('contacts', views.flatpage, {'url': '/contacts/', name = 'contacts'),
]


