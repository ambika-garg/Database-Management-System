from django import forms
from core.models import participant_aware, participant_capac, program_aware, program_capac, program_entre, program_skill, participant_entre, participant_skill, placement_skill
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
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

class program_skillform(forms.ModelForm):

    class Meta:
        model = program_skill
        fields = '__all__'

        # updating value of columns
        labels = {
            'program_name_skill': 'Program Name',
            'depart_name_skill': 'Department Name',
            'state': 'State',
            'financial_Year_skill': 'Financial Year',
            'trade_skill': 'Trade',
            'no_of_participants_skill': 'Total Participants',
            'address_skill_location': 'Location',
            'address_skill_city': 'City'
        }

    def __init__(self, *args, **kwargs):
        super(program_skillform, self).__init__(*args, **kwargs)
        self.fields['depart_name_skill'].empty_label = "Select" #empty label pr select aajayega
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

        self.fields["state"].required = False
        self.fields["trade_skill"].required = False
        self.fields["address_skill_location"].required = False
        self.fields["address_skill_city"].required = False
        self.fields["no_of_participants_skill"].required = False



class program_awareform(forms.ModelForm):
    class Meta:
        model = program_aware
        fields = '__all__'

        # updating value of columns
        labels = {
            'program_name_aware': 'Program Name',
            'depart_name_aware': 'Department Name',
            'state_aware': 'State',
            'financial_year_aware': 'Financial Year',
            'no_of_participants_aware': 'Total Participants',
            'address_aware_location': 'Location',
            'address_aware_city': 'City'
        }

    def __init__(self, *args, **kwargs):
        super(program_awareform, self).__init__(*args, **kwargs)
        self.fields['depart_name_aware'].empty_label = "Select" #empty label pr select aajayega
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})


