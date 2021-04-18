from django.shortcuts import render, get_object_or_404

import xlwt

from django.http import HttpResponse
from handicapped.models import Handicapped

def export_handicapped_csv(request, id=None):

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