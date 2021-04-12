from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

from .models import Food
from handicapped.models import Handicapped


@login_required(login_url='/')
def food_list(request):
    template_name='food_list.html'
    context = {}
    if request.GET.get('deleted', None):
        deleted_food = Food.objects.filter(is_finish=True, is_deleted=True).order_by('-id')
        return render(request, template_name, {'deleted_food':deleted_food, 'deleted':True})
    finished_food = Food.objects.filter(is_finish=True, is_deleted=False).order_by('-id')
    waiting_food = Food.objects.filter(is_finish=False).order_by('-id')

    context.update({
        'finished_food': finished_food,
        'waiting_food': waiting_food,
    })

    return render(request, template_name, context)


@login_required(login_url='/')
def add_food(request):
    template_name='add_food.html'
    context = {}
    if request.method == 'POST':
        try:
            id = request.POST.get('id', None)
            handicapped = get_object_or_404(Handicapped, id=id)

            if not Food.objects.filter(handicapped=handicapped).exists():
                Food.objects.create(handicapped=handicapped)
                return JsonResponse({'success':True})
            else:
                return JsonResponse({'success':False, 'message':'هذا الشخص مستفيد أو تمت اضافته إلى قائمة الإنتضار'})
        except:
            return JsonResponse({'success':False, 'message':'هنالك خطا ما، حاول ورة أخرى'})
    return render(request, template_name, context)


@login_required(login_url='/')
def delete_food(request, id):
    if request.method == 'POST':
        try:
            food = get_object_or_404(Food, id=id)
            approved = food.is_finish
            if food.is_finish and not food.is_deleted:
                messages.success(request, 'لقد تم حدف المستفيد')
                food.is_deleted = not food.is_deleted
                food.delete_description = request.POST.get('delete_description', '')
                food.save()
            else:
                food.delete()
                messages.success(request, 'لقد تم حدف المستفيد')
            if not approved:
                return redirect('food:food_list')
            else:
                context = {}
                finished_food = Food.objects.filter(is_finish=True, is_deleted=False).order_by('-id')
                waiting_food = Food.objects.filter(is_finish=False).order_by('-id')

                context.update({
                    'finished_food': finished_food,
                    'waiting_food': waiting_food,
                    'approved':approved
                })
                return render(request, 'food_list.html', context)
        except:
            messages.success(request, 'حدت خطأ ما أتناء حدف المستفيد')
    return redirect('food:food_list')


@login_required(login_url='/')
def restore_delete_food(request, id):
    if request.method == 'POST':
        try:
            food = get_object_or_404(Food, id=id)
            messages.success(request, 'لقد تم إستعادة المستفيد')
            food.is_deleted = False
            food.delete_description = request.POST.get('delete_description', '')
            food.save()
        except:
            messages.success(request, 'حدت خطأ ما أتناء إستعادة المستفيد')
    return redirect('food:food_list')


@login_required(login_url='/')
def approve_food(request, id):
    if request.method == 'POST':
        try:
            food = get_object_or_404(Food, id=id)
            messages.success(request, 'لقد تم قبول المستفيد')
            food.is_finish = True
            food.save()
        except:
            messages.success(request, 'حدت خطأ ما أتناء قبول المستفيد')
    return redirect('food:food_list')