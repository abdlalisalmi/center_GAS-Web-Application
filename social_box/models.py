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
    is_deleted      = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AssociationHistory(models.Model):
    association     = models.ForeignKey(Association, on_delete=models.CASCADE)
    year            = models.DateField(auto_now=False, auto_now_add=False)
    students_number = models.IntegerField()
    budget          = models.DecimalField(max_digits=9, decimal_places=2)
    # programm Type
    A                   = models.BooleanField(default=False)
    B                   = models.BooleanField(default=False)
    C                   = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.association}-{self.year}"
    


class AssociationHr(models.Model):
    association     = models.ForeignKey(Association, on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    role            = models.CharField(max_length=100, null=True, blank=True)
    phone           = models.CharField(max_length=12, null=True, blank=True)
    education       = models.CharField(max_length=100, null=True, blank=True)
    city            = models.CharField(max_length=100, null=True, blank=True)
    month_salary    = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    year_salary     = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class AssociationStudent(models.Model):
    association         = models.ForeignKey(Association, on_delete=models.CASCADE)
    full_name           = models.CharField(max_length=50)
    genre               = models.CharField(max_length=50, null=True, blank=True)
    address             = models.CharField(max_length=100, null=True, blank=True)
    zone                = models.CharField(max_length=100, null=True, blank=True)
    phone_number        = models.CharField(max_length=12, null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    guardian            = models.CharField(max_length=50, null=True, blank=True)
    handicap_Type       = models.CharField(max_length=50, null=True, blank=True)
    # programm Type
    A                   = models.BooleanField(default=False)
    B                   = models.BooleanField(default=False)
    C                   = models.BooleanField(default=False)
    # services
    ES                   = models.BooleanField(default=False)
    FP                   = models.BooleanField(default=False)
    Ortho                = models.BooleanField(default=False)
    Psy                  = models.BooleanField(default=False)
    keni                 = models.BooleanField(default=False)
    Psycom               = models.BooleanField(default=False)
    Ergo                 = models.BooleanField(default=False)
    Tronsport            = models.BooleanField(default=False)

    is_deleted           = models.BooleanField(default=False)
    deleted_date         = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.full_name