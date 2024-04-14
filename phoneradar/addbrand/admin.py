from django.contrib import admin
from .models import Brand
from .models import Model
from .models import Review
# Register your models here.

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Review)