from django import forms
from core.models import program_entre, participant_entre


class program_entreform(forms.ModelForm):
    class Meta:
        model = program_entre
        fields = '__all__'

        # updating value of columns
        labels = {
            'program_name_ent': 'Program Name',
            'depart_name_ent': 'Department Name',
            'state_ent': 'State',
            'financial_year_ent': 'Financial Year',
            'college_name_ent': 'College Name',
            'no_of_participants_ent': 'Total Participants',
            'address_ent_location': 'Location',
            ' address_ent_city': 'City'

        }

    def __init__(self, *args, **kwargs):
        super(program_entreform, self).__init__(*args, **kwargs)
        self.fields['depart_name_ent'].empty_label = "Select" #empty label pr select aajayega
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})


class participantForm(forms.ModelForm):
    class Meta:
        model = participant_entre
        fields = '__all__'

        #updating columns
        labels = {
            'participant_id_ent' : 'Serial number',
            'program_id' : 'Program Name',
            'name_of_trainee' : 'Participant Name',
            'idcard_entre_id_type' : 'Id_type',
            'idcard_entre_alt_id_type' : 'Alternate Id type',
            'idcard_entre_aadhaar_ref_no' : 'Aadhar Number',
            'idcard_entre_alt_id_no' : 'Alternate Id Number',
            'mobile_entre_country_code' : 'Country Code',
            'mobile_entre_mobile_number' : 'Mobile Number',
            'category_entre' : 'Category',
            'address_entre_location': 'Address',
            'address_entre_city' : 'City',
            'address_entre_state' : 'State'
        }
    def __init__(self, *args, **kwargs):
        super(participantForm, self).__init__(*args, **kwargs)
        self.fields['program_id'].empty_label = "Select"
        print("hello")
        self.fields['gender'].empty_label = "(Select here)"
        self.fields['idcard_entre_id_type'].empty_label = "Select"
        self.fields['idcard_entre_alt_id_type'].empty_label = "Select"
        self.fields['category_entre'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})



    def fields_required(self, fields):
        """Used for conditionally marking fields as required."""
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

    def clean(self):
        Id = self.cleaned_data.get('idcard_entre_id_type')
        print("Id")
        if Id == "Alternate ID":
            self.fields_required(['idcard_entre_alt_id_type', 'idcard_entre_alt_id_no'])
        elif Id == "Aadhar ID":
            self.fields_required(['idcard_entre_aadhaar_ref_no'])