from django import forms
from DD.models import Course


class EditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']