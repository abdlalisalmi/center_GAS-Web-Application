from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
import datetime
from social_box.models import AssociationHr, Project, ProjectVisit, Device, Association, AssociationHistory
from handicapped.models import Handicapped
from .forms import AssociationCreateForm, AddHRForm, AddStudentForm, AddHistoryForm, AddProjectVisitForm

@login_required(login_url='/')
def box(request):
    template_name = "box.html"
    context = {}

    return render(request, template_name, context)

#################################################################################
################################### education ###################################
#################################################################################
@login_required(login_url='/')
def education(request):
    template_name = "education.html"
    context = {}
    if request.GET.get('deleted', None):
        associations = Association.objects.filter(is_deleted=True).order_by('-id')
        context.update({'deleted':True})
    else:
        associations = Association.objects.filter(is_deleted=False).order_by('-id')
    context.update({
        'associations': associations,
    })
    return render(request, template_name, context)

################# Association #####################
@login_required(login_url='/')
def association(request, id):
    template_name = "association.html"
    context = {}

    ass = get_object_or_404(Association, id=id)
    hrs = AssociationHr.objects.filter(association=ass).order_by('-id')
    hr_count = AssociationHr.objects.filter(association=ass).count()

    students = Handicapped.objects.filter(association=id, is_deleted=False).order_by('-id')
    present_students_count = Handicapped.objects.filter(association=id, is_deleted=False).count()

    deleted_students = Handicapped.objects.filter(association=id, is_deleted=True).order_by('-id')
    deleted_students_count = Handicapped.objects.filter(association=id, is_deleted=True).count()

    histories = AssociationHistory.objects.all().order_by('-year')

    context.update({
        'ass': ass,
        'hrs': hrs,
        'hr_count': hr_count,
        'present_students': students,
        'present_students_count': present_students_count,
        'deleted_students': deleted_students,
        'deleted_students_count': deleted_students_count,
        'histories': histories
        })
    return render(request, template_name, context)

@login_required(login_url='/')
def add_association(request):
    if request.method == 'POST':
        form = AssociationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '?????? ???? ?????????? ??????????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        
    return redirect('box:education')

@login_required(login_url='/')
def update_association(request, id):
    if request.method == 'POST':
        ass = get_object_or_404(Association, id=id)
        form = AssociationCreateForm(instance=ass, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '?????? ???? ?????????? ?????????????? ??????????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':ass.id}))
    return redirect('box:education')
    

@login_required(login_url='/')
def delete_association(request, id):
    if request.method == 'POST':
        ass = get_object_or_404(Association, id=id)
        ass.is_deleted = not ass.is_deleted
        ass.save()
        messages.success(request, '?????? ?????? ?????????????? ??????????')
    return redirect('box:education')

################# Association HR #####################
login_required(login_url='/')
def add_hr(request):
    if request.method == 'POST':
        form = AddHRForm(request.POST)
        if form.is_valid():
            hr = form.save(commit=False)
            if hr.month_salary:
                hr.year_salary = hr.month_salary * 11
            hr.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')


login_required(login_url='/')
def update_hr(request, id):
    if request.method == 'POST':
        hr = get_object_or_404(AssociationHr, id=id)
        form = AddHRForm(instance=hr, data=request.POST)
        if form.is_valid():
            hr = form.save(commit=False)
            if hr.month_salary:
                hr.year_salary = hr.month_salary * 11
            hr.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')


login_required(login_url='/')
def delete_hr(request, id):
    if request.method == 'POST':
        try:
            hr = get_object_or_404(AssociationHr, id=id)
            hr.delete()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        except:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')


################# Association Students #####################

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        else:
            print(form.errors)
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')

def update_student(request, id):
    if request.method == 'POST':
        student = get_object_or_404(AssociationStudent, id=id)
        form = AddStudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')

login_required(login_url='/')
def delete_student(request, id):
    if request.method == 'POST':
        try:
            student = get_object_or_404(Handicapped, id=id)
            student.is_deleted = not student.is_deleted
            student.deleted_date = datetime.date.today()
            student.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        except:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')

################# Association History #####################

def add_history(request):
    if request.method == 'POST':
        form = AddHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        else:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
            print(form.errors)
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')

login_required(login_url='/')
def delete_history(request, id):
    if request.method == 'POST':
        try:
            history = get_object_or_404(AssociationHistory, id=id)
            history.delete()
            messages.success(request, '?????? ?????? ?????????????? ??????????')
        except:
            messages.success(request, '?????????? ?????? ???? ???????? ?????? ????????')
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':request.POST.get('association')}))
    return redirect('box:education')

