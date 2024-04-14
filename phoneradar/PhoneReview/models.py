from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    manufacturing_since = models.DateField(null=True)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.name

class Model(models.Model):
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50, default='null')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='model_images/', null=True, blank=True)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.model_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model_name)
        super().save(*args, **kwargs)

class Review(models.Model):
    article = models.TextField()
    date_published = models.DateField(default=timezone.now)
    phone_model = models.ManyToManyField(Model)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.article
    
    def save(self, *args, **kwargs):
        if not self.id:  
            super().save(*args, **kwargs)
        if self.phone_model.exists():
                phone_model = self.phone_model.first()
                self.slug = '%i-%s' % (self.id, slugify(phone_model.model_name))
        super().save(*args, **kwargs)