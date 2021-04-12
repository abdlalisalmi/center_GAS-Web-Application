from django.db import models
from django.db.models import base

from handicapped.models import Handicapped



class Food(models.Model):
    handicapped           = models.OneToOneField(Handicapped, on_delete=models.CASCADE)
    submiting_date        = models.DateTimeField(auto_now_add=True)
    finishing_date        = models.DateTimeField(null=True, blank=True)
    is_finish             = models.BooleanField(default=False)
    is_deleted            = models.BooleanField(default=False)
    delete_description   = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return self.handicapped.full_name if self.handicapped.full_name else f"card {self.id}"