from django.urls import path
from .views import (
        box,

        education,
        association,
        add_association,
        delete_association,

        projects, 
        add_project, 
        delete_project, 
        approve_project,

        devices, 
        add_device,
        delete_device, 
        approve_device,
    )

app_name = 'box'
urlpatterns = [
    path('', box, name='box'),

    path('education/', education, name='education'),
    path('education/association/add', add_association, name='add_association'),
    path('education/association/<int:id>/', association, name='association'),
    path('education/association/delete/<int:id>/', delete_association, name='delete_association'),

    path('projects/', projects, name='projects'),
    path('projects/add/', add_project, name='add_project'),
    path('projects/delete/<int:id>/', delete_project, name='delete_project'),
    path('projects/approve/<int:id>/', approve_project, name='approve_project'),

    path('devices/', devices, name='devices'),
    path('devices/add/', add_device, name='add_device'),
    path('devices/delete/<int:id>/', delete_device, name='delete_device'),
    path('devices/approve/<int:id>/', approve_device, name='approve_device'),
]