from django import forms
from .models import Username_Query
from captcha.fields import ReCaptchaField

class Username_Query_Form(forms.ModelForm):
    id = forms.CharField()
    birthdate = forms.CharField()
    captcha = ReCaptchaField()


    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')