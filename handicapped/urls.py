from django.urls import path
from django.urls.resolvers import URLPattern
from.views import add_handicapped, handicapped_list

app_name = 'handicapped'
urlpatterns = [
    path('', handicapped_list, name='handicapped_list'),
    path('add/', add_handicapped, name='add_handicapped')
]