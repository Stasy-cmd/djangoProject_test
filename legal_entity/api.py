from rest_framework import generics
from rest_framework.response import Response
from .serialize import LegalEntitySerializer
from .model import LegalEntity


class LegalEntityCreateApi ( generics.CreateAPIView ):
    queryset = LegalEntity.objects.all ()
    serializer_class = LegalEntitySerializer


class LegalEntityApi ( generics.ListAPIView ):
    queryset = LegalEntity.objects.all ()
    serializer_class = LegalEntitySerializer


class LegalEntityUpdateApi ( generics.RetrieveUpdateAPIView ):
    queryset = LegalEntity.objects.all ()
    serializer_class = LegalEntitySerializer


class LegalEntityDeleteApi ( generics.DestroyAPIView ):
    queryset = LegalEntity.objects.all ()
    serializer_class = LegalEntitySerializer
