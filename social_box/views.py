from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
import datetime
from social_box.models import Project, Device, Association
from handicapped.models import Handicapped
from .forms import AssociationCreateForm

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
    associations = Association.objects.all().order_by('-id')
    context.update({
        'associations': associations
    })
    return render(request, template_name, context)


@login_required(login_url='/')
def association(request, id):
    template_name = "association.html"
    context = {}

    ass = get_object_or_404(Association, id=id)
    context.update({'ass': ass})
    return render(request, template_name, context)

@login_required(login_url='/')
def add_association(request):
    if request.method == 'POST':
        form = AssociationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'لقد تم إضافة الجمعية')
        else:
            messages.success(request, 'هنالك خطأ ما حاول مرة أخرى')
        
    return redirect('box:education')

@login_required(login_url='/')
def update_association(request, id):
    if request.method == 'POST':
        ass = get_object_or_404(Association, id=id)
        form = AssociationCreateForm(instance=ass, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'لقد تم تعديل معلومات الجمعية')
        else:
            messages.success(request, 'هنالك خطأ ما حاول مرة أخرى')
        
        return HttpResponseRedirect(reverse('box:association', kwargs={'id':ass.id}))
    return redirect('box:education')
    

@login_required(login_url='/')
def delete_association(request, id):
    if request.method == 'POST':
        ass = get_object_or_404(Association, id=id)
        ass.delete()
        messages.success(request, 'لقد تم حذف الجمعية')
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
                return JsonResponse({'success':False, 'message':'هذا الشخص مسجل في لائحة المشاريع.'})
        except:
            return JsonResponse({'success':False, 'message':'هنالك خطا ما، حاول ورة أخرى'})

    return render(request, template_name, context)


@login_required(login_url='/')
def delete_project(request, id):
    try:
        Project.objects.get(id=id).delete()
        messages.success(request, 'لقد تم حدف المشروع')
    except:
        messages.success(request, 'هنالك خطا ما، حاول ورة أخرى')

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
        messages.success(request, 'لقد تم الموافقة على المشروع')
    except:
        messages.success(request, 'هنالك خطا ما، حاول ورة أخرى')

    return redirect('box:projects')



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
                return JsonResponse({'success':False, 'message':'هذا الشخص مستفيد أو تمت اضافته إلى قائمة الإنتضار'})
        except:
            return JsonResponse({'success':False, 'message':'هنالك خطا ما، حاول ورة أخرى'})

    return render(request, template_name, context)


@login_required(login_url='/')
def delete_device(request, id):
    try:
        Device.objects.get(id=id).delete()
        messages.success(request, 'لقد تم حدف الطلب')
    except:
        messages.success(request, 'هنالك خطا ما، حاول ورة أخرى')

    return redirect('box:devices')


@login_required(login_url='/')
def approve_device(request, id):
    try:
        device = Device.objects.get(id=id)
        device.is_finish = True
        device.approving_date = datetime.date.today()
        device.save()
        messages.success(request, 'لقد تم الموافقة على الطلب')
    except:
        messages.success(request, 'هنالك خطا ما، حاول ورة أخرى')

    return redirect('box:devices')