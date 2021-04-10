from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Card
from .forms import  AddCardForm

@login_required(login_url='/')
def cards(request):
    template_name = 'cards.html'
    context = {}

    # handicapped = get_object_or_404(Handicapped, id=id)

    # if request.method == 'POST':
    #     form = HandicappedForm(instance=handicapped, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('handicapped:handicapped_list')
    #     else:
    #         return render(request, template_name, {'form': form})
    # context['handicapped']= handicapped
    return render(request, template_name, context)


@login_required(login_url='/')
def add_card(request):
    template_name = 'add_card.html'
    context = {}

    if request.method == 'POST':
        pass
    form = AddCardForm()
    return render(request, template_name, context)