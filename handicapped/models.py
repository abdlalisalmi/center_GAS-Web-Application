from django.db import models
from django.urls import reverse


class Handicapped(models.Model):
    association         = models.ForeignKey('social_box.Association', on_delete=models.CASCADE, null=True, blank=True)
    full_name           = models.CharField(max_length=50)
    genre               = models.CharField(max_length=50)
    address             = models.CharField(max_length=100, null=True, blank=True)
    zone                = models.CharField(max_length=100, null=True, blank=True)
    phone_number        = models.CharField(max_length=12, null=True, blank=True)
    cin                 = models.CharField(max_length=20, null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    birth_address       = models.CharField(max_length=100, null=True, blank=True)
    guardian            = models.CharField(max_length=50, null=True, blank=True)
    handicap_Type       = models.CharField(max_length=50, null=True, blank=True)

    is_deleted          = models.BooleanField(default=False)
    deleted_date        = models.DateField(null=True, blank=True)
    delete_description  = models.TextField(null=True, blank=True)

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

    def __str__(self) -> str:
        return self.full_name if self.full_name else f"handicapped {self.id}"
    
    def get_absolute_url(self):
        return f'/search/{self.pk}'
    