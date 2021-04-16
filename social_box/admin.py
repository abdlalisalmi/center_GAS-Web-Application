from django.contrib import admin
from .models import Project, Device, Association, AssociationHr, AssociationStudent, AssociationHistory
# Register your models here.
admin.site.register(Project)
admin.site.register(Device)
admin.site.register(Association)
admin.site.register(AssociationHistory)
admin.site.register(AssociationHr)
admin.site.register(AssociationStudent)