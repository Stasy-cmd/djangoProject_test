from django.urls import path
from .api import SocialNetworksCreateApi, SocialNetworksApi, SocialNetworksUpdateApi, SocialNetworksDeleteApi

urlpatterns = [
    path('api',SocialNetworksApi.as_view()),
    path('api/create',SocialNetworksCreateApi.as_view()),
    path('api/<int:pk>',SocialNetworksUpdateApi.as_view()),
    path('api/<int:pk>/delete',SocialNetworksDeleteApi.as_view()),
]