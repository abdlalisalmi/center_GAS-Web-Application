from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from handicapped.models import Handicapped
from .models import Card
from .forms import  AddCardForm

@login_required(login_url='/')
def cards(request):
    template_name = 'cards.html'
    context = {}

    finished_card = Card.objects.filter(is_finish=True).order_by('-id')
    waiting_card = Card.objects.filter(is_finish=False).order_by('-id')

    context.update({
        'finished_cards': finished_card,
        'waiting_cards': waiting_card
    })

    return render(request, template_name, context)


@login_required(login_url='/')
def add_card(request):
    template_name = 'add_card.html'
    context = {}

    if request.method == 'POST':
        try:
            id = request.POST.get('id', None)
            handicapped = get_object_or_404(Handicapped, id=id)

            if not Card.objects.filter(handicapped=handicapped).exists():
                Card.objects.create(handicapped=handicapped)
                return JsonResponse({'success':True})
            else:
                return JsonResponse({'success':False, 'message':'هذا الشخص لديه بطاقة أو سبق وتم إضافت طلب له.'})
        except:
            return JsonResponse({'success':False, 'message':'هنالك خطا ما، حاول ورة أخرى'})

    return render(request, template_name, context)


@login_required(login_url='/')
def delete_card(request, id):
    pass