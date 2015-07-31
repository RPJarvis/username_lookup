from django.db import models
from django import forms
from django.core.validators import RegexValidator

class Username_Query(models.Model):
   # numeric = RegexValidator(r'^[0-9]+', 'Numbers only, please.')

    id = forms.CharField(max_length=9)
    birthdate = forms.CharField(max_length=6)



# Create your models here.
