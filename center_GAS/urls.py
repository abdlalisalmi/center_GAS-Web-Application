from django.contrib import admin
from django.urls import path, include

from .views import home_page, search, search_folder


urlpatterns = [
    path('', home_page, name="home_page"),
    path('search/', search, name="search"),
    path('search/<int:id>/', search_folder, name="search_folder"),

    path('handicapped/', include('handicapped.urls')),

    path('cards/', include('cards.urls')),
    
    path('food/', include('food.urls')),

    path('admin/', admin.site.urls),
]
