from django.db import models
from django import forms

class Username_Query(models.Model):
    id = forms.IntegerField(max_value=999999999)
    birthdate = forms.IntegerField(max_value=999999)


# Create your models here.