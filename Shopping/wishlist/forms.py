from django import forms
from django.forms import ModelForm
from .models import *
class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['title', 'cost', 'link']