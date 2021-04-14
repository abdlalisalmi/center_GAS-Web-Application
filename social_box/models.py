from django.db import models
from handicapped.models import Handicapped




class Project(models.Model):
    handicapped     = models.OneToOneField(Handicapped, on_delete=models.CASCADE)
    description     = models.TextField(null=True, blank=True)
    notes           = models.TextField(null=True, blank=True)
    budget          = models.DecimalField(max_digits=20,  decimal_places=2, null=True, blank=True)
    submiting_date  = models.DateField(auto_now=False, auto_now_add=True)
    approving_date  = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    state           = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.handicapped.full_name


class Device(models.Model):
    handicapped     = models.OneToOneField(Handicapped, on_delete=models.CASCADE)
    device_type     = models.CharField(max_length=100, null=True, blank=True)
    device_name     = models.TextField(null=True, blank=True)
    submiting_date  = models.DateField(auto_now=False, auto_now_add=True)
    approving_date  = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    is_finish       = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.handicapped.full_name


class Association(models.Model):
    name            = models.CharField(max_length=100)
    address         = models.CharField(max_length=100, null=True, blank=True)
    creation_date   = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    about           = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    