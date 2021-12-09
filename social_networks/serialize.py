from rest_framework import serializers
from .model import SocialNetworks


class SocialNetworksSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = SocialNetworks
        fields = 'social_networks'

    def create(self, validated_data):
        return SocialNetworksSerializer.objects.create ( **validated_data )

    def read(self, instance):
        return SocialNetworksSerializer.objects.filter ( instance.pk )

    def update(self, instance, validated_data):
        return SocialNetworksSerializer.objects.filter ( instance.pk ).update ( **validated_data )

    def delete(self, instance):
        return SocialNetworksSerializer.objects.filter ( instance.pk ).delete ()
