from django.urls import path, re_path

from . import views
from .api import LegalEntityCreateApi, LegalEntityApi, LegalEntityUpdateApi, LegalEntityDeleteApi

urlpatterns = [
    path('api',LegalEntityApi.as_view()),
    path('api/create',LegalEntityCreateApi.as_view()),
    path('api/<int:pk>',LegalEntityUpdateApi.as_view()),
    path('api/<int:pk>/delete',LegalEntityDeleteApi.as_view()),
    path('list/', views.LegalEntityGetAll, name='all_legal_entity'),
    path('create/', views.LegalEntityCreate, name='legal_entity_page_create'),
    path('update/<int:pk>/', views.LegalEntityUpdate, name='legal_entity_page_update'),
    path('delete/<int:pk>/', views.LegalEntityDelete, name='legal_entity_page_delete'),
]