from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def handicapped_list(request):
    template_name = 'handicapped_list.html'
    return render(request, template_name, {})


@login_required(login_url='/')
def add_handicapped(request):
    template_name = 'add_handicapped.html'
    return render(request, template_name, {})