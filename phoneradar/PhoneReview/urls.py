from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.PhoneReviewView.as_view(), name="PhoneReview"),
    path('models/<slug:brand_slug>/', views.ModelListView.as_view(), name="ModelList"),
    path('reviews/<slug:model_slug>/', views.ReviewListView.as_view(), name="ReviewList"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
