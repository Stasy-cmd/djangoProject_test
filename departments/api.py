from rest_framework import generics
from rest_framework.response import Response
from .serialize import DepartmentsSerializer
from .model import Departments


class DepartmentsCreateApi ( generics.CreateAPIView ):
    queryset = Departments.objects.all ()
    serializer_class = DepartmentsSerializer


class DepartmentsApi ( generics.ListAPIView ):
    queryset = Departments.objects.all ()
    serializer_class = DepartmentsSerializer


class DepartmentsUpdateApi ( generics.RetrieveUpdateAPIView ):
    queryset = Departments.objects.all ()
    serializer_class = DepartmentsSerializer


class DepartmentsDeleteApi ( generics.DestroyAPIView ):
    queryset = Departments.objects.all ()
    serializer_class = DepartmentsSerializer
