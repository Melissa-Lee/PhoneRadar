from . import views
from django.urls import path

app_name = 'addbrand'

urlpatterns = [
    path('', views.AddBrandFormView.as_view(), name='addbrand'),
]