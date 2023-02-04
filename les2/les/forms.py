from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'
    value = datetime.now()


class AddLocalityType(forms.ModelForm):
    class Meta:
        model = LocalityType
        fields = '__all__'


class AddOrganization(forms.ModelForm):
    prefix = 'organization'
    class Meta:
        model = Organization
        fields = ['title', ]


class AddPersonPassport(forms.ModelForm):
    prefix = 'person_passport'

    class Meta:
        model = PersonPassport
        fields = ['series', 'number', 'date_of_issue', 'issued', 'address_birth', 'inn']
        labels = {'series': 'person_series', 'number': 'person_number'}
        widgets = {'date_of_issue': MyDateInput, }


class AddRepresentativePassport(forms.ModelForm):
    prefix = 'representative_passport'

    class Meta:
        model = RepresentativePassport
        fields = ['series', 'number', 'date_of_issue', 'issued', 'address_birth', 'inn']
        widgets = {'date_of_issue': MyDateInput, }


class AddPersonResidenceAddress(forms.ModelForm):
    prefix = 'person_residence_address'

    class Meta:
        model = PersonResidenceAddress
        fields = '__all__'


class AddRepresentativeResidenceAddress(forms.ModelForm):
    prefix = 'representative_residence_address'

    class Meta:
        model = RepresentativeResidenceAddress
        fields = '__all__'


class AddPerson(forms.ModelForm):
    prefix = 'person'

    class Meta:
        model = Person
        fields = '__all__'
        """fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number',
                  'there_is_a_representative']"""
        widgets = {
            'date_of_bird': MyDateInput,
        }


class AddRepresentativePerson(forms.ModelForm):
    prefix = 'representative'

    class Meta:
        model = RepresentativePerson
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number']
        widgets = {
            'date_of_bird': MyDateInput,
        }


class AddStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'quantity', 'date']
        widgets = {
            'date': MyDateInput,
        }


class ModStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'date', 'quantity', ]
        widgets = {
            'date': MyDateInput,
        }


class AddHeatedPromise(forms.ModelForm):
    class Meta:
        model = HeatedPremise
        fields = '__all__'


class AddContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number_decree', 'date_decree', 'number', 'date',
                  'the_end_date_of_the_export_of_wood', 'end_date_of_wood_harvesting']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput, 'end_date_of_wood_harvesting': MyDateInput,
            'the_end_date_of_the_export_of_wood': MyDateInput,
        }


class ModContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number_decree', 'date_decree', 'number', 'date',
                  'the_end_date_of_the_export_of_wood', 'end_date_of_wood_harvesting', 'plot']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput, 'the_end_date_of_the_export_of_wood': MyDateInput,
            'end_date_of_wood_harvesting': MyDateInput
        }
