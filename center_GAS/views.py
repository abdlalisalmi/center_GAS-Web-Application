from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.db.models import Q
from django.core import serializers
from django.contrib.auth.decorators import login_required


from handicapped.models import Handicapped
from food.models import Food
from cards.models import Card


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
                messages.success(request, 'لقد تم تسجيل الدخول بنجاح')
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
    food = Food.objects.filter(handicapped=handicapped)
    food = food[0] if food else None
    card = Card.objects.filter(handicapped=handicapped)
    card = card[0] if card else None

    context.update({
        'handicapped': handicapped,
        'food': food,
        'card': card,
    })

    return render(request, template_name, context)
    

@login_required(login_url='/')
def analytics(request):
    template_name = 'analytics.html'
    context = {}

    men = Handicapped.objects.filter(genre='ذكر').count()
    womans = Handicapped.objects.filter(genre='أنثى').count()

    context.update({
        'men': men,
        'womans': womans,
    })
    return render(request, template_name, context)
    