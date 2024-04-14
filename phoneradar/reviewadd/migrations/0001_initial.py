# Generated by Django 5.0.3 on 2024-04-05 07:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('manufacturing_since', models.DateField(null=True)),
                ('slug', models.SlugField(default='null', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('launch_date', models.DateField()),
                ('platform', models.CharField(default='null', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='model_images/')),
                ('slug', models.SlugField(default='null', max_length=150)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewadd.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.TextField()),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='null', max_length=150)),
                ('phone_model', models.ManyToManyField(to='reviewadd.model')),
            ],
        ),
    ]
