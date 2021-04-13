from django.urls import path
from .views import box, projects, add_project, delete_project, approve_project, devices, delete_device, approve_device

app_name = 'box'
urlpatterns = [
    path('', box, name='box'),

    path('projects/', projects, name='projects'),
    path('projects/add/', add_project, name='add_project'),
    path('projects/delete/<int:id>/', delete_project, name='delete_project'),
    path('projects/approve/<int:id>/', approve_project, name='approve_project'),

    path('devices/', devices, name='devices'),
    path('devices/delete/<int:id>/', delete_device, name='delete_device'),
    path('devices/approve/<int:id>/', approve_device, name='approve_device'),
]