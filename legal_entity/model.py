from django.core.validators import RegexValidator
from django.db import models


class LegalEntity (models.Model):

    inn_regex = RegexValidator (regex=r'\d{15}',
                                message="KPP number must be entered in the format: '999999999999999'. "
                                           "You need to enter 15 digits" )

    kpp_regex = RegexValidator ( regex=r'\d{9}',
                                 message="KPP number must be entered in the format: '999999999'. "
                                         "You need to enter 9 digits" )

    id = models.IntegerField ( primary_key=True, auto_created=True )
    #id_client = models.IntegerField (unique=True, max_length=7, validators=[id_client_regex], blank=True )
    #date_creation = models.DateTimeField()
    #date_change = models.DateTimeField()
    name_short = models.CharField ( max_length=255 )
    name_full = models.TextField()
    inn = models.IntegerField (validators=[inn_regex], blank=True )
    kpp = models.IntegerField (validators=[kpp_regex], blank=True )
