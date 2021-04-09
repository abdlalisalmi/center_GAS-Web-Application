from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user


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