class program_capacform(forms.ModelForm):
    class Meta:
        model = program_capac
        fields = '__all__'

        # updating value of columns
        labels = {
            'program_name_capac': 'Program Name',
            'depart_name_capac': 'Department Name',
            'state_capac': 'State',
            'financial_year_capac': 'Financial Year',
            'no_of_participants_capac': 'Total Participants',
            'address_capac_location': 'Location',
            'address_capac_city': 'City'
        }

    def __init__(self, *args, **kwargs):
        super(program_capacform, self).__init__(*args, **kwargs)
        self.fields['depart_name_capac'].empty_label = "Select" #empty label pr select aajayega
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
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
            'program_id_ent' : 'Program Name',
            'participant_id_ent' : 'Serial number',
            'batchid' : 'Batch Id',
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
        self.fields['program_id_ent'].empty_label = "Select"
        self.fields['gender'].empty_label = "(Select here)"
        self.fields['idcard_entre_id_type'].empty_label = "Select"
        self.fields['idcard_entre_alt_id_type'].empty_label = "Select"
        self.fields['category_entre'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

    # def fields_required(self, fields):
    #     """Used for conditionally marking fields as required."""
    #     for field in fields:
    #         if not self.cleaned_data.get(field, ''):
    #             msg = forms.ValidationError("This field is required.")
    #             self.add_error(field, msg)

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

class participantSkillForm(forms.ModelForm):
    class Meta:
        model = participant_skill
        fields = '__all__'

        #updating columns
        labels = {
            'program_id_skill' : 'Program Name',
            'participant_id_skill' : 'Participant ID',
            'batchid' : 'Batch ID',
            'name_skill_salutation' : 'Salutation',
            'name_skill_FirstName' : 'First Name',
            'name_skill_LastName' : 'Last Name',
            'gender' : 'Gender',
            'dob' : 'Date of Birth',
            'email' : 'Email',
            'marital_status' : 'Marital Status',
            'fathers_name' : 'Father Name',
            'mothers_name' : 'Mother Name',
            'religion' : 'Religion',
            'category' : 'Category',
            'disability_input' : 'Disability Input',
            'disability_type' : 'Disability Type',
            'domicile_state' : 'Domicile State',
            'domicile_district' : 'Domicile District',
            'idcard_skill_id_type' : 'Id Type',
            'idcard_skill_alt_id_type' : 'Alternate Id Type',
            'idcard_skill_aadhaar_ref_no' : 'Aadhar Number',
            'idcard_skill_alt_id_no' : 'Alternate Id Number',
            'mobile_skill_country_code' : 'Country Code',
            'mobile_skill_primary_mobile' : 'Primary Mobile Number',
            'mobile_skill_secondary_mobile' : 'Secondary Mobile Number',
            'education_level' : 'Education Level',
            'perm_address' : 'Permanent Address',
            'perm_state' : 'Permanent Address State',
            'perm_district' : 'Permanent Address District',
            'perm_pincode' : 'Permanent Address Pincode',
            'perm_city' : 'Permanent Address City',
            'perm_tehsil' : 'Permanent Address Tehsil',
            'perm_constituency' : 'Permanent Address Constituency',
            'pa_same_as_ca' : 'Permanent Address same as Communication Address',
            'comm_address' : 'Communication Address',
            'comm_state' : 'Communication Address State',
            'comm_district' : 'Communication Address District',
            'comm_pincode' : 'Communication Address Pincode',
            'comm_city' : 'Communication Address City',
            'comm_tehsil' : 'Communication Address Tehsil',
            'comm_constituency' : 'Communication Address Constituency',
            'training_status' : 'Training Status',
            'job_details_prev_exp_sector' : 'Previous Experience Sector',
            'job_details_no_of_months' : 'No of months',
            'job_details_employed' : 'Employed',
            'job_details_employment_status' : 'Employment Status',
            'job_details_employment_details' : 'Employment Details',
            'heard_about_us' : 'Heard About Us'
        }

    def __init__(self, *args, **kwargs):
        super(participantSkillForm, self).__init__(*args, **kwargs)
        self.fields['program_id_skill'].empty_label = "Select"
        self.fields['gender'].empty_label = "(Select here)"
        self.fields['idcard_skill_id_type'].empty_label = "Select"
        self.fields['idcard_skill_alt_id_type'].empty_label = "Select"
        self.fields['category'].empty_label = "Select"
        self.fields['marital_status'].empty_label = "Select"
        self.fields['pa_same_as_ca'].empty_label = "Select"
        self.fields['religion'].empty_label = "Select"
        self.fields['training_status'].empty_label = "Select"
        self.fields['heard_about_us'].empty_label = "Select"
        self.fields['job_details_employed'].empty_label = "Select"
        self.fields['job_details_employment_status'].empty_label = "Select"
        self.fields['disability_input'].empty_label = "Select"
        self.fields['disability_type'].empty_label = "Select"
        self.fields['name_skill_salutation'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

    # def fields_required(self, fields):
    #     """Used for conditionally marking fields as required."""
    #     for field in fields:
    #         if not self.cleaned_data.get(field, ''):
    #             msg = forms.ValidationError("This field is required.")
    #             self.add_error(field, msg)

    def clean(self):
        Id = self.cleaned_data.get('idcard_skill_id_type')
        print(Id)
        if Id == "Alternate ID":
            self.fields['idcard_skill_alt_id_type'].required = True
            self.fields['idcard_skill_alt_id_no'].required = True
            self.fields['idcard_skill_aadhaar_ref_no'].required = False
        elif Id == "Aadhar ID":
            self.fields['idcard_skill_alt_id_type'].required = False
            self.fields['idcard_skill_alt_id_no'].required = False

        PA_same_as_CA = self.cleaned_data.get('pa_same_as_ca')
        print(PA_same_as_CA)
        if PA_same_as_CA == "Yes":
            self.fields['perm_address'].required = True
            self.fields['perm_state'].required = True
            self.fields['perm_pincode'].required = True
            self.fields['perm_city'].required = True
            self.fields['perm_tehsil'].required = True
            self.fields['perm_constituency'].required = True
            self.fields['comm_address'].required = False
            self.fields['comm_state'].required = False
            self.fields['comm_pincode'].required = False
            self.fields['comm_city'].required = False
            self.fields['comm_tehsil'].required = False
            self.fields['comm_constituency'].required = False
        elif PA_same_as_CA == "No":
            self.fields['perm_address'].required = True
            self.fields['perm_state'].required = True
            self.fields['perm_pincode'].required = True
            self.fields['perm_city'].required = True
            self.fields['perm_tehsil'].required = True
            self.fields['perm_constituency'].required = True
            self.fields['comm_address'].required = True
            self.fields['comm_state'].required = True
            self.fields['comm_pincode'].required = True
            self.fields['comm_city'].required = True
            self.fields['comm_tehsil'].required = True
            self.fields['comm_constituency'].required = True
        TrainingStatus = self.cleaned_data.get('training_status')  
        print(TrainingStatus)
        if TrainingStatus == "Fresher":
            self.field['job_details_prev_exp_sector'].required = False    
            self.field['job_details_no_of_months'].required = False  
            self.field['job_employed'].required = False    
            self.field['employment_status'].required = False  
            self.field['employment_details'].required = False 
        elif TrainingStatus == "Experienced":
            self.field['job_details_prev_exp_sector'].required = True   
            self.field['job_details_no_of_months'].required = True    
            self.field['job_employed'].required = True      
            self.field['employment_status'].required = True   
            self.field['employment_details'].required = True  

        DisabilityInput = self.cleaned_data.get('disability_input')  
        print(DisabilityInput)
        if DisabilityInput == "Yes":
            self.field['disability_type'].required = True
        elif DisabilityInput == "No":    
            self.field['disability_type'].required = False               
    
    def clean_email(self):
        print(self.cleaned_data['email']) 


class participantAwareForm(forms.ModelForm):
    class Meta:
        model = participant_aware
        fields = '__all__'

        #updating columns
        labels = {
            'program_id_aware' : 'Program Name',
            'participant_id_aware' : 'Serial number',
            'name_of_trainee' : 'Participant Name',
            'father_or_husband_name' : 'Father/Husband Name',
            'gender_aware' : 'Gender',
            'date_of_birth_aware' : 'Date of Birth',
            'idcard_aware_aadhaar_ref_no' : 'Aadhar Number',
            'mobile_entre_country_code' : 'Country Code',
            'mobile_entre_number' : 'Mobile Number',
            'category_aware' : 'Category',
            'qualification' : 'Qualification',
            'email' : 'Email',
            'address_aware_location': 'Address',
            'address_aware_city' : 'City',
            'address_aware_state' : 'State',
            }

    def __init__(self, *args, **kwargs):
        super(participantAwareForm, self).__init__(*args, **kwargs)
        self.fields['program_id_aware'].empty_label = "Select"
        self.fields['gender_aware'].empty_label = "(Select here)"
        self.fields['category_aware'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

    # def fields_required(self, fields):
    #     """Used for conditionally marking fields as required."""
    #     for field in fields:
    #         if not self.cleaned_data.get(field, ''):
    #             msg = forms.ValidationError("This field is required.")
    #             self.add_error(field, msg)



    def clean_email(self):
        print(self.cleaned_data['email'])


class participantCapacForm(forms.ModelForm):
    class Meta:
        model = participant_capac
        fields = '__all__'

        #updating columns
        labels = {
            'program_id_capac' : 'Program Name',
            'participant_id_capac' : 'Serial number',
            'name_of_trainee' : 'Participant Name',
            'father_or_husband_name' : 'Father/Husband Name',
            'gender_capac' : 'Gender',
            'date_of_birth_capac' : 'Date of Birth',
            'idcard_aware_aadhaar_ref_no' : 'Aadhar Number',
            'mobile_entre_country_code' : 'Country Code',
            'mobile_entre_number' : 'Mobile Number',
            'category_capac' : 'Category',
            'qualification' : 'Qualification',
            'email' : 'Email',
            'address_capac_location': 'Address',
            'address_capac_city' : 'City',
            'address_capac_state' : 'State',
            }

    def __init__(self, *args, **kwargs):
        super(participantCapacForm, self).__init__(*args, **kwargs)
        self.fields['program_id_capac'].empty_label = "Select"
        self.fields['gender_capac'].empty_label = "(Select here)"
        self.fields['category_capac'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})

    # def fields_required(self, fields):
    #     """Used for conditionally marking fields as required."""
    #     for field in fields:
    #         if not self.cleaned_data.get(field, ''):
    #             msg = forms.ValidationError("This field is required.")
    #             self.add_error(field, msg)



    def clean_email(self):
        print(self.cleaned_data['email'])




class placement_skillform(forms.ModelForm):
    class Meta:
        model = placement_skill
        fields = '__all__'

        # updating value of columns
        labels = {
            'participant_id_skill': 'Particpant ID',
            # 'placement_id_batch_id': 'Batch ID',
            # 'placement_id_rced_batch_id': 'RCED Batch ID',
            'course_name': 'Program Name',
            'placement_status': 'Placement Status',
            'reason': 'Reason',
            'employer_name': 'Employer Name',
            'job_type': 'Job Type',
            'job_position': 'Job Position',
            'salary' : 'Salary',
            'job_id' : 'Job ID',
            'other_benefit' : 'Other Benefit',
            'date_of_joining' : 'Date of Joining',
            'contact_person' : 'Contact Person',
            'contact_person_no' : 'Contact Person No'
        }

    def __init__(self, *args, **kwargs):
        super(placement_skillform, self).__init__(*args, **kwargs)
        self.fields['participant_id_skill'].empty_label = "Select"
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})
