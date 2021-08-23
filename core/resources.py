from import_export import resources
from .models import *
from django.db import IntegrityError

class CategoryAdminAdminResource(resources.ModelResource):
    class Meta:
        model = category
        skip_unchanged = True
        report_skipped = True
    
    def save_instance(self, instance, using_transactions=True, dry_run=False):
                try:
                    super(CategoryAdminAdminResource, self).save_instance(instance, using_transactions, dry_run)
                except IntegrityError:
                    pass

class ParticipantEntAdminResource(resources.ModelResource):
    class Meta:
        model = participant_entre
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)

class ParticipantSkillAdminResource(resources.ModelResource):
    class Meta:
        model = participant_skill
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('program_id_skill','participant_id_skill','name_skill_salutation', 'name_skill_FirstName', 'name_skill_LastName', 'gender', 'dob', 'Age', 'email', 'marital_status', 'fathers_name', 'mothers_name', 'Annual_income', 'religion', 'category', 'disability_input', 'disability_type', 'domicile_state', 'domicile_district', 'idcard_skill_id_type', 'idcard_skill_alt_id_type', 'idcard_skill_aadhaar_ref_no', 'idcard_skill_alt_id_no', 'mobile_skill_country_code', 'mobile_skill_primary_mobile', 'mobile_skill_secondary_mobile', 'education_level', 'perm_address', 'perm_state', 'perm_district', 'perm_pincode', 'perm_city', 'perm_tehsil', 'perm_constituency', 'pa_same_as_ca', 'comm_address', 'comm_state', 'comm_district', 'comm_pincode', 'comm_city', 'comm_tehsil', 'comm_constituency', 'training_status', 'job_details'_'prev_exp_sector', 'job_details_no_of_months', 'job_details_employed', 'job_details_employment_status', 'job_details_employment_details', 'heard_about_us')      

class ParticipantAwareAdminResource(resources.ModelResource):
    class Meta:
        model = participant_aware
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)          

class ParticipantCapacAdminResource(resources.ModelResource):
    class Meta:
        model = participant_capac
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)     

class PlacementSkillAdminResource(resources.ModelResource):
    class Meta:
        model = placement_skill
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)                  