from django import forms
from .models import Username_Query
from captcha.fields import ReCaptchaField
from django.core.validators import validate_integer, ValidationError
from django.core.validators import RegexValidator

class Username_Query_Form(forms.Form):
   # numeric = RegexValidator(r'^[0-9]+', 'Numbers only, please.')
   #^[0-9]*$

    id = forms.CharField(max_length=9, label='ID Number', initial='<xxxxxxxxx>')
    birthdate = forms.CharField(max_length=6, label='Birthdate', initial='<MMDDYY>')
    captcha = ReCaptchaField()

    def clean(self):
        cd = self.cleaned_data
        if (validate_integer(cd.get('id')) == False):
            raise ValidationError('Numbers only please.')
        if (validate_integer(cd.get('birthdate')) == False):
            raise ValidationError('Numbers only please.')

        return cd

    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')

        labels = {
            'id': 'Nine digit ID number',
        }