
from core.forms import program_entreform, participantForm
from core.models import dept_entre, program_entre, participant_entre
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
    context = {'deptEnt': dept_entre.objects.all()}
    return render(request, 'ui-view_department_ent.html', context)


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
    # print(id)
    program = program_entre.objects.get(pk=id)
    program.delete()
    return render(request, '/program_list')


def participant_list(request):
    context = {'participant_list': participant_entre.objects.all()}
    return render(request, 'ui-view_participant_ent.html', context)


def participant_del(request,  participant_id_ent):
    program = participant_entre.objects.get(pk= participant_id_ent)
    program.delete()
    return render(request, '/participant_list')
