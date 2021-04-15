from django.contrib import admin
from .models import Project, Device, Association
# Register your models here.
admin.site.register(Project)
admin.site.register(Device)
admin.site.register(Association)