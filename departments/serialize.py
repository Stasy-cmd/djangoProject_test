from rest_framework import serializers
from .model import Departments, NumberId, DepartmentsLegal, LegalClient


class DepartmentsSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Departments
        fields = ('name')

    def create(self, validated_data):
        return Departments.objects.create ( **validated_data )

    def read(self, instance):
        return Departments.objects.filter ( instance.pk )

    def update(self, instance, validated_data):
        return Departments.objects.filter ( instance.pk ).update ( **validated_data )

    def delete(self, instance):
        return Departments.objects.filter ( instance.pk ).delete ()


class NumberIdSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = NumberId

class LegalClientSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = LegalClient

class DepartmentsLegalSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = DepartmentsLegal
