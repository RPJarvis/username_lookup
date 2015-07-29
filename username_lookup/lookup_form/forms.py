from django import forms
from .models import Username_Query

class Username_Query_Form(forms.ModelForm):
    id = forms.CharField()
    birthdate = forms.CharField()

    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')