from django.db import models

from client.model import Client

SOCIAL_NETWORKS = [
    ("VK", "VK"),
    ("FB", "Женский"),
    ("ОК", "ОК"),
    ("Instagram", "Instagram"),
    ("Telegram", "Telegram"),
    ("WhatsApp", "WhatsApp"),
    ("Viber", "Viber"),
]


class SocialNetworks (models.Model):
    id = models.IntegerField ( primary_key=True, auto_created=True )
    id_client = models.ForeignKey ( Client, on_delete=models.CASCADE )
    name_network = models.CharField(max_length=2, choices=SOCIAL_NETWORKS, default='primary')

