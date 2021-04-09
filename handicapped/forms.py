from django.forms import ModelForm, fields
from .models import Handicapped

class HandicappedForm(ModelForm):
    class Meta:
        model = Handicapped
        exclude = ['has_card', 'request_card', ]