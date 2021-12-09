from django.core.validators import RegexValidator
from django.db import models

from client.model import Client
from legal_entity.model import LegalEntity


class Departments ( models.Model ):
    id_department_regex = RegexValidator ( regex=r'\d*(03)$',
                                           message="identification number (always ends with 01)" )

    id = models.IntegerField ( primary_key=True, auto_created=True )
    id_department = models.IntegerField ( unique=True, max_length=7, validators=[id_department_regex], blank=True )
    name = models.CharField ( max_length=255, blank=True )
    id_client = models.ForeignKey ( Client, on_delete=models.CASCADE )
    id_legal_entity = models.ForeignKey ( LegalEntity, on_delete=models.CASCADE )
