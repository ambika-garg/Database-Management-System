from django import forms
from core.models import program_entre

class Program_entreform(forms.ModelForm):
    class Meta:
        model = program_entre
        fields = ['program_name','depart_name', 'state', 'financial_year', 'no_of_participants']

        #updating value of columns
        labels = {
            'program_name':'Program Name',
            'depart_name':'Department Name',
            'state':'State',
            'financial_year':'Financial Year',
            'no_of_participants':'Participants'

        }
