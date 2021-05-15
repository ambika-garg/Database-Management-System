# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from core.views import deptSkill, deptEnt, insprogEnt, insprogSkill, programSkill_list, programSkill_del, participant_ent, program_list, pm_del, participant_del, participant_list, insparticipant_skill, participantSkill_list, participantSkill_del, insplacementSkill, placementSkill_list, placementSkill_del

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin' , admin.site.urls),
    path('deptSkill', deptSkill, name='deptSkill'),
    path('deptEnt', deptEnt, name='deptEnt'),
    path('insprogEnt', insprogEnt, name='insprogEnt'), # get and post request for insert operation
    path('<int:id>/',insprogEnt,name = "program_update"), #get and post request for update operation
    path('program_list', program_list, name = 'program_list'),#display program routes
    path('delete/<int:id>/', pm_del ,name = 'program_delete'),
    path('insprogSkill', insprogSkill, name='insprogSkill'), # get and post request for insert operation
    path('<int:id>/',insprogSkill,name = "programSkill_update"), #get and post request for update operation
    path('programSkill_list', programSkill_list, name = 'programSkill_list'),#display program routes
    path('delete/<int:id>/', programSkill_del ,name = 'programSkill_del'),
    path('insertparticipant', participant_ent, name='participant_ent'),
    path('<int:participant_id_ent>/', participant_ent, name = "participant_update"),
    path('delete/<int:participant_id_ent>/', participant_del ,name = 'participant_delete'),
    path('participant_list', participant_list, name = 'participant_list'),
    path('insparticipant_skill', insparticipant_skill, name='insparticipant_skill'),
    path('<int:participant_id_skill>/', insparticipant_skill, name = "participantSkill_update"),
    path('delete/<int:participant_id_skill>/', participantSkill_del ,name = 'participantSkill_del'),
    path('participantSkill_list', participantSkill_list, name = 'participantSkill_list'),
    path('insplacementSkill', insplacementSkill, name='insplacementSkill'),
    path('<int:participant_id_skill>/', insplacementSkill, name = "placementSkill_update"),
    path('delete/<int:participant_id_skill>/', placementSkill_del ,name = 'placementSkill_del'),
    path('placementSkill_list', placementSkill_list, name = 'placementSkill_list'),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),            # UI Kits Html files
]
