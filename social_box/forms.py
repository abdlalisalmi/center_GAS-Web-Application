from django import forms
from .models import Association


class AssociationCreateForm(forms.ModelForm):
    class Meta:
        model   = Association
        fields  = '__all__'