from rest_framework import generics
from rest_framework.response import Response
from .serialize import SocialNetworksSerializer
from .model import SocialNetworks


class SocialNetworksCreateApi ( generics.CreateAPIView ):
    queryset = SocialNetworks.objects.all ()
    serializer_class = SocialNetworksSerializer


class SocialNetworksApi ( generics.ListAPIView ):
    queryset = SocialNetworks.objects.all ()
    serializer_class = SocialNetworksSerializer


class SocialNetworksUpdateApi ( generics.RetrieveUpdateAPIView ):
    queryset = SocialNetworks.objects.all ()
    serializer_class = SocialNetworksSerializer


class SocialNetworksDeleteApi ( generics.DestroyAPIView ):
    queryset = SocialNetworks.objects.all ()
    serializer_class = SocialNetworksSerializer
