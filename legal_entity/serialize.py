from rest_framework import serializers
from .model import LegalEntity


class LegalEntitySerializer ( serializers.ModelSerializer ):
    class Meta:
        model = LegalEntity
        fields = ('id_client', 'name_short', 'name_full', 'inn', 'kpp')

    def create(self, validated_data):
        return LegalEntity.objects.create ( **validated_data )

    def read(self, instance):
        return instance.filter ( instance.pk )

    def update(self, instance, validated_data):
        return LegalEntity.objects.filter ( instance.pk ).update ( **validated_data )

    def delete(self, instance):
        return instance.delete()
