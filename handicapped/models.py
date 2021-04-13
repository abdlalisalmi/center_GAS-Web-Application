from django.db import models
from django.urls import reverse


class Handicapped(models.Model):
    full_name           = models.CharField(max_length=50)
    genre               = models.CharField(max_length=50)
    address             = models.CharField(max_length=100, null=True, blank=True)
    phone_number        = models.CharField(max_length=12, null=True, blank=True)
    cin                 = models.CharField(max_length=20, null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    birth_address       = models.CharField(max_length=100, null=True, blank=True)
    guardian            = models.CharField(max_length=50, null=True, blank=True)
    handicap_Type       = models.CharField(max_length=50, null=True, blank=True)

    is_deleted          = models.BooleanField(default=False)
    delete_description  = models.TextField(null=True, blank=True)

    has_card            = models.BooleanField(default=False)
    request_card        = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name if self.full_name else f"handicapped {self.id}"
    
    def get_absolute_url(self):
        return f'/search/{self.pk}'
    