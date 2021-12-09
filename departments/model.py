from django.core.validators import RegexValidator
from django.db import models

from client.model import Client
from legal_entity.model import LegalEntity

TYPE_ID = [
    ("client", "01"),
    ("legal_entity", "02"),
    ("departments", "03"),
]

class Departments ( models.Model ):

    id = models.IntegerField ( primary_key=True, auto_created=True )
    name = models.CharField ( max_length=255, blank=True )


class DepartmentsLegal ( models.Model ):
    id = models.IntegerField ( primary_key=True, auto_created=True )

    id_department = models.ForeignKey ( Departments, on_delete=models.CASCADE, db_index=False )
    id_legal_entity = models.ForeignKey ( LegalEntity, on_delete=models.CASCADE, db_index=False )


class LegalClient ( models.Model ):
    id = models.IntegerField ( primary_key=True, auto_created=True )

    id_legal = models.ForeignKey ( LegalEntity, on_delete=models.CASCADE, db_index=False )
    id_client = models.ForeignKey ( Client, on_delete=models.CASCADE, db_index=False )


class NumberId(models.Model):
    type_id = models.IntegerField ()

    id = models.IntegerField ( primary_key=True, auto_created=True )
    id_department = models.IntegerField ()
    type_id =  models.CharField(max_length=255, choices=TYPE_ID, default='active')



