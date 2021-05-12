from core.forms import program_entreform, participantForm
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
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def deptSkill(request):
    return render(request, 'ui-department_skill.html')


def deptEnt(request):
    return render(request, 'ui-department_ent.html')


def participant_ent(request, participant_id_ent=0):
    if request.method == "POST":
        if participant_id_ent == 0:
            form = participantForm(request.POST)
            print(form)
        else:
            participant = participantForm.objects.get(pk = participant_id_ent)
            form = participantForm(request.POST, instance = participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program Added Successfully!')
        return redirect('/insertparticipant')
    else:
        if participant_id_ent == 0:
            form = participantForm()
        else:
            participant = participantForm.objects.get(pk = participant_id_ent)
            form = participantForm(instance = participant)
    return render(request, 'ui-participants_ent.html', {'form': form})


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
    print(id)
    program = program_entre.objects.get(pk=id)
    program.delete()
    return render(request, 'ui-view_program_ent.html')


def participant_list(request):
    context = {'participant_list': participantForm.objects.all()}
    return render(request, 'ui-view_program_ent.html', context)


def participant_del(request, id):
    program = participantForm.objects.get(pk=id)
    program.delete()
    return render(request, 'ui-view_participant_ent.html')
