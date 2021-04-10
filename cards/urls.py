from django.urls import path
from.views import cards, add_card

app_name = 'cards'
urlpatterns = [
    path('', cards, name='cards'),
    path('add/', add_card, name='add_card'),
]