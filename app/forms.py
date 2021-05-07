from django import forms
from app.models import prog_entre

class Program_entreform(forms.ModelForm):
    class Meta:
        model = prog_entre
        fields = "__all__"
