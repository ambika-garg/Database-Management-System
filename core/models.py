# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django_pg.models import CompositeField
from django.contrib.auth.models import User
from django.db import models
from collectionfield.models import CollectionField


# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=100)

class AddressField(CompositeField):
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=50, unique=False)
    city = models.CharField(max_length=40, unique=False)

class NameField(CompositeField):
    salutation = models.CharField(max_length=25, blank=True)
    FirstName = models.CharField(max_length=25, blank=True)
    LastName = models.CharField(max_length=25, blank=True)

class ParticipantComAddField(CompositeField):
    address_comm = models.CharField(max_length=100, blank=True)
    state_comm = models.CharField(max_length=25, blank=True)
    district_comm = models.CharField(max_length=25, blank=True)
    pincode_comm = models.IntegerField()
    city_comm = models.CharField(max_length=25, blank=True)
    tehsil_comm = models.CharField(max_length=25, blank=True)
    constituency_comm = models.CharField(max_length=25, blank=True)


class dept_entre(models.Model):
    category_ent = models.ForeignKey(category, default=1, verbose_name="category", on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class dept_skill(models.Model):
    category_skill = models.ForeignKey(category, default=2, verbose_name="category", on_delete=models.CASCADE)
    department_name_skill = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name_skill


class program_entre(models.Model):
    depart_name = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=100, blank=True)
    financial_year = models.CharField(max_length=10)
    college_name = models.CharField(max_length=100)
    no_of_participants = models.IntegerField(null=True)
    address = AddressField()
    objects = models.Manager()

    def __str__(self):
        return self.program_name


class program_skill(models.Model):
    depart_name_skill = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name_skill = models.CharField(max_length=100, unique=True)
    financial_year_skill = financial_year = models.CharField(max_length=10)
    trade_skill = models.CharField(max_length=100, blank=True)
    no_of_participants_skill = models.IntegerField(null=True)
    Address_skill = AddressField()
    objects = models.Manager()

    def __str__(self):
        return self.program_name_skill


class participant_skill(models.Model):
    CATEGORY_CHOICES = ['General', 'OBC', 'SC', 'ST']
    program_id = models.ForeignKey(program_skill, on_delete=models.CASCADE)
    participant_id_skill = models.IntegerField(primary_key=True, unique=True)
    name_skill = NameField()
    gender = models.CharField(max_length=25, blank=True)
    dob = models.DateField()
    email = models.EmailField(max_length=25, blank=True, unique=True)
    marital_status = models.CharField(max_length=25, blank=True)
    fathers_name = models.CharField(max_length=25, blank=True)
    mothers_name = models.CharField(max_length=25, blank=True)
    religion = models.CharField(max_length=25, blank=True)
    category = models.CharField(max_length=25, blank=True, choices=CATEGORY_CHOICES)
    education_level = models.CharField(max_length=25, blank=True)
    pa_same_as_ca = models.CharField(max_length=25, blank=True)
    training_status = models.CharField(max_length=25, blank=True)
    heard_about_us = models.CharField(max_length=25, blank=True)
    Communication_address = ParticipantComAddField()
    contact_number = CollectionField(item_type=int, collection_type=set, max_length = 10)




class participant_disability_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    disability_input = models.CharField(max_length=25, blank=True)
    disability_type = models.CharField(max_length=25, blank=True)


class participant_domicile_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    dom_state = models.CharField(max_length=25, blank=True)
    dom_district = models.CharField(max_length=25, blank=True)


class participant_id_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    id_type = models.CharField(max_length=25, blank=True)
    alt_id_type = models.CharField(max_length=25, blank=True)
    aadhaar_ref_no = models.IntegerField(unique=True)
    id_no = models.IntegerField(unique=True)


class participant_job_details_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    prev_exp_sector = models.CharField(max_length=25, blank=True)
    no_of_months = models.IntegerField()
    employed = models.CharField(max_length=25, blank=True)
    employment_status = models.CharField(max_length=25, blank=True, unique=False)
    employment_details = models.CharField(max_length=50, blank=True)


class participant_mobile_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    country_code = models.IntegerField()
    mobile_number = models.IntegerField(unique=True)


class participant_perm_address_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    address_perm = models.CharField(max_length=100, blank=True)
    state_perm = models.CharField(max_length=25, blank=True, unique=False)
    district_perm = models.CharField(max_length=25, blank=True, unique=False)
    pincode_perm = models.IntegerField()
    city_perm = models.CharField(max_length=25, blank=True, unique=False)
    tehsil_perm = models.CharField(max_length=25, blank=True, unique=False)
    constituency_perm = models.CharField(max_length=25, blank=True, unique=False)


class placement_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
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


class placement_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    batch_id = models.IntegerField()
    rced_batch_id = models.IntegerField()


class participant_entre(models.Model):
    CATEGORY_CHOICES = ['General', 'OBC', 'SC', 'ST']
    program_id = models.ForeignKey(program_entre, default=1, on_delete=models.CASCADE)
    participant_id_ent = models.IntegerField(primary_key=True, unique=True)
    name_of_trainee = NameField()
    father_or_husband_name = models.CharField(max_length=50, unique=False)
    gender = models.CharField(max_length=10, unique=False)
    date_of_birth = models.DateField()
    aadhar_number = models.IntegerField(max_length=20, unique=True)  # id number#re
    primary_email = models.EmailField(max_length=50)
    secondary_email = models.EmailField(max_length=50)
    primary_mobile_number = models.IntegerField(unique=True)
    secondary_mobile_number = models.IntegerField(unique=True)
    category_entre = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # text choices general sc st obc
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
    Address = AddressField()

class participant_project_cost_entre(models.Model):
    Serial_number = models.ForeignKey(participant_entre, default=1, on_delete=models.CASCADE)
    CE = models.IntegerField(default=0)
    WC = models.IntegerField(default=0)

    @property
    def total(self):
        return self.CE + self.WC


