# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from . import views
from core.views import deptSkill, deptEnt, insprogEnt, participant_ent

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin' , admin.site.urls),
    path('deptSkill', deptSkill, name='deptSkill'),
    path('deptEnt', deptEnt, name='deptEnt'),
    path('insprogEnt', insprogEnt, name='insprogEnt'),
    path('insertparticipant', participant_ent, name='participant_ent'),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),            # UI Kits Html files

]
