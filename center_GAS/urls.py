from django.contrib import admin
from django.urls import path, include

from .views import home_page


urlpatterns = [
    path('', home_page, name="home_page"),
    path('handicapped/', include('handicapped.urls')),
    path('admin/', admin.site.urls),
]
