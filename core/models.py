# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from composite_field import CompositeField
from django.contrib.auth.models import User
from django.db import models
from collectionfield.models import CollectionField
from django.core.exceptions import ValidationError
from django.db.models.fields import EmailField


# Create your models here.
# 1
class category(models.Model):
    category_name = models.CharField(max_length=100)


# 2
class dept_entre(models.Model):
    category_ent = models.ForeignKey(category, default=1, verbose_name="category", on_delete=models.CASCADE)
    department_nam_ent = models.CharField(max_length=100)

    def __str__(self):
        return self.department_nam_ent

# 3
class dept_skill(models.Model):
    category_skill = models.ForeignKey(category, default=2, verbose_name="category", on_delete=models.CASCADE)
    department_name_skill = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name_skill

class program_address(CompositeField):
    location = models.CharField(max_length=50, unique=False)
    city = models.CharField(max_length=40, unique=False)

#4
class program_entre(models.Model):
    depart_name_ent = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name_ent = models.CharField(max_length=100, unique=True)
    state_ent = models.CharField(max_length=100, blank=True)
    financial_year_ent = models.CharField(max_length=10)
    college_name_ent = models.CharField(max_length=100)
    no_of_participants_ent = models.IntegerField(null=True)
    address_ent = program_address()
    objects = models.Manager()

    def __str__(self):
        return self.program_name_ent

#5
class program_skill(models.Model):
    depart_name_skill = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name_skill = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=30)
    financial_Year_skill = models.CharField(max_length=10)
    trade_skill = models.CharField(max_length=100, blank=True)
    no_of_participants_skill = models.IntegerField(null=True)
    address_skill = program_address()
    objects = models.Manager()

    def _str_(self):
        return self.program_name_skill


class participant_address_entre(CompositeField):
    location = models.CharField(max_length=100, unique=False)
    city = models.CharField(max_length=50, unique=False)
    state = models.CharField(max_length=40, unique=False)


class participant_mobile(CompositeField):
    country_code = models.IntegerField()
    mobile_number = CollectionField(item_type=int, collection_type=set, max_length=10,  max_items=2)


class participant_idcard(CompositeField):
    ID_TYPE_CHOICES = (('Alternate ID', 'Alternate ID'), ('Aadhar ID', 'Aadhar ID'))
    ALT_ID_TYPE_CHOICES = (
    ('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Domicile Certificate', 'Domicile Certificate'),
    ('ST/SC Certificate', 'ST/SC Certificate'),
    ('Permanent Residential Certificate (PRC)', 'Permanent Residential Certificate (PRC)'),
    ('Driving License', 'Driving License'), ('Ration Card', 'Ration Card'),
    ('Birth Certificate issued by Government', 'Birth Certificate issued by Government'), ('BPL Card', 'BPL Card'), 
    ('National Population Register (NPR) Card', 'National Population Register (NPR) Card'), 
    ('Identity proof by Gazetted officers', 'Identity proof by Gazetted officers'), ('Passport', 'Passport'),
    ('Jail Identification Card/ Number', 'Jail Identification Card/ Number'),
    ('School leaving certificate/10th certificate', 'School leaving certificate/10th certificate'),
    ('Letter of domicile from SDM/DM/Government Authority', 'Letter of domicile from SDM/DM/Government Authority'))
    id_type = models.CharField(max_length=25, blank=True, choices=ID_TYPE_CHOICES, null=True)
    alt_id_type = models.CharField(max_length=100, blank=True, choices=ALT_ID_TYPE_CHOICES, null=True)
    aadhaar_ref_no = models.IntegerField(unique=True, null=True)
    alt_id_no = models.IntegerField(unique=True, null=True)
    def alt_it_type_check(self):
        if self.id_type == 'Aadhar ID' and self.alt_id_type is not None:
            raise ValidationError('Not to be filled if selected as Aadhar ID in the ID Type')
        elif self.id_type == 'Aadhar ID' and self.alt_id_no is not None:
            raise ValidationError('Not to be filled if selected as Aadhar ID in the ID Type')

class participant_project_cost_entre(CompositeField):
    CE = models.IntegerField(default=0)
    WC = models.IntegerField(default=0)

    @property
    def total(self):
        return self.CE + self.WC

