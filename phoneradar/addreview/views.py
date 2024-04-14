from django.shortcuts import render
from django.views import generic
from .forms import ModelsForm
from PhoneReview.models import Model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class AddModelFormView(generic.TemplateView):
    template_name = 'addreview/addmodelform.html'

    def get(self, request):
        form = ModelsForm()
        models = Model.objects.all()
        args = {'form': form, 'models': models}
        return render(request, self.template_name, args)
    

    def post(self, request):
        form = ModelsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            model_name = form.cleaned_data['model_name']
            launch_date = form.cleaned_data['launch_date']
            platform = form.cleaned_data['platform']
            brand = form.cleaned_data['brand']
            image = form.cleaned_data['image']
            args = {'form': form,
                    'model_name': model_name,
                    'launch_date': launch_date,
                    'platform': platform,
                    'brand': brand,
                    'image': image}
            messages.success(request, 'The new phone model is saved successfully.')
            return HttpResponseRedirect(reverse('addreview:addmodel'))
            
            