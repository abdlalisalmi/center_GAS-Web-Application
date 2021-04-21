from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import HandicappedForm
from .models import Handicapped

from food.models import Food
from cards.models import Card


@login_required(login_url='/')
def handicapped_list(request):
    template_name = 'handicapped_list.html'
    context = {}

    if request.GET.get('deleted', None):
        handicapped_list = Handicapped.objects.filter(is_deleted=True).order_by('-id')
        context.update({
            'handicapped_list': handicapped_list,
            'deleted':True
            })
    else:
        handicapped_list = Handicapped.objects.filter(is_deleted=False).order_by('-id')
        context.update({'handicapped_list': handicapped_list})

    return render(request, template_name, context)


@login_required(login_url='/')
def add_handicapped(request):
    template_name = 'add_handicapped.html'
    context = {}

    if request.method == 'POST':
        form = HandicappedForm(request.POST)
        if form.is_valid():
            handicap = form.save()

            if request.POST.get('f_card'):
                card = Card.objects.create(handicapped=handicap)
                card.is_finish = True
                card.save()
            elif request.POST.get('w_card'):
                card = Card.objects.create(handicapped=handicap)
            
            if request.POST.get('f_food'):
                food = Food.objects.create(handicapped=handicap)
                food.is_finish = True
                food.save()
            elif request.POST.get('w_food'):
                food = Food.objects.create(handicapped=handicap)

            return redirect('handicapped:handicapped_list')
        else:
            return render(request, template_name, {'form': form})

    form = HandicappedForm()
    
    context['form']= form
    return render(request, template_name, context)


@login_required(login_url='/')
def delete_handicapped(request, id):
    try:
        id = int(id)
        delete_description = request.POST.get('delete_description', None)
        handicapped = Handicapped.objects.get(id=id)
        if handicapped:
            handicapped.is_deleted = not handicapped.is_deleted
            handicapped.delete_description = delete_description
            handicapped.save()
    except:
        pass
    return redirect('handicapped:handicapped_list')


@login_required(login_url='/')
def update_handicapped(request, id):
    template_name = 'update_handicapped.html'
    context = {}

    handicapped = get_object_or_404(Handicapped, id=id)

    if request.method == 'POST':
        form = HandicappedForm(instance=handicapped, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('handicapped:handicapped_list')
        else:
            return render(request, template_name, {'form': form})
    context['handicapped']= handicapped
    return render(request, template_name, context)