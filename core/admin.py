from django.contrib import admin
from .models import category
from .models import dept_entre, dept_aware, dept_capac
from .models import dept_skill
from .models import program_entre, program_capac, program_aware
from .models import program_skill
from .models import participant_entre, participant_aware, participant_capac
from .models import participant_skill
from .models import placement_skill
from import_export.admin import ImportExportModelAdmin
from .resources import *

@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryAdminResource
    list_display = ['id','category_name']
    pass

@admin.register(dept_entre)
class DepartmentEntAdmin(ImportExportModelAdmin):
    list_display = ['id','category_ent','department_nam_ent']
    pass

@admin.register(dept_aware)
class DepartmentawareAdmin(ImportExportModelAdmin):
    list_display = ['id','category_aware','department_name_aware']
    pass

@admin.register(dept_capac)
class DepartmentcapacAdmin(ImportExportModelAdmin):
    list_display = ['id','category_capac','department_name_capac']
    pass

@admin.register(dept_skill)
class DepartmentSkillAdmin(ImportExportModelAdmin):
    list_display = ['id','category_skill','department_name_skill']
    pass

@admin.register(program_aware)
class ProgramawareAdmin(ImportExportModelAdmin):
    list_display = ['id','depart_name_aware','program_name_aware','state_aware','financial_year_aware','no_of_participants_aware','address_aware','address_aware_location','address_aware_city']
    pass

@admin.register(program_capac)
class ProgramCapacAdmin(ImportExportModelAdmin):
    list_display = ['id','depart_name_capac', 'program_name_capac', 'state_capac', 'financial_year_capac', 'no_of_participants_capac', 'address_capac', 'address_capac_location', 'address_capac_city']
    pass

@admin.register(program_entre)
class ProgramEntAdmin(ImportExportModelAdmin):
    list_display = ['id','depart_name_ent', 'program_name_ent', 'state_ent', 'financial_year_ent', 'no_of_participants_ent', 'address_ent', 'address_ent_location', 'address_ent_city']
    pass

@admin.register(program_skill)
class ProgramSkillAdmin(ImportExportModelAdmin):
    list_display = ['id','depart_name_skill','program_name_skill','state','financial_Year_skill','trade_skill','no_of_participants_skill','address_skill','address_skill_location','address_skill_city']
    pass

@admin.register(participant_entre)
class ParticipantEntAdmin(ImportExportModelAdmin):
    resource_class = ParticipantEntAdminResource
    list_display = ['program_id_ent','participant_id_ent','name_of_trainee','father_or_husband_name','gender','date_of_birth','idcard_entre_id_type','idcard_entre_alt_id_type','idcard_entre_aadhaar_ref_no','idcard_entre_alt_id_no','mobile_entre_country_code','mobile_entre_primary_mobile','mobile_entre_secondary_mobile','category_entre','job','qualification','project_identified','items_to_be_manufactured','place_of_unit','self_or_bank_financed','own_contribution_amount','date_of_loan_release','commencement_date','no_of_persons_employed','primary_email','secondary_email','address_entre_location','address_entre_city','address_entre_state','project_cost_CE','project_cost_WC','total']
    pass

@admin.register(participant_skill)
class ParticipantSkillAdmin(ImportExportModelAdmin):
    list_display = ['program_id_skill','batchid','participant_id_skill','name_skill_salutation', 'name_skill_FirstName', 'name_skill_LastName', 'gender', 'dob', 'Age', 'email', 'marital_status', 'fathers_name', 'mothers_name', 'Annual_income', 'religion', 'category', 'disability_input', 'disability_type', 'domicile_state', 'domicile_district', 'idcard_skill_id_type', 'idcard_skill_alt_id_type', 'idcard_skill_aadhaar_ref_no', 'idcard_skill_alt_id_no', 'mobile_skill_country_code', 'mobile_skill_primary_mobile', 'mobile_skill_secondary_mobile', 'education_level', 'perm_address', 'perm_state', 'perm_district', 'perm_pincode', 'perm_city', 'perm_tehsil', 'perm_constituency', 'pa_same_as_ca', 'comm_address', 'comm_state', 'comm_district', 'comm_pincode', 'comm_city', 'comm_tehsil', 'comm_constituency', 'training_status', 'job_details_prev_exp_sector', 'job_details_no_of_months', 'job_details_employed', 'job_details_employment_status', 'job_details_employment_details', 'heard_about_us']
    resource_class = ParticipantSkillAdminResource
    pass

@admin.register(participant_aware)
class ParticipantAwareAdmin(ImportExportModelAdmin):
    list_display = ['program_id_aware','participant_id_aware','name_of_trainee','father_or_husband_name','gender','date_of_birth','mobile_aware_country_code','mobile_aware_primary_mobile','mobile_aware_secondary_mobile','aadhaar_ref_no','category_aware','qualification','primary_email','secondary_email','address_aware_location','address_aware_city','address_aware_state']
    resource_class = ParticipantAwareAdminResource
    pass

@admin.register(participant_capac)
class ParticipantCapacAdmin(ImportExportModelAdmin):
    resource_class = ParticipantCapacAdminResource
    list_display = ['program_id_capac','participant_id_capac','name_of_trainee','father_or_husband_name','gender','date_of_birth','mobile_capac_country_code','mobile_capac_primary_mobile','mobile_capac_secondary_mobile','category_capac','qualification','primary_email','secondary_email','address_capac_location','address_capac_city','address_capac_state']
    pass

@admin.register(placement_skill)
class PlacementSkillAdmin(ImportExportModelAdmin):
    resource_class = PlacementSkillAdminResource
    list_display = ['participant_id_skill','course_name','placement_status','reason','employer_name','job_type','job_position','salary','job_id','other_benefit','date_of_joining','contact_person','contact_person_no']
    pass