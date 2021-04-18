from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.db.models import Q
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime


from handicapped.models import Handicapped
from food.models import Food
from cards.models import Card
from social_box.models import Device, Project


def home_page(request):
    template_name = 'home_page.html'
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(
                username = username,
                password = password
            )
            if user:
                login_user(request, user)
            else:
                messages.error(request, 'إسم المستخدم أو كلمة المرور  غير صحيحة')
        else:
            messages.error(request, 'الرجاء إدخال اسم المستخدم وكلمة المرور')
    return render(request, template_name, {})


@login_required(login_url='/')
def search(request):
    template_name = 'search.html'
    context = {}

    search = request.GET.get('search', None)
    if search:
        lookups = Q(full_name__contains=search) | Q(
                phone_number__contains=search) | Q(cin__contains=search)
        handicapped_list = Handicapped.objects.filter(lookups)
        handicapped_list = serializers.serialize("json", handicapped_list)
        return HttpResponse(handicapped_list, content_type="application/json")
    else:
        return render(request, template_name, context)
    

@login_required(login_url='/')
def search_folder(request, id):
    template_name = 'search_folder.html'
    context = {}

    handicapped = get_object_or_404(Handicapped, id=id)

    food = Food.objects.filter(handicapped=handicapped).first()
    card = Card.objects.filter(handicapped=handicapped).first()

    project = Project.objects.filter(handicapped=handicapped).first()
    device = Device.objects.filter(handicapped=handicapped).first()


    context.update({
        'handicapped': handicapped,
        'food': food,
        'card': card,
        'project': project,
        'device': device,
    })

    return render(request, template_name, context)
    

@login_required(login_url='/')
def analytics(request):
    template_name = 'analytics.html'
    context = {}

    men = Handicapped.objects.filter(genre='ذكر').count()
    womans = Handicapped.objects.filter(genre='أنثى').count()

    handicappeds = Handicapped.objects.all()
    child, young, old = 0, 0, 0
    today = datetime.date.today()
    handicap_Types = {
        'move': 0,
        'ear': 0,
        'eye': 0,
        'autism': 0,
        'late': 0,
        'trisomy': 0
    }
    for handicapped in handicappeds:
        #get number of each handicap age
        if handicapped.birthday:
            age = today - handicapped.birthday
            if age < datetime.timedelta(days=20*365):
                child += 1
            elif age >= datetime.timedelta(days=20*365) and age < datetime.timedelta(days=40*365):
                young += 1
            else:
                old += 1

        # get number of each handicap taype
        h_type = handicapped.handicap_Type
        if h_type == 'حركية':
            handicap_Types['move'] += 1
        elif h_type == 'بصرية':
            handicap_Types['ear'] += 1
        elif h_type == 'سمعية':
            handicap_Types['eye'] += 1
        elif h_type == 'التوحد':
            handicap_Types['autism'] += 1
        elif h_type == 'التأخر الزمني':
            handicap_Types['late'] += 1
        else:
            handicap_Types['trisomy'] += 1


    has_card = Card.objects.filter(is_finish=True).count()
    waiting_card = Card.objects.filter(is_finish=False).count()

    has_food = Food.objects.filter(is_finish=True, is_deleted=False).count()
    waiting_food = Food.objects.filter(is_finish=False).count()

    # Analytics of peaple in the devices programm
    has_help_devices = Device.objects.filter(device_type='help', is_finish=True).order_by('-id').count()
    waiting_help_devices = Device.objects.filter(device_type='help', is_finish=False).order_by('-id').count()

    has_replace_devices = Device.objects.filter(device_type='replace', is_finish=True).order_by('-id').count()
    waiting_replace_devices = Device.objects.filter(device_type='replace', is_finish=False).order_by('-id').count()

    # Analytics of help projects programm
    local_projects = Project.objects.filter(state=0).count()
    regional_projects = Project.objects.filter(state=1).count()
    central_projects = Project.objects.filter(state=2).count()
    finish_projects = Project.objects.filter(state=3).count()

    context.update({
        'men': men,
        'womans': womans,

        'child': child,
        'young': young,
        'old': old,

        'handicap_Types': handicap_Types,

        'has_card': has_card,
        'waiting_card': waiting_card,

        'has_food': has_food,
        'waiting_food': waiting_food,

        'has_help_devices': has_help_devices,
        'waiting_help_devices': waiting_help_devices,
        'has_replace_devices': has_replace_devices,
        'waiting_replace_devices': waiting_replace_devices,

        'local_projects': local_projects,
        'regional_projects': regional_projects,
        'central_projects': central_projects,
        'finish_projects': finish_projects,
    })
    return render(request, template_name, context)
    