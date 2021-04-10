from django.urls import path
from.views import add_handicapped, handicapped_list, delete_handicapped, update_handicapped

app_name = 'handicapped'
urlpatterns = [
    path('', handicapped_list, name='handicapped_list'),
    path('add/', add_handicapped, name='add_handicapped'),
    path('delete/<str:id>/', delete_handicapped, name='delete_handicapped'),
    path('update/<int:id>/', update_handicapped, name='update_handicapped')

]