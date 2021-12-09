from rest_framework import serializers
from .model import Client


class ClientSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Client
        fields = ('id_client', 'phone_number', 'additional_numbers', 'additional_numbers',
                  'surname', 'name', 'middle_name',
                  'status', 'type_of_client', 'email', 'timezone', 'sex')

    def create(self, validated_data):
        return Client.objects.create ( **validated_data )

    def read(self, instance):
        return Client.objects.filter ( instance.pk )

    def update(self, instance, validated_data):
        return Client.objects.filter ( instance.pk ).update ( **validated_data )

    def delete(self, instance):
        return instance.delete ()
