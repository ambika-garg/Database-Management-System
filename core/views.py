# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
# """
# from core.forms import Program_entreform
from core.models import program_entre
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib import messages

@login_required(login_url="/login/")
def index(request):
    print("index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def deptSkill(request):
    return render(request, 'ui-department_skill.html')

def deptEnt(request):
    return render(request, 'ui-department_ent.html')

def participant_ent(request):
    return render(request, 'ui-participants_ent.html')

def insprogEnt(request):
    # if request.method == "POST":
    #     form = Program_entreform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Program Added Successfully!')
    #     return redirect('/insprogEnt')
    # else:
    #     form = Program_entreform()
    # return render(request, 'ui-program_ent.html',{'form':form})
    return render(request, 'ui-program_ent.html')

