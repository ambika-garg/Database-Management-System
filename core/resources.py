from import_export import resources
from .models import *
from django.db import IntegrityError

class CategoryAdminResource(resources.ModelResource):
    class Meta:
        model = category
        skip_unchanged = True
        report_skipped = True
    
    def save_instance(self, instance, using_transactions=True, dry_run=False):
                try:
                    super(CategoryAdminResource, self).save_instance(instance, using_transactions, dry_run)
                except IntegrityError:
                    pass

class ParticipantEntAdminResource(resources.ModelResource):
    class Meta:
        model = participant_entre
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('program_id_ent','participant_id_ent','name_of_trainee','father_or_husband_name','gender','date_of_birth','idcard_entre_id_type','idcard_entre_alt_id_type','idcard_entre_aadhaar_ref_no','idcard_entre_alt_id_no','mobile_entre_country_code','mobile_entre_primary_mobile','mobile_entre_secondary_mobile','category_entre','job','qualification','project_identified','items_to_be_manufactured','place_of_unit','self_or_bank_financed','own_contribution_amount','date_of_loan_release','commencement_date','no_of_persons_employed','primary_email','secondary_email','address_entre_location','address_entre_city','address_entre_state','project_cost_CE','project_cost_WC')

class ParticipantSkillAdminResource(resources.ModelResource):
    class Meta:
        model = participant_skill
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('program_id_skill','batchid','participant_id_skill','name_skill_salutation', 'name_skill_FirstName', 'name_skill_LastName', 'gender', 'dob', 'Age', 'email', 'marital_status', 'fathers_name', 'mothers_name', 'Annual_income', 'religion', 'category', 'disability_input', 'disability_type', 'domicile_state', 'domicile_district', 'idcard_skill_id_type', 'idcard_skill_alt_id_type', 'idcard_skill_aadhaar_ref_no', 'idcard_skill_alt_id_no', 'mobile_skill_country_code', 'mobile_skill_primary_mobile', 'mobile_skill_secondary_mobile', 'education_level', 'perm_address', 'perm_state', 'perm_district', 'perm_pincode', 'perm_city', 'perm_tehsil', 'perm_constituency', 'pa_same_as_ca', 'comm_address', 'comm_state', 'comm_district', 'comm_pincode', 'comm_city', 'comm_tehsil', 'comm_constituency', 'training_status', 'job_details_prev_exp_sector', 'job_details_no_of_months', 'job_details_employed', 'job_details_employment_status', 'job_details_employment_details', 'heard_about_us')      

class ParticipantAwareAdminResource(resources.ModelResource):
    class Meta:
        model = participant_aware
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)   
        import_id_fields = ('program_id_aware','participant_id_aware','name_of_trainee','father_or_husband_name','gender','date_of_birth','mobile_aware_country_code','mobile_aware_primary_mobile','mobile_aware_secondary_mobile','aadhaar_ref_no','category_aware','qualification','primary_email','secondary_email','address_aware_location','address_aware_city','address_aware_state')
       

class ParticipantCapacAdminResource(resources.ModelResource):
    class Meta:
        model = participant_capac
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)  
        import_id_fields = ('program_id_capac','participant_id_capac','name_of_trainee','father_or_husband_name','gender','date_of_birth','mobile_capac_country_code','mobile_capac_primary_mobile','mobile_capac_secondary_mobile','category_capac','qualification','primary_email','secondary_email','address_capac_location','address_capac_city','address_capac_state')
   

class PlacementSkillAdminResource(resources.ModelResource):
    class Meta:
        model = placement_skill
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)     
        import_id_fields = ('participant_id_skill','course_name','placement_status','reason','employer_name','job_type','job_position','salary','job_id','other_benefit','date_of_joining','contact_person','contact_person_no')
         