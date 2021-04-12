from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def box(request):
    template_name = "box.html"
    context = {}

    return render(request, template_name, context)

