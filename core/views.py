from core.forms import program_entreform, program_skillform, participantForm, participantSkillForm, placement_skillform
from core.models import dept_entre, dept_skill, program_entre, program_skill, participant_entre, participant_skill, placement_skill
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib import messages
from .filters import program_skillFilter, department_skillFilter, particpant_skillFilter,placement_skillFilter,program_ENTFilter,department_ENTFilter, particpant_ENTFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url="/login/")
def index(request):
    count_entre = participant_entre.objects.count()
    print(count_entre)
    count_skill = participant_skill.objects.count()
    print(count_skill)
    return render(request, "index.html", {'count_entre': count_entre, 'count_skill' : count_skill})


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
    myFilter = department_ENTFilter(request.GET, queryset=dept_entre.objects.all())
    return render(request, 'ui-view_department_ent.html',{'filter' : myFilter})

def deptSkill(request):
    myFilter = department_skillFilter(request.GET, queryset= dept_skill.objects.all())
    # user_list = dept_skill.objects.all()
    # myFilter = department_skillFilter(request.GET, queryset= user_list)
    # user_list = department_skillFilter.qs
    # paginator = Paginator(user_list, 10)
    # page = request.GET.get('page', 1)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)
    # args = {'paginator': paginator,'filter':myFilter, 'users':users,}
    # return render(request, 'ui-view_department_skill.html', args)
    return render(request, 'ui-view_department_skill.html',{'filter' : myFilter})

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
    myFilter = program_ENTFilter(request.GET, queryset=program_entre.objects.all())
    context = {'filter': myFilter}
    return render(request, 'ui-view_program_ent.html', context)


def pm_del(request, id):
    program = program_entre.objects.get(pk=id)
    program.delete()
    return redirect('/program_list')


def insprogSkill(request, id=0):
    messages = None
    if request.method == "POST":
        if id == 0:
            form = program_skillform(request.POST)
        else:
            program = program_skill.objects.get(pk=id)
            form = program_skillform(request.POST, instance=program)
            print(form)
        if form.is_valid():
            form.save()
            messages = 'Program Added Successfully!'
        # return redirect('/insprogSkill')
    else:
        if id == 0:
            form = program_skillform()
        else:
            program = program_skill.objects.get(pk=id)
            form = program_skillform(instance=program)
    return render(request, 'ui-program_skill.html', {'form': form, 'msg': messages})


def programSkill_list(request):
    myFilter = program_skillFilter(request.GET, queryset=program_skill.objects.all())
    return render(request, 'ui-view_program_skill.html',  {'filter': myFilter})

def programSkill_del(request, id):
    program = program_skill.objects.get(pk=id)
    program.delete()
    return redirect('/programSkill_list')

def participant_ent(request, participant_id_ent=0):
    if request.method == "POST":
        if participant_id_ent == 0:
            fi = participantForm(request.POST)
            email = request.POST.get('email')
        else:
            participant = participant_entre.objects.get(pk=participant_id_ent)
            print("particpant:", participant)
            fi = participantForm(request.POST, instance=participant)
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
            participant = participant_entre.objects.get(pk=participant_id_ent)
            fi = participantForm(instance=participant)
            email = request.POST.get('email')

    return render(request, 'ui-participants_ent.html', {'form': fi, 'email': email})


def participant_list(request):
    filter = particpant_ENTFilter(request.GET, queryset=participant_entre.objects.all())
    context = {'filter': filter}
    return render(request, 'ui-view_participant_ent.html', context)


def participant_del(request, participant_id_ent):
    participant = participant_entre.objects.get(pk=participant_id_ent)
    participant.delete()
    return redirect('/participant_list') 


def insparticipant_skill(request, participant_id_skill=0):
    messages = None
    if request.method == "POST":
        if participant_id_skill == 0:
            fi = participantSkillForm(request.POST)
            email = request.POST.get('email')
        else:
            participant = participant_skill.objects.get(pk=participant_id_skill)
            fi = participantSkillForm(request.POST, instance=participant)
            email = request.POST.get('email')
            print("email: ", email)
        if fi.is_valid():
            fi.save()
            # messages.success(request, 'Program Added Successfully!')
            messages = 'Participant Details Added Successfully!'
            # return redirect('/insparticipant_skill')
    else:
        if participant_id_skill == 0:
            fi = participantSkillForm()
            email = request.POST.get('email')
        else:
            participant = participant_skill.objects.get(pk=participant_id_skill)
            fi = participantSkillForm(instance=participant)
            email = request.POST.get('email')
    return render(request, 'ui-participants_skill.html', {'form': fi, 'email': email, 'msg':messages})


def participantSkill_list(request):
    filter = particpant_skillFilter(request.GET, queryset=participant_skill.objects.all())
    context = {'filter': filter}
    return render(request, 'ui-view_participant_skill.html', context)


def participantSkill_del(request, participant_id_skill):
    participant = participant_skill.objects.get(pk=participant_id_skill)
    participant.delete()
    return redirect('/participantSkill_list')


def insplacementSkill(request, participant_id_skill=0):
    messages = None
    if request.method == "POST":
        print("insert")
        if participant_id_skill == 0:
            form = placement_skillform(request.POST)
        else:
            placement = placement_skill.objects.get(pk=participant_id_skill)
            form = placement_skillform(request.POST, instance=placement)
        if form.is_valid():
            form.save()
            messages = 'Placement Details Added Successfully!'
        # return redirect('/insplacementSkill')
        # return render(request, 'ui-placement_skill.html', {'form': form, 'msg': messages})
    else:
        print("update")
        if participant_id_skill == 0:
            form = placement_skillform()
        else:
            placement = placement_skill.objects.get(pk=participant_id_skill)
            form = placement_skillform(instance=placement)
            # messages = "Placement Details Updated Successfully!"
    return render(request, 'ui-placement_skill.html', {'form': form, 'msg' : messages})


def placementSkill_list(request):
    filter = placement_skillFilter(request.GET, queryset= placement_skill.objects.all())
    context = {'filter': filter}
    return render(request, 'ui-view_placement_skill.html', context)


def placementSkill_del(request, participant_id_skill):
    print(participant_id_skill)
    placement = placement_skill.objects.get(pk=participant_id_skill)
    placement.delete()
    return redirect('/placementSkill_list')


