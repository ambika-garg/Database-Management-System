# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models


# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=100)
    #
    # class Meta:
    #     verbose_name_plural = "Categories"
    #
    # def __str__(self):
    #     return self.category_name


class dept_entre(models.Model):
    category_ent = models.ForeignKey(category, default=1, verbose_name="category", on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)
    # class Meta:
    #     verbose_name_plural = "department"
    #
    def __str__(self):
        return self.department_name

class dept_skill(models.Model):
    category_skill = models.ForeignKey(category, default=2, verbose_name="category", on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)
    # class Meta:
    #     verbose_name_plural = "department"
    #
    def __str__(self):
        return self.department_name        


class program_entre(models.Model):
    depart_name = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100, unique = True)
    state = models.CharField(max_length=100, blank = True)
    financial_year = models.IntegerField()
    no_of_participants = models.IntegerField(null=True)
    objects = models.Manager()
    def __str__(self):
        return self.program_name

class program_skill(models.Model):
    depart_name = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100, unique = True)
    location = models.CharField(max_length=100, blank = True)
    financial_year = models.DateField()
    trade =  models.CharField(max_length=100, blank = True)
    no_of_participants = models.IntegerField(null=True)
    objects = models.Manager() #doubt    
    def __str__(self):
        return self.program_name

class program_address_state_skill(models.Model): 
    program_id = models.ForeignKey(program_skill, on_delete=models.CASCADE)
    state = models.CharField(max_length=25, blank = True) #doubt

class program_address_location_skill(models.Model):
    program_id = models.ForeignKey(program_skill, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank = True) #doubt    

class participant_skill(models.Model): 
    program_id = models.ForeignKey(program_skill, on_delete=models.CASCADE)
    gender = models.CharField(max_length=25, blank = True)
    dob = models.DateField()
    email = models.CharField(max_length=25, blank = True, unique=True)
    marital_status = models.CharField(max_length=25, blank = True)
    fathers_name = models.CharField(max_length=25, blank = True)
    mothers_name = models.CharField(max_length=25, blank = True)
    religion = models.CharField(max_length=25, blank = True)
    category = models.CharField(max_length=25, blank = True)
    education_level = models.CharField(max_length=25, blank = True)
    pa_same_as_ca = models.CharField(max_length=25, blank = True)
    training_status = models.CharField(max_length=25, blank = True)
    heard_about_us = models.CharField(max_length=25, blank = True)
    # def __str__(self):
    #     return self.  #doubt

class participant_name_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=25, blank = True)
    full_name  = models.CharField(max_length=25, blank = True)

class participant_comm_address_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    address_comm = models.CharField(max_length=100, blank = True)
    state_comm = models.CharField(max_length=25, blank = True)
    district_comm = models.CharField(max_length=25, blank = True)
    pincode_comm = models.IntegerField()
    city_comm = models.CharField(max_length=25, blank = True)
    tehsil_comm = models.CharField(max_length=25, blank = True)
    constituency_comm = models.CharField(max_length=25, blank = True)

class participant_disability_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    disability_input = models.CharField(max_length=25, blank = True)
    disability_type = models.CharField(max_length=25, blank = True)

class participant_domicile_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    dom_state = models.CharField(max_length=25, blank = True)
    dom_district = models.CharField(max_length=25, blank = True)

class participant_id_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    id_type = models.CharField(max_length=25, blank = True)
    alt_id_type = models.CharField(max_length=25, blank = True)
    aadhaar_ref_no = models.IntegerField(unique = True)
    id_no = models.IntegerField(unique = True)

class participant_job_details_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    prev_exp_sector = models.CharField(max_length=25, blank = True)
    no_of_months = models.IntegerField()
    employed = models.CharField(max_length=25, blank = True)
    employment_status = models.CharField(max_length=25, blank = True)
    employment_details = models.CharField(max_length=50, blank = True)

class participant_mobile_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    country_code = models.IntegerField()
    mobile_number = models.IntegerField(unique = True)

