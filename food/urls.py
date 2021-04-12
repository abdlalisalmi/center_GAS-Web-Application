from django.urls import path

from .views import food_list, add_food, delete_food, restore_delete_food, approve_food


app_name='food'
urlpatterns = [
    path('', food_list, name='food_list'),
    path('add/', add_food, name='add_food'),
    path('delete/<int:id>/', delete_food, name='delete_food'),
    path('restore/<int:id>/', restore_delete_food, name='restore_delete_food'),
    path('approve/<int:id>/', approve_food, name='approve_food'),
]
