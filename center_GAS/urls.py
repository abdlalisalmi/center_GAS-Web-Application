from django.contrib import admin
from django.urls import path, include

from .views import home_page, search, search_folder, analytics


urlpatterns = [
    path('', home_page, name="home_page"),
    path('analytics/', analytics, name="analytics"),
    path('search/', search, name="search"),
    path('search/<int:id>/', search_folder, name="search_folder"),

    path('handicapped/', include('handicapped.urls')),

    path('cards/', include('cards.urls')),
    
    path('food/', include('food.urls')),

    path('box/', include('social_box.urls')),

    path('admin/', admin.site.urls),
]
