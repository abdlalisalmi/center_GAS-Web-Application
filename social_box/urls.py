from django.urls import path
from .views import box

app_name = 'box'
urlpatterns = [
    path('', box, name='box'),
]