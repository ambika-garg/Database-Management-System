from django import forms
from core.models import program_entre, participant_entre
from collectionfield.forms import CollectionField

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
            'address_ent_city': 'City'
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
    # email = CollectionField()
    # email = forms.EmailField(max_length=100, widget = forms.EmailInput)
    class Meta:
        model = participant_entre
        fields = '__all__'

        #updating columns
        labels = {
            'program_id' : 'Program Name',
            'participant_id_ent' : 'Serial number',
            'name_of_trainee' : 'Participant Name',
            'father_or_husband_name' : 'Father/Husband Name',
            'gender' : 'Gender',
            'date_of_birth' : 'Date of Birth',
            'idcard_entre_id_type' : 'Id Type',
            'idcard_entre_alt_id_type' : 'Alternate Id Type',
            'idcard_entre_aadhaar_ref_no' : 'Aadhar Number',
            'idcard_entre_alt_id_no' : 'Alternate Id Number',
            'mobile_entre_country_code' : 'Country Code',
            'mobile_entre_number' : 'Mobile Number',
            'category_entre' : 'Category',
            'job' : 'Job',
            'qualification' : 'Qualification',
            'project_identified' : 'Project Identified',
            'items_to_be_manufactured' : 'Items to be Manufactured',
            'place_of_unit' : 'Place of Unit',
            'self_or_bank_financed' : 'Self or Bank Finanaced',
            'own_contribution_amount' : 'Own Contribution Amount',
            'date_of_loan_release' : 'Date of Loan Release',
            'commencement_date' : 'Commencement Date',
            'no_of_persons_employed' : 'No. of persons employed',
            'email' : 'Email',
            'address_entre_location': 'Address',
            'address_entre_city' : 'City',
            'address_entre_state' : 'State',
            'project_cost_entre_CE' : 'CE',
            'project_cost_entre_WE' : 'WE',
            'project_cost_entre_total' : 'Total'
        }

    def __init__(self, *args, **kwargs):
        super(participantForm, self).__init__(*args, **kwargs)
        self.fields['program_id'].empty_label = "Select"
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
        print(Id)
        if Id == "Alternate ID":
            self.fields['idcard_entre_alt_id_type'].required = True
            self.fields['idcard_entre_alt_id_no'].required = True
            self.fields['idcard_entre_aadhaar_ref_no'].required = False
            # self.fields_required(['idcard_entre_alt_id_type', 'idcard_entre_alt_id_no'])
        elif Id == "Aadhar ID":

            self.fields['idcard_entre_alt_id_type'].required = False
            self.fields['idcard_entre_alt_id_no'].required = False
            # self.fields['idcard_entre_aadhaar_ref_no'].required = True

    def clean_email(self):
        print(self.cleaned_data['email'])