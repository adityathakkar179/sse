from django import forms
from .models import form

class fm(forms.ModelForm):
    class Meta:
        model=form
        fields='__all__'

