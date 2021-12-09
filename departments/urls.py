from django.urls import path

from . import views
from .api import DepartmentsCreateApi, DepartmentsApi, DepartmentsUpdateApi, DepartmentsDeleteApi

urlpatterns = [
    path('api',DepartmentsApi.as_view()),
    path('api/create',DepartmentsCreateApi.as_view()),
    path('api/<int:pk>',DepartmentsUpdateApi.as_view()),
    path('api/<int:pk>/delete',DepartmentsDeleteApi.as_view()),
    path ( 'create/', views.DepartmentsCreate ),
    path ( 'list/', views.DepartmentGetAll),
    path('create/dl/', views.DepartmentLegalCreate),
    path ( 'create/lc/', views.LegalClientCreate ),

]