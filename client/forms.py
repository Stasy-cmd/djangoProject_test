from django import forms

from client.model import Client
from legal_entity.model import LegalEntity


class ClientForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( ClientForm, self ).__init__ ( *args, **kwargs )
        # self.fields['date_creation'].widget = widgets.AdminDateWidget()
        # self.fields['date_change'].widget = widgets.AdminDateWidget()
        # self.fields['date_status_change'].widget = widgets.AdminDateWidget()

    class Meta:
        model = Client
        fields = ('id_client', 'phone_number', 'additional_numbers', 'additional_numbers',
                  'surname', 'name', 'middle_name',
                  'status', 'type_of_client', 'email', 'timezone', 'sex')
