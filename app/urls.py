# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views
from django.contrib import admin

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # path('admin/', admin.site.urls),
    # path('progEnt/', views.progEnt, name='program_entre'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
