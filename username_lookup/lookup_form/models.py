from django.db import models
from django import forms

class Username_Query(models.Model):
    id = forms.CharField()
    birthdate = forms.CharField()


# Create your models here.
