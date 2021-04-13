from django.urls import path
from .views import box, projects, add_project, delete_project, approve_project

app_name = 'box'
urlpatterns = [
    path('', box, name='box'),

    path('projects/', projects, name='projects'),
    path('projects/add/', add_project, name='add_project'),
    path('projects/delete/<int:id>/', delete_project, name='delete_project'),
    path('projects/approve/<int:id>/', approve_project, name='approve_project'),
]