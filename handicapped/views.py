from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HandicappedForm
from .models import Handicapped


@login_required(login_url='/')
def handicapped_list(request):
    template_name = 'handicapped_list.html'
    handicapped_list = Handicapped.objects.all().order_by('-id')
    return render(request, template_name, {'handicapped_list': handicapped_list})


@login_required(login_url='/')
def add_handicapped(request):
    template_name = 'add_handicapped.html'
    context = {}

    if request.method == 'POST':
        form = HandicappedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('handicapped:handicapped_list')
        else:
            return render(request, template_name, {'form': form})

    form = HandicappedForm()
    
    context['form']= form
    return render(request, template_name, context)