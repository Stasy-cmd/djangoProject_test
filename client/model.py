from django.core.validators import RegexValidator
from django.db import models

SEX_CHOICES = [
    ("male", "Мужской"),
    ("female", "Женский"),
    ("unknown", "Неизвестно"),
]

TYPE_CLIENT = [
    ("primary", "первичный"),
    ("repeated", "повторный"),
    ("external", "внешний"),
    ("indirect", "косвенный"),
]

STATUS = [
    ("active", "ACTIVE"),
    ("not_active", "NOT ACTIVE"),
]


class Client ( models.Model ):


    id_client_regex = RegexValidator ( regex=r'\d*(01)$',
                                       message="identification number (always ends with 01)" )

    phone_regex = RegexValidator ( regex=r'^\d{9,15}$',
                                   message="Phone number must be entered in the format: '999999999'. "
                                           "Up to 15 digits allowed." )

    id = models.IntegerField (primary_key=True, auto_created=True)
    id_client = models.IntegerField (unique=True, validators=[id_client_regex], blank=True )
    phone_number = models.IntegerField ( max_length=7, validators=[phone_regex], blank=True )
    additional_numbers = models.CharField ( max_length=255 )
    surname = models.CharField ( max_length=255 )
    name = models.CharField ( max_length=255 )
    middle_name = models.CharField ( max_length=255 )
    #date_creation = models.DateTimeField ( auto_now=True )
    #date_change = models.DateTimeField ( auto_now=False )
    #date_status_change = models.DateTimeField ( auto_now=True )
    status =  models.CharField(max_length=255, choices=STATUS, default='active')
    type_of_client = models.CharField(max_length=255, choices=TYPE_CLIENT, default='primary')
    email = models.EmailField()
    timezone = models.CharField( max_length=255 )
    sex = models.CharField(max_length=255, choices=SEX_CHOICES, default='Неизвестно')

