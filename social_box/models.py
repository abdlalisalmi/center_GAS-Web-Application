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


class AssociationHistory(models.Model):
    year            = models.DateField(auto_now=False, auto_now_add=False)
    students_number = models.IntegerField()
    budget          = models.DecimalField(max_digits=9, decimal_places=2)
    programm        = models.CharField(max_length=100)

    def __str__(self):
        return self.year
    


class AssociationHr(models.Model):
    association     = models.ForeignKey(Association, on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    phone           = models.CharField(max_length=12, null=True, blank=True)
    education       = models.CharField(max_length=100, null=True, blank=True)
    city            = models.CharField(max_length=100, null=True, blank=True)
    month_salary    = models.DecimalField(max_digits=9, decimal_places=2)
    year_salary     = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class Student(models.Model):
    Association         = models.OneToOneField(Association, on_delete=models.CASCADE)
    full_name           = models.CharField(max_length=50)
    genre               = models.CharField(max_length=50)
    address             = models.CharField(max_length=100, null=True, blank=True)
    zone                = models.CharField(max_length=100, null=True, blank=True)
    phone_number        = models.CharField(max_length=12, null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    guardian            = models.CharField(max_length=50, null=True, blank=True)
    handicap_Type       = models.CharField(max_length=50, null=True, blank=True)
    programm_Type       = models.CharField(max_length=50, null=True, blank=True)
    services            = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.full_name