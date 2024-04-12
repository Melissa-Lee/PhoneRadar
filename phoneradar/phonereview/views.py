from django.shortcuts import render

# Create your views here.
def phonereview_list(request):
    return render(request, 'phonereview/phonereview_list.html')