from django import forms
from .models import Association, AssociationHr, AssociationStudent, AssociationHistory, ProjectVisit


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
        exclude = ('deleted_date', 'is_deleted',)


class AddHistoryForm(forms.ModelForm):
    class Meta:
        model = AssociationHistory
        fields = '__all__'


class AddProjectVisitForm(forms.ModelForm):
    class Meta:
        model = ProjectVisit
        fields = '__all__'

