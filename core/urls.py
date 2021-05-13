# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from . import views
from core.views import deptSkill, deptEnt, insprogEnt, participant_ent, program_list, pm_del, participant_del, participant_list

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin' , admin.site.urls),
    path('deptSkill', deptSkill, name='deptSkill'),
    path('deptEnt', deptEnt, name='deptEnt'),
    path('insprogEnt', insprogEnt, name='insprogEnt'), # get and post request for insert operation
    path('<int:id>/',insprogEnt,name = "program_update"), #get and post request for update operation
    path('delete/<int:id>/', pm_del ,name = 'program_delete'),
    path('insertparticipant', participant_ent, name='participant_ent'),
    path('<int:participant_id_ent>/', participant_ent, name = "participant_update"),
    path('delete/<int:participant_id_ent>/', participant_del ,name = 'participant_delete'),
    path('program_list', program_list, name = 'program_list'),#display program routes
    path('participant_list', participant_list, name = 'participant_list'),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),            # UI Kits Html files

]
