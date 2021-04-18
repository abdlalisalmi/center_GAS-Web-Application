from django.db import models

from handicapped.models import Handicapped



class Card(models.Model):
    handicapped         = models.OneToOneField(Handicapped, on_delete=models.CASCADE)
    submiting_date      = models.DateTimeField(auto_now_add=True)
    finishing_date      = models.DateTimeField(auto_now=True)
    card                = models.FileField(upload_to='cards/', max_length=100, null=True, blank=True)
    is_finish           = models.BooleanField(default=False)
    is_deleted          = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.handicapped.full_name if self.handicapped.full_name else f"card {self.id}"