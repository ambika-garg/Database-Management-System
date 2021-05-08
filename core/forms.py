from django import forms
from core.models import program_entre

class Program_entreform(forms.ModelForm):
    class Meta:
        model = program_entre
        fields = ['depart_name', 'program_name', 'state', 'financial_year', 'no_of_participants']
