from django.contrib import admin
from django.urls import path, include

from .views import home_page, search


urlpatterns = [
    path('', home_page, name="home_page"),
    path('search/', search, name="search"),
    path('handicapped/', include('handicapped.urls')),
    path('cards/', include('cards.urls')),
    path('admin/', admin.site.urls),
]
