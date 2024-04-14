# Create your views here.
from django.shortcuts import render
from django.views import generic
from .forms import ReviewForm
from PhoneReview.models import Review
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class AddReviewFormView(generic.TemplateView):
    template_name = 'reviewadd/reviewadd.html'

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()
        args = {'form': form, 'reviews': reviews}
        return render(request, self.template_name, args)
    

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            article = form.cleaned_data['article']
            phone_model = form.cleaned_data['phone_model']
            args = {'form': form,
                    'article': article,
                    'phone_model': phone_model
                    }
            messages.success(request, 'The new review is saved successfully.')
            return HttpResponseRedirect(reverse('reviewadd:reviewadd'))
            
            