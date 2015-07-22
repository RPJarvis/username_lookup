from django import forms
from .models import Username_Query

class Username_Query_Form(forms.ModelForm):
    id = forms.IntegerField(max_value=999999999)
    birthdate = forms.IntegerField(max_value=999999)

    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')