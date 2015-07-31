from django import forms
from .models import Username_Query
from captcha.fields import ReCaptchaField
from django.core.validators import RegexValidator

class Username_Query_Form(forms.ModelForm):
   # numeric = RegexValidator(r'^[0-9]+', 'Numbers only, please.')
   #^[0-9]*$

    id = forms.CharField(max_length=9)
    birthdate = forms.CharField(max_length=6)
    captcha = ReCaptchaField()


    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')