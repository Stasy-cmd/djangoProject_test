from django import forms
from crispy_forms.layout import Field
from client.model import Client
from departments.model import DepartmentsLegal, LegalClient, Departments, NumberId


class DepartmentsForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( DepartmentsForm, self ).__init__ ( *args, **kwargs )

    class Meta:
        model = Departments
        fields = ('name',)


class DepartmentsLegalForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( DepartmentsLegalForm, self ).__init__ ( *args, **kwargs )

    class Meta:
        model = DepartmentsLegal
        fields = ('id_department', 'id_legal_entity')


class LegalClientForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super ( LegalClientForm, self ).__init__ ( *args, **kwargs )
        #self.fields['id_department'] = forms.ModelChoiceField ( queryset=Departments.objects.all() )

    class Meta:
        model = LegalClient
        fields = ('id_legal', 'id_client')


class NumberIdForm ( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super (NumberIdForm, self ).__init__ ( *args, **kwargs )

    class Meta:
        model = NumberId
        fields = ('id_department', 'type_id')


