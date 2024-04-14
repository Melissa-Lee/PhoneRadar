from . import views
from django.urls import path

app_name = 'reviewadd'

urlpatterns = [
    path('', views.AddReviewFormView.as_view(), name='reviewadd'),
]