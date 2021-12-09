from django import forms
from crispy_forms.layout import Field
from client.model import Client


class ClientForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( ClientForm, self ).__init__ ( *args, **kwargs )

    class Meta:
        model = Client
        fields = ('phone_number', 'additional_numbers', 'additional_numbers',
                  'surname', 'name', 'middle_name',
                  'status', 'type_of_client', 'email', 'timezone', 'sex')

