from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def test(request):
    pass

