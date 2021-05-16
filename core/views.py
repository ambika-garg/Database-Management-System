from core.forms import program_entreform, program_skillform, participantForm, participantSkillForm, placement_skillform
from core.models import dept_entre, dept_skill, program_entre, program_skill, participant_entre, participant_skill, placement_skill
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
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

def deptEnt(request):
    context = {'deptEnt': dept_entre.objects.all()}
    return render(request, 'ui-view_department_ent.html', context)

def deptSkill(request):
    context = {'deptSkill': dept_skill.objects.all()}
    return render(request, 'ui-view_department_skill.html', context)

def insprogEnt(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = program_entreform(request.POST)
        else:
            program = program_entre.objects.get(pk=id)
            form = program_entreform(request.POST, instance=program)
            print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program Added Successfully!')
        return redirect('/insprogEnt')
    else:
        if id == 0:
            form = program_entreform()
        else:
            program = program_entre.objects.get(pk=id)
            form = program_entreform(instance=program)
    return render(request, 'ui-program_ent.html', {'form': form})

def program_list(request):
    context = {'program_list': program_entre.objects.all()}
    return render(request, 'ui-view_program_ent.html', context)

def pm_del(request, id):
    program = program_entre.objects.get(pk=id)
    program.delete()
    return render(request, '/program_list')

def insprogSkill(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = program_skillform(request.POST)
        else:
            program = program_skill.objects.get(pk=id)
            form = program_skillform(request.POST, instance=program)
            print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program Added Successfully!')
        return redirect('/insprogSkill')
    else:
        if id == 0:
            form = program_skillform()
        else:
            program = program_skill.objects.get(pk=id)
            form = program_skillform(instance=program)
    return render(request, 'ui-program_skill.html', {'form': form})

def programSkill_list(request):
    context = {'programSkill_list': program_skill.objects.all()}
    return render(request, 'ui-view_program_skill.html', context)

def programSkill_del(request, id):
    print(id)
    program = program_skill.objects.get(pk=id)
    program.delete()
    return render(request, 'ui-view_program_skill.html')

def participant_ent(request, participant_id_ent=0):
    if request.method == "POST":
        if participant_id_ent == 0:
            fi = participantForm(request.POST)
            email = request.POST.get('email')
        else:
            participant = participant_entre.objects.get(pk = participant_id_ent)
            print("particpant:", participant)
            fi = participantForm(request.POST, instance = participant)
            email = request.POST.get('email')
            print("email: ", email)
        if fi.is_valid():
            fi.save()
            messages.success(request, 'Program Added Successfully!')
            return redirect('/insertparticipant')
    else:
        if participant_id_ent == 0:
            fi = participantForm()
            email = request.POST.get('email')
        else:
            participant = participant_entre.objects.get(pk = participant_id_ent)
            fi = participantForm(instance = participant)
            email = request.POST.get('email')

    return render(request, 'ui-participants_ent.html', {'form': fi, 'email': email})

def participant_list(request):
    context = {'participant_list': participant_entre.objects.all()}
    return render(request, 'ui-view_participant_ent.html', context)

def participant_del(request,  participant_id_ent):
    program = participant_entre.objects.get(pk= participant_id_ent)
    program.delete()
    return render(request, '/participant_list')

def insparticipant_skill(request, participant_id_skill=0):
    if request.method == "POST":
        if participant_id_skill == 0:
            fi = participantSkillForm(request.POST)
            email = request.POST.get('email')
        else:
            participant = participant_skill.objects.get(pk = participant_id_skill)
            print("particpant:", participant)
            fi = participantSkillForm(request.POST, instance = participant)
            email = request.POST.get('email')
            print("email: ", email)
        if fi.is_valid():
            fi.save()
            messages.success(request, 'Program Added Successfully!')
            return redirect('/insparticipant_skill')
    else:
        if participant_id_skill == 0:
            fi = participantSkillForm()
            email = request.POST.get('email')
        else:
            participant = participant_skill.objects.get(pk = participant_id_skill)
            fi = participantSkillForm(instance = participant)
            email = request.POST.get('email')

    return render(request, 'ui-participants_skill.html', {'form': fi, 'email': email})

def participantSkill_list(request):
    context = {'participantSkill_list': participant_skill.objects.all()}
    return render(request, 'ui-view_participant_skill.html', context)

def participantSkill_del(request,  participant_id_skill):
    participant = participant_skill.objects.get(pk= participant_id_skill)
    participant.delete()
    return render(request, '/participantSkill_list')    

def insplacementSkill(request, participant_id_skill=0):
    if request.method == "POST":
        if participant_id_skill == 0:
            form = placement_skillform(request.POST)
        else:
            placement = placement_skillform.objects.get(pk=participant_id_skill)
            form = placement_skillform(request.POST, instance=placement)
            print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Placement Details Added Successfully!')
        return redirect('/insplacementSkill')
    else:
        if participant_id_skill == 0:
            form = placement_skillform()
        else:
            placement = placement_skill.objects.get(pk=participant_id_skill)
            form = placement_skillform(instance=placement)
    return render(request, 'ui-placement_skill.html', {'form': form})

def placementSkill_list(request):
    context = {'placementSkill_list': placement_skill.objects.all()}
    return render(request, 'ui-view_placement_skill.html', context)

def placementSkill_del(request, participant_id_skill):
    print(participant_id_skill)
    placement = placement_skill.objects.get(pk=participant_id_skill)
    placement.delete()
    return render(request, 'ui-view_placement_skill.html')