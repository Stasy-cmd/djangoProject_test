from rest_framework import generics
from rest_framework.response import Response
from .serialize import ClientSerializer
from .model import Client


class ClientCreateApi ( generics.CreateAPIView ):
    queryset = Client.objects.all ()
    serializer_class = ClientSerializer


class ClientApi ( generics.ListAPIView ):
    queryset = Client.objects.all ()
    serializer_class = ClientSerializer


class ClientUpdateApi ( generics.RetrieveUpdateAPIView ):
    queryset = Client.objects.all ()
    serializer_class = ClientSerializer


class ClientDeleteApi ( generics.DestroyAPIView ):
    queryset = Client.objects.all ()
    serializer_class = ClientSerializer
