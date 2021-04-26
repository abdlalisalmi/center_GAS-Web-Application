from django.shortcuts import render, get_object_or_404

import xlwt

from django.http import HttpResponse
from handicapped.models import Handicapped
from cards.models import Card
from food.models import Food

def export_handicapped_excel(request, id=None):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
                'الإسم الكامل',
                'العنوان',
                'رقم الهاتف',
                'رقم البطاقة الوطنية', 
                'الجنس', 
                'مكان الإزدياد', 
                'تاريخ الإزدياد', 
                'المجال',
                'ولي الأمر',
                'نوع الإعاقة',
            ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    if not id == 'None':
        handicappeds = Handicapped.objects.filter(id=id)
    else:
        handicappeds = Handicapped.objects.all()

    handicappeds = handicappeds.values_list('full_name', 'address', 'phone_number', 
                                                        'cin', 'genre', 'birth_address', 
                                                        'birthday', 'zone', 'guardian', 'handicap_Type',)

    for hand in handicappeds:
        row_num += 1
        for col_num in range(len(hand)):
            ws.write(row_num, col_num, hand[col_num], font_style)

    wb.save(response)
    return response


def export_food_card_list_excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
                'صاحب الطلب',
                'نوع الإعاقة',
            ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    data = ''
    if request.GET.get('f_card'):
        data = Card.objects.filter(is_finish=True).order_by('-finishing_date').values('handicapped__full_name', 'handicapped__handicap_Type',)
    elif request.GET.get('w_card'):
        data = Card.objects.filter(is_finish=False).order_by('-finishing_date').values('handicapped__full_name', 'handicapped__handicap_Type',)
    elif request.GET.get('f_food'):
        data = Food.objects.filter(is_finish=True).order_by('-finishing_date').values('handicapped__full_name', 'handicapped__handicap_Type',)
    elif request.GET.get('w_food'):
        data = Food.objects.filter(is_finish=False).order_by('-finishing_date').values('handicapped__full_name', 'handicapped__handicap_Type',)

    # data = data.values_list('handicapped__full_name', 'handicapped__handicap_Type',)

    for field in data:
        row_num += 1
        for col_num, key in zip(range(len(field)), field.keys()):
            ws.write(row_num, col_num, field[key], font_style)

    wb.save(response)
    return response