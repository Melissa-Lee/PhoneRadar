from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView

from .models import Brand
from .models import Model
from .models import Review

# Create your views here.

class PhoneReviewView(generic.ListView):
    model = Brand
    template_name = 'PhoneReview/phonereview_list.html'  # Template to render list of brands
    context_object_name = 'brands'

    def get_queryset(self):
        return Brand.objects.all()

class ModelListView(generic.ListView):
    model = Model
    template_name = 'PhoneReview/model.html'
    context_object_name = 'models'
    
    def get_queryset(self):
        brand = get_object_or_404(Brand, slug=self.kwargs['brand_slug'])
        return Model.objects.filter(brand=brand)


class ReviewListView(generic.ListView):
    model = Review
    template_name = 'PhoneReview/review.html'
    context_object_name = 'reviews'
    
    def get_queryset(self):
        phone_model = get_object_or_404(Model, slug=self.kwargs['model_slug'])
        return Review.objects.filter(phone_model=phone_model)


    