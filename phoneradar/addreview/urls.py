from . import views
from django.urls import path

app_name = 'addreview'

urlpatterns = [
    path('', views.AddModelFormView.as_view(), name='addmodel'),
]