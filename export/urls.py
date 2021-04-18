from django.urls import path
from .views import export_handicapped_csv


app_name = 'export'
urlpatterns = [
    path("handicapped/<str:id>/", export_handicapped_csv, name="export_handicapped_csv")
]