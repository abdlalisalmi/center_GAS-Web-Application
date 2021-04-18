from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, search, search_folder, analytics


urlpatterns = [
    path('', home_page, name="home_page"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('analytics/', analytics, name="analytics"),
    path('search/', search, name="search"),
    path('search/<int:id>/', search_folder, name="search_folder"),

    path('handicapped/', include('handicapped.urls')),

    path('cards/', include('cards.urls')),
    
    path('food/', include('food.urls')),

    path('box/', include('social_box.urls')),

    path('export/', include('export.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
