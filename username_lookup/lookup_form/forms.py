from django import forms
from .models import Username_Query
from captcha.fields import ReCaptchaField
from django.core.validators import validate_integer, ValidationError
from django.core.validators import RegexValidator

class Username_Query_Form(forms.Form):
    def validate_fields(value):
        if (validate_integer(value) == False):
            raise forms.ValidationError('Numbers only please.')
        return value

    error_messages = {
        'invalid': 'Numbers only please. ',
        'min_length': 'Ensure this value has 6 characters.'
    }
    id = forms.CharField(min_length=9, max_length=9, label='ID Number', validators=[validate_fields],
                         error_messages = {
                            'invalid': 'Numbers only please. ',
                            'min_length': 'Ensure this value has 9 characters.'
                        })

    birthdate = forms.CharField(min_length=6, max_length=6, label='Birthdate', validators=[validate_fields],
                                error_messages = {
                                    'invalid': 'Numbers only please. ',
                                    'min_length': 'Ensure this value has 6 characters.'
                                })
    captcha = ReCaptchaField()

    class Meta:
        model = Username_Query
        fields = ('id', 'birthdate')




