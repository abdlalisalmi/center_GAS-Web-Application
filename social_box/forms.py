from django import forms
from .models import Association, AssociationHr, AssociationStudent


class AssociationCreateForm(forms.ModelForm):
    
    class Meta:
        model   = Association
        fields  = '__all__'


class AddHRForm(forms.ModelForm):

    class Meta:
        model = AssociationHr
        fields = '__all__'


class AddStudentForm(forms.ModelForm):
    
    class Meta:
        model = AssociationStudent
        fields = '__all__'
