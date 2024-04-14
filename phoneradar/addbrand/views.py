from django.shortcuts import render
from django.views import generic
from .forms import BrandForm
from PhoneReview.models import Brand
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class AddBrandFormView(generic.TemplateView):
    template_name = 'addbrand/addbrand.html'

    def get(self, request):
        form = BrandForm()
        brands = Brand.objects.all()
        args = {'form': form, 'brands': brands}
        return render(request, self.template_name, args)
    

    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            origin = form.cleaned_data['origin']
            manufacturing_since = form.cleaned_data['manufacturing_since']
            args = {'form': form,
                    'name': name,
                    'origin': origin,
                    'manufacturing_since': manufacturing_since,
                    }
            messages.success(request, 'The new phone brand is saved successfully.')
            return HttpResponseRedirect(reverse('addbrand:addbrand'))
            
            