#################################################################################
############################### help the projects ###############################
#################################################################################
@login_required(login_url='/')
def projects(request):
    template_name = "projects/projects.html"
    context = {}

    local_projects = Project.objects.filter(state=0).order_by('-id')
    regional_projects = Project.objects.filter(state=1).order_by('-id')
    central_projects = Project.objects.filter(state=2).order_by('-id')
    finish_projects = Project.objects.filter(state=3).order_by('-id')

    context.update({
        'local_projects': local_projects,
        'regional_projects': regional_projects,
        'central_projects': central_projects,
        'finish_projects': finish_projects,
    })
    return render(request, template_name, context)


@login_required(login_url='/')
def add_project(request):
    template_name = "projects/add_project.html"
    context = {}

    if request.method == 'POST':
        try:
            id = request.POST.get('id', None)

            handicapped = get_object_or_404(Handicapped, id=id)

            if not Project.objects.filter(handicapped=handicapped).exists():
                description = request.POST.get('description', None)
                budget = request.POST.get('budget', None) if len(request.POST.get('budget', None)) > 0 else 0
                notes = request.POST.get('notes', None)
                
                Project.objects.create(
                    handicapped=handicapped,
                    description=description,
                    budget=budget,
                    notes=notes
                )
                return JsonResponse({'success':True})
            else:
                return JsonResponse({'success':False, 'message':'?????? ?????????? ???????? ???? ?????????? ????????????????.'})
        except:
            return JsonResponse({'success':False, 'message':'?????????? ?????? ?????? ???????? ?????? ????????'})

    return render(request, template_name, context)


@login_required(login_url='/')
def delete_project(request, id):
    try:
        Project.objects.get(id=id).delete()
        messages.success(request, '?????? ???? ?????? ??????????????')
    except:
        messages.success(request, '?????????? ?????? ?????? ???????? ?????? ????????')

    return redirect('box:projects')


@login_required(login_url='/')
def approve_project(request, id):
    try:
        project = Project.objects.get(id=id)
        if project.state < 3:
            project.state += 1
            if project.state == 3:
                project.approving_date = datetime.date.today()
            project.save()
        messages.success(request, '?????? ???? ???????????????? ?????? ??????????????')
    except:
        messages.success(request, '?????????? ?????? ?????? ???????? ?????? ????????')

    return redirect('box:projects')


############### Project Visits ###################

@login_required(login_url='/')
def get_project_visits(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id', None)
        if project_id:
            visits = ProjectVisit.objects.filter(project=project_id)
            visits = serializers.serialize("json", visits)
            return HttpResponse(visits, content_type="application/json")
    
    return HttpResponseRedirect(reverse('box:education'))

@login_required(login_url='/')
def add_project_visit(request):
    if request.method == 'POST':
        form = AddProjectVisitForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('box:projects'))       


#################################################################################
#################################### devices ####################################
#################################################################################

@login_required(login_url='/')
def devices(request):
    template_name = "devices/devices.html"
    context = {}

    has_help_devices = Device.objects.filter(device_type='help', is_finish=True).order_by('-id')
    waiting_help_devices = Device.objects.filter(device_type='help', is_finish=False).order_by('-id')

    has_replace_devices = Device.objects.filter(device_type='replace', is_finish=True).order_by('-id')
    waiting_replace_devices = Device.objects.filter(device_type='replace', is_finish=False).order_by('-id')

    context.update({
        'has_help_devices': has_help_devices,
        'waiting_help_devices': waiting_help_devices,
        'has_replace_devices': has_replace_devices,
        'waiting_replace_devices': waiting_replace_devices
    })
    return render(request, template_name, context)


@login_required(login_url='/')
def add_device(request):
    template_name = 'devices/add_device.html'
    context = {}

    if request.method == 'POST':
        try:
            id = request.POST.get('id', None)
            handicapped = get_object_or_404(Handicapped, id=id)

            if not Device.objects.filter(handicapped=handicapped).exists():
                Device.objects.create(
                    handicapped=handicapped,
                    device_name=request.POST.get('deviceName'),
                    device_type=request.POST.get('deviceType')
                    )
                return JsonResponse({'success':True})
            else:
                return JsonResponse({'success':False, 'message':'?????? ?????????? ???????????? ???? ?????? ???????????? ?????? ?????????? ????????????????'})
        except:
            return JsonResponse({'success':False, 'message':'?????????? ?????? ?????? ???????? ?????? ????????'})

    return render(request, template_name, context)


@login_required(login_url='/')
def delete_device(request, id):
    try:
        Device.objects.get(id=id).delete()
        messages.success(request, '?????? ???? ?????? ??????????')
    except:
        messages.success(request, '?????????? ?????? ?????? ???????? ?????? ????????')

    return redirect('box:devices')


@login_required(login_url='/')
def approve_device(request, id):
    try:
        device = Device.objects.get(id=id)
        device.is_finish = True
        device.approving_date = datetime.date.today()
        device.save()
        messages.success(request, '?????? ???? ???????????????? ?????? ??????????')
    except:
        messages.success(request, '?????????? ?????? ?????? ???????? ?????? ????????')

    return redirect('box:devices')