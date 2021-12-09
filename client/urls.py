from django.template.defaulttags import url
from django.urls import path, re_path
from . import views
from .api import ClientCreateApi, ClientApi, ClientUpdateApi, ClientDeleteApi

urlpatterns = [
    path('api',ClientApi.as_view()),
    path('api/create',ClientCreateApi.as_view()),
    path('api/<int:pk>',ClientUpdateApi.as_view()),
    path('api/<int:pk>/delete',ClientDeleteApi.as_view()),
    path('list/', views.ClientGetAll, name='all_client'),
    path('create/', views.ClientCreate, name='client_create'),
    path('update/<int:pk>/', views.ClientUpdate, name='client_update'),
    path('delete/<int:pk>/', views.ClientDelete, name='client_delete'),
]
