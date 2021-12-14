import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from model_mommy import mommy
import legal_entity.model
import client.model
import departments.model
import string
import random

def test_create_data():
    legal_entities = []
    clients = []
    departaments = []

    SEX_CHOICES = ["male","female", "unknown"]

    TYPE_CLIENT = ["primary", "repeated", "external", "indirect"]

    STATUS = ["active","not_active"]
    k = 1

    for i in range(1, 401):
        name_short  = ''.join ( random.choices ( string.ascii_letters, k = 8) )
        name_full = ''.join ( random.choices ( string.ascii_letters, k = 20 ) )
        inn = random.randint ( 100000000000001, 999999999999999 )
        kpp = random.randint ( 100000000, 999999999 )

        legal_entity = mommy.make('legal_entity.LegalEntity', id = i, name_short=name_short, name_full=name_full, inn=inn, kpp=kpp)
        if bool ( random.getrandbits ( 1 ) ) and len(legal_entities) < 10000:
            legal_entities.append(legal_entity)
        mommy.make('departments.NumberId',id = k, id_number = i, type_id = 1)
        k += 1
    for i in range (1, 40000 ):
        phone_number = random.randint ( 100000000, 999999999999999 )
        add_numbers = random.randint ( 100000000, 99999999999999)
        name_s  = ''.join ( random.choices ( string.ascii_letters, k = 8) )
        name = ''.join ( random.choices ( string.ascii_letters, k = 8 ) )
        name_m  = ''.join ( random.choices ( string.ascii_letters, k = 8) )
        random.shuffle(TYPE_CLIENT)
        type = TYPE_CLIENT[0]
        email = ''.join (['email', "@", 'mail', ".",  'com'])
        random.shuffle(SEX_CHOICES)
        sex = SEX_CHOICES[0]
        random.shuffle(STATUS)
        status = STATUS[0]
        client = mommy.make('client.Client', id = i, phone_number=phone_number,
                            additional_numbers= add_numbers,
                            surname=name_s, name=name, middle_name=name_m, status=status, type_of_client=type,
                            email=email, timezone="UTC+3", sex=sex)
        mommy.make('departments.NumberId',id = k, id_number = i, type_id = 2)
        k += 1
        if bool ( random.getrandbits ( 1 ) ) and len(clients) < 10000:
            clients.append(client)

    for i in range (1, 601 ):
        name_s = ''.join ( random.choices ( string.ascii_letters, k=8 ) )
        departament = mommy.make ('departments.Departments', id = i, name=name_s)
        mommy.make('departments.NumberId',id = k, id_number = i, type_id = 3)
        k += 1

        if bool ( random.getrandbits ( 1 ) ) and len ( departaments ) < 10000:
            departaments.append ( departament )

    for i in range(1, 100):
        random.shuffle ( clients )
        random.shuffle ( departaments )
        random.shuffle ( legal_entities )
        #print(departaments[0])
        mommy.make ('departments.LegalClient', id=i, id_client=clients[0], id_legal=legal_entities[0])


#test_create_data()
'''for i in range(1, 6):
    id_departament = random.randint ( 1, 601 )
    id_legal = random.randint ( 1, 401)
    mommy.make ('departments.DepartmentsLegal', id=i, id_departament=id_departament, id_legal=id_legal)'''


k= 1
for i in range(1, 401):
    mommy.make ( 'departments.NumberId', id=k, id_number=i, type_id=1 )
    k += 1
for i in range(1, 40000 ):
    mommy.make ( 'departments.NumberId', id=k, id_number=i, type_id=2 )
    k += 1

for i in range(1, 601 ):
    mommy.make ( 'departments.NumberId', id=k, id_number=i, type_id=3 )
    k += 1