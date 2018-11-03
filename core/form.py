from django import forms
from django.core.validators import MaxValueValidator, MaxValueValidator

class GenerateRandomUserForms(forms.Form):
    total = forms.IntegerField(validators=[MinValueValidator(50),
            MaxValueValidator(500)])