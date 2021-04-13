from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from social_box.models import Project
from handicapped.models import Handicapped

@login_required(login_url='/')
def box(request):
    template_name = "box.html"
    context = {}

    return render(request, template_name, context)


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