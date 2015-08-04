from django.db import models
from django import forms
from django.core.validators import validate_integer, ValidationError

class Username_Query(models.Model):
   # numeric = RegexValidator(r'^[0-9]+', 'Numbers only, please.')

    id = forms.CharField(min_length=9, max_length=9, label='ID Number',
                         error_messages={'invalid': 'Numbers only please.'})
    birthdate = forms.CharField(min_length=6, max_length=6, label='Birthdate',
                                error_messages={'invalid': 'Numbers only please.'})


    def clean(self):
        cd = self.cleaned_data
        if (validate_integer(cd.get('id')) == False):
            raise ValidationError(u'Numbers only please.')
        if (validate_integer(cd.get('birthdate')) == False):
            raise ValidationError(u'Numbers only please.')

        return cd
# Create your models here.
