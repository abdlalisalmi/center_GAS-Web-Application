from django.urls import path
from .views import export_handicapped_excel, export_food_card_list_excel


app_name = 'export'
urlpatterns = [
    path("handicapped/<str:id>/", export_handicapped_excel, name="export_handicapped_excel"),
    path("card_food_list/", export_food_card_list_excel, name="export_food_card_list_excel"),
]