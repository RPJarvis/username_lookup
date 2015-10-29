from django.db import models
from django import forms
from django.core.validators import validate_integer, ValidationError

class Username_Query(models.Model):
   # numeric = RegexValidator(r'^[0-9]+', 'Numbers only, please.')

    id_number = models.CharField(verbose_name="ID Number", max_length=9,
                         error_messages={'invalid': 'Numbers only please.'})
    birthdate = models.CharField(verbose_name="Birthdate <MMDDYY>", max_length=6,
                                error_messages={'invalid': 'Numbers only please.'})


    def clean(self):
        cd = self.cleaned_data
        if (validate_integer(cd.get('id')) == False):
            raise ValidationError(u'Numbers only please.')
        if (validate_integer(cd.get('birthdate')) == False):
            raise ValidationError(u'Numbers only please.')

        return cd
# id = models.CharField(verbose_name="ID Number", min_length=9, max_length=9, label='ID Number',
                    #     error_messages={'invalid': 'Numbers only please.'})
#birthdate = models.CharField(verbose_name="Birthdate", min_length=6, max_length=6, label='Birthdate',
                          #      error_messages={'invalid': 'Numbers only please.'})