class participant_number_skill(models.Model): #doubt
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    number1 = models.IntegerField()
    number2 = models.IntegerField()

class participant_perm_address_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    address_perm = models.CharField(max_length=100, blank = True)
    state_perm = models.CharField(max_length=25, blank = True)
    district_perm = models.CharField(max_length=25, blank = True)
    pincode_perm = models.IntegerField()
    city_perm = models.CharField(max_length=25, blank = True)
    tehsil_perm = models.CharField(max_length=25, blank = True)
    constituency_perm = models.CharField(max_length=25, blank = True)

class placement_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50, blank = True)
    placement_status = models.CharField(max_length=25, blank = True)
    reason = models.CharField(max_length=25, blank = True)
    employer_name = models.CharField(max_length=25, blank = True)
    job_type = models.CharField(max_length=25, blank = True)
    job_position = models.CharField(max_length=25, blank = True)
    salary = models.IntegerField()
    job_id = models.IntegerField()
    other_benefit = models.CharField(max_length=100, blank = True)
    date_of_joining = models.DateField()
    contact_person = models.CharField(max_length=25, blank = True)
    contact_person_no = models.IntegerField()

class placement_skill(models.Model):
    participant_id_skill = models.ForeignKey(participant_skill, on_delete=models.CASCADE)
    batch_id = models.IntegerField()
    rced_batch_id = models.IntegerField()

class participant_entre(models.Model): 
    program_id = models.ForeignKey(program_entre,default=1,on_delete=models.CASCADE)
    ID_proof = models.CharField(max_length=20,unique=True)
    category = models.CharField(max_length=20,unique=False)
    job = models.CharField(max_length=25,unique=False)
    qualification = models.CharField(max_length=25,unique=False)
    project_identified = models.CharField(max_length=50,unique=False)
    items_to_be_manufactured = models.CharField(max_length=50,unique=False)
    place_of_unit = models.CharField(max_length=40,unique=False)
    self_or_bank_financed = models.CharField(max_length=20,unique=False)
    own_contribution_amount = models.IntegerField()
    date_of_loan_release = models.DateField()
    commencement_date = models.DateField()
    no_of_persons_employed = models.IntegerField()
    # def __str__(self):
    #     return self. #doubt

class participant_email_entre(models.Model): 
    serial_number=models.ForeignKey(participant_entre,default=1,on_delete=models.CASCADE)
    email = models.CharField(max_length=50,unique=True)

class participant_mobile_entre(models.Model): 
    serial_number=models.ForeignKey(participant_entre,default=1,on_delete=models.CASCADE)
    mobile_number = models.IntegerField(unique=True)

class participant_address_entre(models.Model): 
    serial_number=models.ForeignKey(participant_entre,default=1,on_delete=models.CASCADE)
    location = models.CharField(max_length=100,unique=False)
    city =  models.CharField(max_length=50,unique=False)
    state =  models.CharField(max_length=40,unique=False)

class participant_project_cost_entre(models.Model): 
    serial_number=models.ForeignKey(participant_entre,default=1,on_delete=models.CASCADE)
    CE= models.IntegerField()
    WC= models.IntegerField()
    total= models.IntegerField() #default=CE+WC

class participant_ID_entre(models.Model):
    ID_proof =models.ForeignKey(participant_entre,default=1,on_delete=models.CASCADE) #kya hai?
    name_of_trainee = models.CharField(max_length=50,unique=False)
    father_or_husband_name = models.CharField(max_length=50,unique=False)
    gender = models.CharField(max_length=10,unique=False)
    date_of_birth = models.DateField()

class program_address_entre(models.Model):
    program_id = models.ForeignKey(program_entre,default=1,on_delete=models.CASCADE)
    college_name = models.CharField(max_length=100,unique=False)
    location = models.CharField(max_length=50,unique=False)
    city = models.CharField(max_length=40,unique=False)
