from django import forms
from .models import Association, AssociationHr


class AssociationCreateForm(forms.ModelForm):
    class Meta:
        model   = Association
        fields  = '__all__'


class AddHRForm(forms.ModelForm):
    class Meta:
        model = AssociationHr
        fields = '__all__'