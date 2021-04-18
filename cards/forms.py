from django.forms import ModelForm, fields
from .models import Card

class AddCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['handicapped',]


class UploadCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['card',]