# Generated by Django 4.1.7 on 2023-03-07 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=500)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(choices=[('EC', 'Eastern Cape'), ('FS', 'Free State'), ('GP', 'Gauteng'), ('KZN', 'KwaZulu-Natal'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'), ('NC', 'Northern Cape'), ('NW', 'North West'), ('WC', 'Western Cape')], max_length=200)),
                ('postal_code', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('photo_one', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('photo_two', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('photo_three', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('photo_four', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('photo_five', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('photo_six', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]