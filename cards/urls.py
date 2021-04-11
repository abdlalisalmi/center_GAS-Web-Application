from django.urls import path
from.views import cards, add_card, delete_card, approve_card

app_name = 'cards'
urlpatterns = [
    path('', cards, name='cards'),
    path('add/', add_card, name='add_card'),
    path('delete/<int:id>/', delete_card, name='delete_card'),
    path('approve/<int:id>/', approve_card, name='approve_card'),
]