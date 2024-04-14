from django.forms import ModelForm
from PhoneReview.models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['article', 'phone_model']
        