#6
class participant_entre(models.Model):
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    program_id = models.ForeignKey(program_entre, default=1, on_delete=models.CASCADE)
    participant_id_ent = models.IntegerField(primary_key=True, unique=True)
    name_of_trainee = models.CharField(max_length=50, unique=False)
    father_or_husband_name = models.CharField(max_length=50, unique=False)
    gender = models.CharField(max_length=25, blank=True, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    idcard_entre = participant_idcard()
    mobile_entre = participant_mobile()
    category_entre = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    job = models.CharField(max_length=25, unique=False)
    qualification = models.CharField(max_length=25, unique=False)
    project_identified = models.CharField(max_length=50, unique=False)
    items_to_be_manufactured = models.CharField(max_length=50, unique=False)
    place_of_unit = models.CharField(max_length=40, unique=False)
    self_or_bank_financed = models.CharField(max_length=20, unique=False)
    own_contribution_amount = models.IntegerField()
    date_of_loan_release = models.DateField()
    commencement_date = models.DateField()
    no_of_persons_employed = models.IntegerField()
    email = CollectionField(collection_type=set, item_type=EmailField, max_items=2)
    address_entre = participant_address_entre()

class participant_name_skill(CompositeField):
    SALUTATION_CHOICES = (('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mx', 'Mx'))
    salutation = models.CharField(max_length=25, blank=True, choices=SALUTATION_CHOICES)
    FirstName = models.CharField(max_length=25, blank=True)
    LastName = models.CharField(max_length=25, blank=True)


class participant_comm_address_skill(CompositeField):
    address_comm = models.CharField(max_length=100, blank=True)
    state_comm = models.CharField(max_length=25, blank=True)
    district_comm = models.CharField(max_length=25, blank=True)
    pincode_comm = models.IntegerField()
    city_comm = models.CharField(max_length=25, blank=True)
    tehsil_comm = models.CharField(max_length=25, blank=True)
    constituency_comm = models.CharField(max_length=25, blank=True)


class participant_disability_skill(CompositeField):
    INPUT_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    TYPE_CHOICES = (('Locomotor Disability', 'Locomotor Disability'), ('Leprosy Cured Person', 'Leprosy Cured Person'),
                    ('Dwarfism', 'Dwarfism'), ('Acid Attack Victim', 'Acid Attack Victim'),
                    ('Blindness/VisualImpairment', 'Blindness/VisualImpairment'),
                    ('Low-vision (Visual Impairment)', 'Low-vision (Visual Impairment)'), ('Deaf', 'Deaf'),
                    ('Hard of Hearing', 'Hard of Hearing'),
                    ('Speech and Language Disability', 'Speech and Language Disability'),
                    ('Intellectual Disability /Mental Retardation', 'Intellectual Disability /Mental Retardation'),
                    ('Autism Spectrum Disorder', 'Autism Spectrum Disorder'),
                    ('Specific Learning Disabilities', 'Specific Learning Disabilities'),
                    ('Mental Behavior-Mental Illness', 'Mental Behavior-Mental Illness'),
                    ('Haemophilia', 'Haemophilia'), ('Thalassemia', 'Thalassemia'),
                    ('Sickle Cell Disease', 'Sickle Cell Disease'), ('Deaf Blindness', 'Deaf Blindness'),
                    ('Cerebral Palsy', 'Cerebral Palsy'), ('Multiple Sclerosis', 'Multiple Sclerosis'),
                    ('Muscular Dystrophy', 'Muscular Dystrophy'))
    disability_input = models.CharField(max_length=25, blank=True, choices=INPUT_CHOICES)
    disability_type = models.CharField(max_length=25, blank=True)

    def disability_check(self):
        if self.disability_input == 'Yes' and self.disability_type is None:
            raise ValidationError('Disability type cannot be null!')


class participant_domicile_skill(CompositeField):
    dom_state = models.CharField(max_length=25, blank=True)
    dom_district = models.CharField(max_length=25, blank=True)


class participant_job_details_skill(CompositeField):
    EMPLOYED_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    EMPLOYMENT_STATUS_CHOICES = (('Employed Through Registered Employer', 'Employed Through Registered Employer'),
                                 ('Opted for Higher Studies', 'Opted for Higher Studies'),
                                 ('Self Employed', 'Self Employed'), ('Up Skilled', 'Up Skilled'),
                                 ('Employed', 'Employed'), ('NA', 'NA'),
                                 ('Employed at Training Partner', 'Employed at Training Partner'),
                                 ('Employed at Other Firm', 'Employed at Other Firm'))
    prev_exp_sector = models.CharField(max_length=25, blank=True)
    no_of_months = models.IntegerField()
    employed = models.CharField(max_length=25, blank=True, choices=EMPLOYED_CHOICES)
    employment_status = models.CharField(max_length=100, blank=True, unique=False, choices=EMPLOYMENT_STATUS_CHOICES)
    employment_details = models.CharField(max_length=100, blank=True)


class participant_perm_address_skill(CompositeField):
    address_perm = models.CharField(max_length=100, blank=True)
    state_perm = models.CharField(max_length=25, blank=True, unique=False)
    district_perm = models.CharField(max_length=25, blank=True, unique=False)
    pincode_perm = models.IntegerField()
    city_perm = models.CharField(max_length=25, blank=True, unique=False)
    tehsil_perm = models.CharField(max_length=25, blank=True, unique=False)
    constituency_perm = models.CharField(max_length=25, blank=True, unique=False)

#7
class participant_skill(models.Model):
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    MARITAL_STATUS_CHOICES = (
    ('Single/Unmarried', 'Single/Unmarried'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced'),
    ('Separated', 'Separated'), ('Not to be Disclosed', 'Not to be Disclosed'))
    PA_SAME_AS_CA_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    RELIGION_CHOICES = (
    ('Atheist', 'Atheist'), ('Hinduism', 'Hinduism'), ('Christianity', 'Christianity'), ('Islam', 'Islam'),
    ('Jews', 'Jews'), ('Buddhism', 'Buddhism'), ('Zoroastrian', 'Zoroastrian'), ('Jainism', 'Jainism'),
    ('Not to be Disclosed', 'Not to be Disclosed'))
    TRAINING_STATUS_CHOICES = (('Fresher', 'Fresher'), ('Experienced', 'Experienced'))
    HEARD_ABOUT_US_CHOICES = (
    ('Poster', 'Poster'), ('SMS', 'SMS'), ('Training Provider', 'Training Provider'), ('Internet', 'Internet'),
    ('Government Agency', 'Government Agency'), ('Radio', 'Radio'), ('Newspaper', 'Newspaper'),
    ('Television', 'Television'), ('Advertisements', 'Advertisements'), ('Social Media', 'Social Media'),
    ('Pamphlets', 'Pamphlets'), ('Recorded phone', 'Recorded phone'), ('Message', 'Message'),
    ('Newsletter', 'Newsletter'), ('Kaushal Mela', 'Kaushal Mela'), ('Call Center', 'Call Center'),
    ('Rozgar Mela', 'Rozgar Mela'), ('Others', 'Others'), ('Event/Workshop', 'Event/Workshop'))
    program_id = models.ForeignKey(program_skill, on_delete=models.CASCADE)
    participant_id_skill = models.IntegerField(primary_key=True, unique=True)
    name_skill = participant_name_skill()
    gender = models.CharField(max_length=25, blank=True, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField(max_length=25, blank=True, unique=True)
    marital_status = models.CharField(max_length=25, blank=True, choices=MARITAL_STATUS_CHOICES)
    fathers_name = models.CharField(max_length=25, blank=True)
    mothers_name = models.CharField(max_length=25, blank=True)
    religion = models.CharField(max_length=25, blank=True, choices=RELIGION_CHOICES)
    category = models.CharField(max_length=25, blank=True, choices=CATEGORY_CHOICES)
    disability = participant_disability_skill()
    domicile = participant_domicile_skill()
    idcard_skill = participant_idcard()
    mobile_skill = participant_mobile()
    education_level = models.CharField(max_length=25, blank=True)
    perm_address = participant_perm_address_skill()
    pa_same_as_ca = models.CharField(max_length=25, blank=True, choices=PA_SAME_AS_CA_CHOICES)
    comm_address = participant_comm_address_skill()
    training_status = models.CharField(max_length=25, blank=True)
    participant_job_details = participant_job_details_skill()
    heard_about_us = models.CharField(max_length=25, blank=True)

    def comm_address_check(self):
        if self.pa_same_as_ca == 'Yes' and self.comm_address is not None:
            raise ValidationError('Permanent Address is same as Communication Address!')
        elif self.pa_same_as_ca == 'No' and self.comm_address is None:
            raise ValidationError('Permanent Address is not same as Communication Address!')

    def participant_job_details_check(self):
        if self.training_status == 'Fresher' and self.participant_job_details is not None:
            raise ValidationError('Job details are not required for Fresher!')
        elif self.training_status == 'Experienced' and self.participant_job_details is None:
            raise ValidationError('Job details are required for Experienced!')

class placement_id_skill(CompositeField):
    batch_id = models.IntegerField()
    rced_batch_id = models.IntegerField()

#8
class placement_skill(models.Model):
    participant_id_skill = models.OneToOneField(participant_skill, on_delete=models.CASCADE)
    placement_id = placement_id_skill()
    course_name = models.CharField(max_length=50, blank=True, unique=False)
    placement_status = models.CharField(max_length=25, blank=True, unique=False)
    reason = models.CharField(max_length=25, blank=True, unique=False)
    employer_name = models.CharField(max_length=25, blank=True, unique=False)
    job_type = models.CharField(max_length=25, blank=True, unique=False)
    job_position = models.CharField(max_length=25, blank=True, unique=False)
    salary = models.IntegerField()
    job_id = models.IntegerField()
    other_benefit = models.CharField(max_length=100, blank=True, unique=False)
    date_of_joining = models.DateField()
    contact_person = models.CharField(max_length=25, blank=True, unique=False)
    contact_person_no = models.IntegerField()
