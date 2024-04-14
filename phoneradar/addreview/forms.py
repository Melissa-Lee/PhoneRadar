from django.forms import ModelForm
from PhoneReview.models import Model
from django import forms


class ModelsForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['model_name', 'launch_date', 'platform', 'brand', 'image', 'slug'] #all fields are needed
        widgets = {
            'launch_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'class': 'form-control'}),
        }
        