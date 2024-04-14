"""
URL configuration for phoneradar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), #username: xingyii pw: 23072493xy
    path('', views.homepage),
    path('about/', views.about),
    path('phonereview/', include(('PhoneReview.urls', 'PhoneReview'), namespace='PhoneReview')),
    path('phonereview/models/', include(('PhoneReview.urls', 'ModelList'), namespace='ModelList')),
    path('phonereview/reviews/', include(('PhoneReview.urls', 'ReviewList'), namespace='ReviewList')),
    path('addreview/', include(('addreview.urls', 'addmodel'), namespace='addmodel')),
    path('addbrand/', include(('addbrand.urls', 'addbrand'), namespace='addbrand')),
    path('reviewadd/', include(('reviewadd.urls', 'reviewadd'), namespace='reviewadd')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)