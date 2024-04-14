from django.forms import ModelForm
from PhoneReview.models import Brand
from django import forms


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'origin', 'manufacturing_since'] 
        widgets = {
            'manufacturing_since': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'class': 'form-control'}),
            }
        