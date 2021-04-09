from django.forms import ModelForm, fields
from .models import Handicapped

class handicappedForm(ModelForm):
    class Meta:
        model = Handicapped
        exclude = ['has_card', 'request_card', ]