from rest_framework import serializers
from .model import Departments


class DepartmentsSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Departments
        fields = ('id_department', 'name', 'id_client', 'id_legal_entity')

    def create(self, validated_data):
        return Departments.objects.create ( **validated_data )

    def read(self, instance):
        return Departments.objects.filter ( instance.pk )

    def update(self, instance, validated_data):
        return Departments.objects.filter ( instance.pk ).update ( **validated_data )

    def delete(self, instance):
        return Departments.objects.filter ( instance.pk ).delete ()
