from django import forms

from legal_entity.model import LegalEntity


class LegalEntityForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( CreateForm, self ).__init__ ( *args, **kwargs )
        # self.fields['date_creation'].widget = widgets.AdminDateWidget()
        # self.fields['date_change'].widget = widgets.AdminDateWidget()

    class Meta:
        model = LegalEntity
        fields = ('id_client', 'name_short', 'name_full', 'inn', 'kpp')
