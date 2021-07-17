# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this
from core.views import deptSkill, deptEnt, insprogEnt, insprogSkill, programSkill_list, programSkill_del, participant_ent, program_list, pm_del, participant_del, participant_list, insparticipant_skill, participantSkill_list, participantSkill_del, insplacementSkill, placementSkill_list, placementSkill_del, index, pages,insprogcap,deptCapac
from core.views import programCapac_del, programCapac_list, participantCapac_del, participantCapac_list, insparticipant_capac
from core.views import programaware_del, insparticipant_aware, deptaware, insprogaware, participantaware_list, programaware_list, participantaware_del

#django admin header customisation
admin.site.site_header = "RCED ADMIN PANEL"
admin.site.site_title = "Administration"
admin.site.index_title = "ADMIN PANEL"
urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin/' , admin.site.urls),
    path('deptEnt', deptEnt, name='deptEnt'),
    path('deptSkill', deptSkill, name = 'deptSkill'),
    path('deptCapac', deptCapac, name = 'deptCapac'),
    path('deptAware', deptaware, name = 'deptAware'),
    path('insprogEnt', insprogEnt, name='insprogEnt'), # get and post request for insert operation
    path('<int:id>/',insprogEnt,name = "program_update"), #get and post request for update operation
    path('program_list', program_list, name = 'program_list'),#display program routes
    path('delete/<int:id>/', pm_del ,name = 'program_delete'),
    path('insprogSkill', insprogSkill, name='insprogSkill'), # get and post request for insert operation
    path('Programskillupdate/<int:id>/',insprogSkill,name = "programSkill_update"), #get and post request for update operation
    path('programSkill_list', programSkill_list, name = 'programSkill_list'),#display program routes
    path('deleteprogramskill/<int:id>/', programSkill_del ,name = 'programSkill_del'),
    path('insertparticipant', participant_ent, name='participant_ent'),
    path('update/<int:participant_id_ent>/', participant_ent, name = "participant_update"),
    path('deleteent/<int:participant_id_ent>/', participant_del ,name = 'participant_delete'),
    path('participant_list', participant_list, name = 'participant_list'),
    path('insparticipant_skill', insparticipant_skill, name='insparticipant_skill'),
    path('updateskill/<int:participant_id_skill>/', insparticipant_skill, name = "participantSkill_update"),
    path('deleteskill/<int:participant_id_skill>/', participantSkill_del ,name = 'participantSkill_del'),
    path('participantSkill_list', participantSkill_list, name = 'participantSkill_list'),
    path('insplacementSkill', insplacementSkill, name='insplacementSkill'),
    path('updateskillID<int:participant_id_skill>/', insplacementSkill, name = "placementSkill_update"),
    path('delete_placementdetail/<int:participant_id_skill>/', placementSkill_del,name = 'placementSkill_del'),
    path('placementSkill_list', placementSkill_list, name = 'placementSkill_list'),
    path('insprogcap',insprogcap, name='insprogcap' ),
    path('updateprogramcapacity/<int:id>/',insprogcap,name = "capac_program_update"), #get and post request for update operation
    path('capacityprogram_list', programCapac_list, name = 'capac_program_list'),#display program routes
    path('deleteupdateprogramcapacity/<int:id>/', programCapac_del,name = 'capac_program_delete'),
    path('insparticipant_capac',insparticipant_capac, name='insparticipant_capac'),
    path('updatecapacity/<int:participant_id_capac>/', insparticipant_capac, name = "participantcapac_update"),
    path('deletecapacity/<int:participant_id_capac>/', participantCapac_del ,name = 'participantcapac_del'),
    path('participantcapacity_list', participantCapac_list, name = 'participantcapac_list'),

    path('insprogaware',insprogaware, name='insprogcap' ),
    path('updateprogramaware/<int:id>/',insprogaware,name = "aware_program_update"), #get and post request for update operation
    path('awareprogram_list', programaware_list, name = 'aware_program_list'),#display program routes
    path('deleteupdateprogramaware/<int:id>/', programaware_del,name = 'aware_program_delete'),
    path('insparticipant_aware',insparticipant_aware, name='insparticipant_aware'),
    path('updateaware/<int:participant_id_aware>/', insparticipant_aware, name = "participantaware_update"),
    path('deleteaware/<int:participant_id_aware>/', participantaware_del ,name = 'participantaware_del'),
    path('participantaware_list', participantaware_list, name = 'participantaware_list'),


    path("", include("authentication.urls")), # Auth routes - login / register
    # path("", include("app.urls")),            # UI Kits Html files
    path('', index, name='home'),
        # Matches any html file
    re_path(r'^.*\.*', pages, name='pages')
]
